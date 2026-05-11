# 🌟 Aura-AI: RAG-Powered Digital Representative

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-blue?style=flat)](https://www.trychroma.com/)
[![Gemini](https://img.shields.io/badge/LLM-Gemini_2.5_Flash-4285F4?style=flat&logo=google&logoColor=white)](https://ai.google.dev/)

**Aura-AI** is a sophisticated **Retrieval-Augmented Generation (RAG)** system designed to act as an autonomous digital representative. Unlike static portfolios, Aura leverages a vector database to provide contextually accurate, real-time responses regarding technical expertise, project history, and software development progress.

---

## 🚀 Key Features

* **Context-Aware Intelligence:** Uses RAG architecture to ensure responses are grounded in verified data logs.
* **Vectorized Memory:** Implemented **ChromaDB** for efficient storage and semantic retrieval of technical milestones.
* **High-Speed Inference:** Integrated with **Gemini 2.5 Flash** for sub-second response times and intelligent synthesis.
* **API-First Design:** Built on **FastAPI**, featuring a fully documented Swagger UI for seamless technical auditing.
* **Secure Architecture:** Professional-grade environment management using `.env` abstraction for sensitive API credentials.

---

## 🛠️ Technical Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.13 |
| **Framework** | FastAPI |
| **Vector Database** | ChromaDB |
| **LLM Engine** | Google Gemini 2.5 Flash |
| **DevOps** | Git, GitHub, Python-Dotenv |

---

## 📦 Installation & Setup

Follow these steps to deploy a local instance of Aura-AI:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/me-devgarg/Aura-AI.git](https://github.com/me-devgarg/Aura-AI.git)
    cd Aura-AI
    ```

2.  **Environment Configuration:**
    Create a `.env` file in the root directory and add your Gemini API Key:
    ```text
    GEMINI_API_KEY=your_actual_key_here
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch Aura:**
    ```bash
    uvicorn main:app --reload
    ```

---

## 📈 Project Roadmap

- [ ] **Multimodal Context:** Enabling Aura to process project screenshots and code snippets.
- [ ] **Live GitHub Sync:** Automatically updating the knowledge base via GitHub Webhooks.
- [ ] **Conversational UI:** Launching a React-based frontend for public interaction.

---

## 🤝 Connect

* **GitHub:** [github.com/me-devgarg](https://github.com/me-devgarg)
* **Status:** B.Tech @ VIT Bhopal (Gaming Technology)
* **Focus:** SDE | Data Analytics | AI-First Development

---
Developed by Dev Garg • 2026