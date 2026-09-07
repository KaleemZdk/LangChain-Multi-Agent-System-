from langchain.tools import tool
import requests
from dotenv import load_dotenv
import os 
from tavily import TavilyClient
from rich import print
from bs4 import BeautifulSoup
from readability import Document
import trafilatura
import re 

load_dotenv()

tavily = TavilyClient(api_key= os.getenv("TAVILY_API_KEY"))
@tool
def web_search(query:str)->str:
    results = tavily.search(query=query, max_results=5)

    out= []

    for r in results['results']:
        out.append(
            f"Title:{r['title']}\nURL:{r['url']}\nSnippet:{r['content'][:300]}\n"
        )
    return "\n----\n".join(out)
    
@tool
def scrape_url(url: str) -> str:
    """Fetch a webpage and return its main readable text content (boilerplate,
    nav bars, and ads stripped out). Use this after web_search when you need
    the full content of a specific result, not just its snippet."""
 
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
        )
    }
 
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Error fetching {url}: {e}"
 
    html = response.text
 
    # 1. trafilatura first — usually the best at stripping boilerplate/ads
    text = trafilatura.extract(html, include_comments=False, include_tables=False)
 
    # 2. fall back to readability + BeautifulSoup if trafilatura found nothing
    if not text:
        try:
            doc = Document(html)
            soup = BeautifulSoup(doc.summary(), "html.parser")
            text = soup.get_text(separator="\n")
        except Exception:
            text = ""
 
    # 3. last resort — raw BeautifulSoup text dump
    if not text:
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(separator="\n")
 
    # clean up whitespace
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text).strip()
 
    if not text:
        return f"Could not extract readable content from {url}"
 
    max_chars = 5000
    if len(text) > max_chars:
        text = text[:max_chars] + "... [truncated]"
 
    return text

