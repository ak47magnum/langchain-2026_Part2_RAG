

import asyncio
import os
import ssl
from typing import Any, Dict, List

import certifi
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_chroma import Chroma     #############   for indexing locally
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_tavily import TavilyCrawl, TavilyExtract, TavilyMap
load_dotenv()

from logger import (
    log_error,
    log_info,
    log_success,
    log_warning,
    log_header,
    Colors,)




## Configure SSL context to use certifi
ssl_context = ssl.create_default_context(cafile=certifi.where())
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()


embeddings = OpenAIEmbeddings(model="text-embedding-3-small", show_progress_bar=True, chunk_size=50, retry_min_seconds=10)

# chroma = Chroma(persist_directory="chroma_db", embedding_function=embeddings) ## Example for chroma database

vectorstore = PineconeVectorStore(
    index_name=os.environ.get("INDEX_NAME"),
    embedding=embeddings,
)
tavily_extract = TavilyExtract()
tavily_map = TavilyMap(max_depth=5, max_breadth=20, max_pages=1000)
tavily_crawl = TavilyCrawl()


async def main():
    """Main async function to orchestrate the entire proccess."""
    log_header("DOCUMENTATION INGESTION PIPELINE")

    log_info("Starting Tavily crawl from httpa://python.langchain.com",
             Colors.PURPLE,
             )
    

    # Crawl the documentation site

    res = tavily_crawl.invoke({
        "url": "https://python.langchain.com",
        "max_depth": 2,
        "extract_depth": "advanced",
        "instructions":"All about  agents"
    })


    all_docs = [Document(page_content=result["raw_content"], metadata={"source": result['url']}) for result in res["results"]]
    log_success(f"Tavily crawl completed! Found {len(all_docs)} URL's from documentation Site")
    
    print (len(all_docs)) ## for debug
    print(all_docs)
    
   

if __name__ == "__main__":
    asyncio.run(main())


