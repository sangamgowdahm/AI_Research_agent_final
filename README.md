# 🌟 AI Research Agent

Welcome to the **AI Research Agent** project! This AI-powered assistant is designed to streamline and enhance the research process by autonomously collecting, analyzing, and summarizing information from diverse sources.

🔗 **GitHub Repository**: [AI Research Agent Final](https://github.com/sangamgowdahm/AI_Research_agent_final)  
📄 **Project Report**: [View Report (PDF)](https://drive.google.com/file/d/12Ybl2kcKqWhcq_cL8r2lmcZJnoMZvNCB/view?usp=sharing)  
🎥 **Video Explanation**: [Watch Detailed Video](https://drive.google.com/file/d/18nETr0lNAEYBwJ5dpBN0CT9S4B6mOgxI/view?usp=sharing)  

---

## 📄 Project Overview

The **AI Research Agent** is an advanced, AI-driven research system designed to perform in-depth analysis by leveraging multiple online sources, synthesizing insights, and generating structured, **APA-formatted research reports**. The system integrates state-of-the-art technologies, including:

- **LangChain & LangGraph** – AI workflow orchestration  
- **Ollama (DeepSeek-R1 LLM)** – Natural language processing and summarization  
- **Tavily API, DuckDuckGo API, and Arxiv Retriever** – Intelligent search and academic research  
- **FAISS Vector Search** – Storage and retrieval of past research  
- **FastAPI with LangServe** – API-based interaction  
- **BeautifulSoup** – Web scraping for extracting information  
- **Streamlit (Future Scope)** – User-friendly UI for interaction  

---

## ✨ Key Features

### 🔍 **Multi-Source Research & Data Collection**
The agent collects information from multiple sources, prioritizing them for **accuracy and reliability**:

- **Tavily API** – AI-powered web search tool retrieving high-quality results.  
- **DuckDuckGo API** – Privacy-focused search engine for additional coverage.  
- **Arxiv Retriever** – Fetches academic papers from ArXiv for scientific content.  
- **Web Scraping (BeautifulSoup)** – Extracts content when API results are insufficient.  

### 🏆 **Intelligent Search Query Optimization**
A **custom search prompt** generates highly optimized queries to retrieve **relevant** information:

1. Understands the user's question using **deep learning models**.  
2. Generates **three refined search queries**, each targeting a different aspect.  
3. Executes searches across **multiple engines**, merging results intelligently.  

### 🧠 **Research Summarization & NLP**
Using **DeepSeek-R1 via Ollama**, the system:  
- Processes **raw data** from searches.  
- Summarizes large documents into **structured insights**.  
- Extracts **key points** when direct answers aren’t available.  

### 📑 **Structured Report Generation**
The system **automatically generates well-structured, 1200+ word** research reports with:  
- **Summary of Findings** – A concise synthesis of all sources.  
- **Detailed Analysis** – Fact-based breakdown with real-world examples.  
- **References** – Properly formatted **APA citation** section.  

---

## ⚙️ Technical Architecture

The system follows a **modular and scalable architecture**, making it easy to expand.

### 🔗 **Core Components**
#### 1️⃣ **LangChain & LangGraph** (AI Workflow)  
- Facilitates complex **AI pipeline orchestration**.  
- Enables **multi-agent collaboration** and branching logic.  

#### 2️⃣ **Ollama & DeepSeek-R1 (LLM Processing & Summarization)**  
- **4.7GB open-source LLM** used for text comprehension and report generation.  
- Summarizes research and writes **coherent narratives**.  

#### 3️⃣ **Search & Data Retrieval**  
- **Tavily API** – Primary web search for high-quality information.  
- **DuckDuckGo API** – Expands search coverage.  
- **Arxiv Retriever** – Fetches academic papers for deeper analysis.  

#### 4️⃣ **FAISS (Vector Search for Knowledge Storage)**  
- Stores past research **efficiently** to prevent redundant queries.  
- Enables quick recall of **previously analyzed topics**.  

#### 5️⃣ **Web Scraping with BeautifulSoup**  
- Extracts webpage content **when API searches lack sufficient data**.  
- Limits output to **1500 characters per page** for relevance.  

#### 6️⃣ **FastAPI & LangServe (API Deployment)**  
- Exposes the **AI Research Agent as a REST API endpoint**.  
- Future integration with **Streamlit UI** for enhanced user experience.  

---

## 🚀 Workflow Execution

1️⃣ **User Inputs a Research Query**  
- The system **generates three optimized search queries**.  
- Searches are executed across **Tavily, DuckDuckGo, and Arxiv**.  

2️⃣ **Information Retrieval & Summarization**  
- If relevant content is found, **web scraping** is triggered.  
- **DeepSeek-R1 processes and summarizes** the retrieved information.  

3️⃣ **Structured Report Generation**  
- Insights are formatted into **a Markdown-based APA report**.  
- The report includes **Key Findings, Analysis, and References**.  

4️⃣ **API Deployment & Future UI Integration**  
- Results are **served via FastAPI & LangServe**.  
- Future **Streamlit UI** for user-friendly interaction.  
