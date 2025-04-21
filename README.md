# Research Paper Summarization Multi-Agent System

This project builds a **multi-agent system** that can find, analyze, and summarize research papers from various sources, organize them by topic, and generate audio podcasts discussing the findings.  
Users can upload research papers, search for relevant academic papers based on topics, or use URLs and DOIs. The system processes them, organizes them by topics, and generates easy-to-understand summaries.
# Demo Links

- **Practical Demo**: [Watch the Demo](https://youtu.be/9sMl821pJMI) 
- **Theory Explanation**: [Watch the Explanation](https://youtu.be/I4u3cVgUfpo)
- **Code Explanation**:[Watch the Explanation](https://youtu.be/i3uPd2IQrUg)
---
# Features

- **Paper Search and Discovery**: Search for research papers based on topics and filter them by relevance or recency.
- **PDF Upload and Processing**: Upload PDFs and process them into readable text for summarization.
- **DOI and URL Handling**: Fetch research papers directly from URLs or DOIs for processing.
- **Topic Classification**: Classify papers into predefined topics.
- **Summary Generation**: Generate short, accurate summaries of research papers.
- **Cross-paper Synthesis**: Combine summaries from multiple papers into one cohesive document.
- **Audio Summaries**: Generate audio versions of paper summaries for easier consumption.

## Project Structure

| File                      | Description                                                                                              |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| `agents/search_agent.py`   | Paper search agent for querying and filtering research papers by topics.                                  |
| `agents/summarize_agent.py`| Summarizes research papers using the **Gemini** API for LLM integration.                                  |
| `agents/audio_agent.py`    | Generates audio summaries using **gTTS** (Google Text-to-Speech).                                        |
| `agents/classify_agent.py` | Classifies papers based on a user-provided list of topics.                                               |
| `app.py`                  | Flask-based web app for uploading, searching, and summarizing papers.                                    |
| `utils/paper_fetcher.py`   | Fetches research papers from URLs and DOIs using **arXiv** and **Crossref** APIs.                         |
| `templates/`               | Contains HTML templates for the user interface.                                                           |
| `static/`                  | Contains CSS and other static files for styling the web app.                                             |

# Prerequisites

# Install Python 3.11.x

Download and install Python 3.11.x from the [official Python website](https://www.python.org/downloads/).

# Upgrade Pip

python -m pip install --upgrade pip
Install Dependencies
sh
Copy
pip install -r requirements.txt
The requirements.txt file includes all necessary Python packages like flask, requests, beautifulsoup4, google-generativeai, and more.

Running the Project
Start the Flask Application:

sh
Copy
python app.py
This starts the web app where users can upload PDFs, fetch papers using DOIs or URLs, and view summaries or download audio versions.

- **Search for Papers:

Use the Search bar to search for research papers based on specific topics.

**Upload Papers:

Users can drag and drop or browse PDF files for automatic summarization.

**Fetch Papers via DOI or URL:

Enter the DOI or URL of a paper to fetch it from repositories like arXiv and Crossref.

**Generate Summaries:

The system will automatically generate a summary of the uploaded paper or fetched papers.

**Download Audio Summary:

After the paper is summarized, the system generates an audio podcast of the summary.

**Output Examples
Summary Output Example
sql
Copy
Title: "Deep Learning in AI"
Summary: This paper explores the various applications of deep learning techniques in artificial intelligence. It covers neural networks, computer vision, and natural language processing advancements in AI systems...
Audio Summary Output Example
pgsql
Copy
Audio Version: AI-Predicted Summary is saved as `summary.mp3`.
App Interface & Screenshots
The web app provides an interactive interface to upload papers, visualize summaries, and download audio.

1. Home Page – Upload Papers
Allows users to upload their own PDFs, view summaries, and download audio.

Screenshot File: screenshots/upload_page.png

2. Search Page – Search Papers
Search for papers based on topics, with filters like relevance and recency.

Screenshot File: screenshots/search_page.png

3. Paper Summarization
The app generates summaries of research papers and displays them.

Screenshot File: screenshots/summarized_page.png

4. Audio Summary
Download or listen to the audio version of the paper summary.

Screenshot File: screenshots/audio_page.png

Notes
DOI and URL Handling: The system fetches papers directly from repositories like arXiv or Crossref.

API Key: To use the Gemini API for LLM-powered summaries, you need an API key.

Dependencies: Ensure all dependencies are installed via pip install -r requirements.txt.

Future Improvements
Multi-Paper Summarization: Improve cross-paper synthesis by handling more papers simultaneously.

Interactive UI: Add more interactive features like saving papers and summaries for later access.

Topic Expansion: Integrate a broader set of topics for paper classification.
