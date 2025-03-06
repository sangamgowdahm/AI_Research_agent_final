from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_community.llms import Ollama
from langchain.callbacks.tracers.langchain import LangChainTracer
import requests
from bs4 import BeautifulSoup
import os
from langchain.schema.runnable import RunnablePassthrough
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain.retrievers import ArxivRetriever
from langchain_community.tools.tavily_search import TavilySearchResults
import json


RESULTS_PER_QUESTION = 4
os.environ["TAVILY_API_KEY"] = "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"  


ddg_search = DuckDuckGoSearchAPIWrapper()
retriever = ArxivRetriever()
tavily_search = TavilySearchResults(tavily_api_key=os.getenv("TAVILY_API_KEY"))


def web_search(query: str, num_results: int = RESULTS_PER_QUESTION):
    try:
        tavily_results = tavily_search.run(query, max_results=num_results)
    except Exception as e:
        print(f"Tavily API error: {e}")
        tavily_results = []

    ddg_results = ddg_search.results(query, num_results)

    return list(set(tavily_results + [r["link"] for r in ddg_results]))

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"


SUMMARY_TEMPLATE = """{text} 
-----------
Using the above content, provide a concise and insightful response to the following question: 
> {question}
-----------
If the question cannot be answered from the text, extract the most relevant key points in a structured manner.
Provide a **brief yet informative** summary.
"""
SUMMARY_PROMPT = ChatPromptTemplate.from_template(SUMMARY_TEMPLATE)


def scrape_text(url: str):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            return soup.get_text(separator=" ", strip=True)[:1800] 
        else:
            return f"Failed to retrieve the webpage: Status code {response.status_code}"
    except Exception as e:
        return f"Failed to retrieve the webpage: {e}"


llm = Ollama(model="deepseek-r1")  
tracer = LangChainTracer()


scrape_and_summarize_chain = (
    RunnablePassthrough.assign(
        text=lambda x: scrape_text(x["url"])
    ) | SUMMARY_PROMPT | llm | StrOutputParser()
) | (lambda x: f"Summary:{x}")


web_search_chain = (
    RunnablePassthrough.assign(
        urls=lambda x: web_search(x["question"]),
        docs=lambda x: retriever.get_summaries_as_docs(x["question"])
    )
    | (lambda x: [{"question": x["question"], "url": u} for u in x["urls"]] + 
                 [{"question": x["question"], "doc": d} for d in x["docs"]])
    | scrape_and_summarize_chain.map()
)


SEARCH_PROMPT = ChatPromptTemplate.from_messages([
    ("user", 
     "**Task:** Generate 3 highly specific and effective search queries to retrieve the best information for:\n\n"
     "**Query:** {question}\n\n"
     "**Guidelines:**\n"
     "1️ The queries should be unique, precise, and context-aware.\n"
     "2️ Each query should focus on a different **aspect** of the question.\n"
     "3️ Format the output as a valid JSON list:\n"
     "[\"query 1\", \"query 2\", \"query 3\"]"
    )
])

def safe_json_loads(response_text):
    try:
        print("Raw LLM Output:", response_text)
        return json.loads(response_text)
    except json.JSONDecodeError:
        print("JSONDecodeError: Invalid JSON received from LLM. Raw output:", response_text)
        return []


search_question_chain = SEARCH_PROMPT | llm | StrOutputParser() | safe_json_loads

full_research_chain = (
    search_question_chain
    | (lambda x: [{"question": q} for q in x])
    | web_search_chain.map()
)


WRITER_SYSTEM_PROMPT = (
    "You are an AI-powered research assistant, skilled in critical thinking, in-depth analysis, and academic writing. "
    "Your task is to generate well-structured, data-backed reports using markdown formatting."
) 

RESEARCH_REPORT_TEMPLATE = """##  Research Report  
### **Topic:** "{question}"  

---
### ** Summary of Findings**
{research_summary}

---
### **🔍 Detailed Analysis**  
1️⃣ Present facts, statistics, and evidence-based insights.  
2️⃣ Offer in-depth explanations, ensuring clarity and relevance.  
3️⃣ Include **real-world examples**, where applicable.  

---
### ** References**
List all used sources (avoid duplicates). Format in **APA style**.

---
** Note:** This report should be detailed (minimum **1,500 words**). Ensure originality and high-quality content.
""" 

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", WRITER_SYSTEM_PROMPT),
        ("user", RESEARCH_REPORT_TEMPLATE),
    ]
)


def collapse_list_of_lists(list_of_lists):
    content = []
    for l in list_of_lists:
        content.append("\n\n".join(l))
    return "\n\n".join(content)


chain = RunnablePassthrough.assign(
    research_summary= full_research_chain | collapse_list_of_lists
) | prompt | llm | StrOutputParser()


from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(
  title="Research Agent",
  version="1.0",
  description="An advanced research agent powered by Tavily, DuckDuckGo, and LangChain.",
)

add_routes(
    app,
    chain,
    path="/research-assistant",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
