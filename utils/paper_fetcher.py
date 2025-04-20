import requests
from bs4 import BeautifulSoup

def fetch_paper_from_url(url):
    if "arxiv.org" in url:
        # Extract arXiv ID
        arxiv_id = url.split("/")[-1]
        api_url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
        response = requests.get(api_url)
        soup = BeautifulSoup(response.text, "xml")
        entry = soup.find("entry")
        if entry:
            return {
                "title": entry.title.text,
                "summary": entry.summary.text.strip(),
                "published": entry.published.text,
                "clean_text": entry.summary.text.strip(),  # this is essential for the summarizer
                "source": "arXiv",
                "link": entry.id.text  # Include the direct link
            }
    elif "doi.org" in url:
        return fetch_from_doi(url)
    else:
        return {"error": "Unsupported URL"}


def fetch_from_doi(doi_url):
    doi = doi_url.split("doi.org/")[-1]
    api_url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(api_url)
    if response.status_code != 200:
        return {"title": "DOI Error", "clean_text": "DOI not found or invalid"}

    data = response.json()
    item = data.get("message", {})

    return {
        "title": item.get("title", [""])[0],
        "summary": item.get("abstract", "No abstract available").replace("<jats:p>", "").replace("</jats:p>", ""),
        "published": str(item.get("published-print", {}).get("date-parts", [[None]])[0][0]),
        "source": "Crossref",
        "clean_text": item.get("abstract", "No abstract available")
    }
