# agents/search_agent.py
import requests
from bs4 import BeautifulSoup

class PaperSearchAgent:
    def search_papers(self, query="AI", max_results=5, sort_by="relevance"):
        url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}&sortBy={sort_by}"
        response = requests.get(url)

        try:
            # Use lxml parser
            soup = BeautifulSoup(response.text, "lxml")
        except Exception as e:
            print(f"⚠️ Error with lxml, falling back to html.parser: {e}")
            soup = BeautifulSoup(response.text, "html.parser")  # Fallback to html.parser

        papers = []
        for entry in soup.find_all("entry"):
            papers.append({
                "title": entry.title.text,
                "summary": entry.summary.text.strip(),
                "published": entry.published.text,
                "link": entry.id.text,
                "clean_text": entry.summary.text.strip(),
                "source": "arXiv"
            })
        return papers
