import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import chromadb
from chromadb.utils import embedding_functions

# 1. Load Environment Variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ ERROR: GEMINI_API_KEY not found in .env file!")

# 2. Configure Gemini (Using 2.5-Flash for better stability/quota)
genai.configure(api_key=api_key)
SELECTED_MODEL = 'gemini-2.5-flash'
model = genai.GenerativeModel(SELECTED_MODEL)

# 3. Setup Memory (ChromaDB)
client = chromadb.PersistentClient(path="./aura_memory")
default_ef = embedding_functions.DefaultEmbeddingFunction()
collection = client.get_or_create_collection(name="dev_profile", embedding_function=default_ef)

# 4. Define Request Structure
class QueryRequest(BaseModel):
    user_query: str

# 5. Initialize FastAPI
app = FastAPI(title="Aura AI")

@app.on_event("startup")
async def load_knowledge():
    print(f"🚀 Aura is starting up using model: {SELECTED_MODEL}")
    if os.path.exists("knowledge_base.txt"):
        with open("knowledge_base.txt", "r") as f:
            content = f.read()
            facts = [line.strip() for line in content.split('\n') if line.strip()]
            if facts:
                collection.upsert(
                    documents=facts,
                    ids=[f"id_{i}" for i in range(len(facts))]
                )
                print(f"✅ Aura synchronized with {len(facts)} facts.")
            else:
                print("⚠️ knowledge_base.txt is empty.")
    else:
        print("⚠️ knowledge_base.txt not found.")

@app.get("/")
def home():
    return {"status": "Aura is online."}

@app.post("/ask")
async def ask_aura(request: QueryRequest):
    try:
        results = collection.query(query_texts=[request.user_query], n_results=2)
        retrieved_context = " ".join(results['documents'][0]) if results['documents'] else "No context found."
        
        prompt = f"""
        You are 'Aura', the AI representative for Dev Garg. 
        Context: {retrieved_context}
        Question: {request.user_query}
        
        Answer professionally and concisely as his representative.
        """
        
        response = model.generate_content(prompt)
        return {"aura_response": response.text}

    except Exception as e:
        print(f"❌ AURA ERROR: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))