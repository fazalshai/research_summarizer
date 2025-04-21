# Research Paper Summarization Multi-Agent System
![WhatsApp Image 2025-04-20 at 21 00 20_9d88815b](https://github.com/user-attachments/assets/f2122180-e949-4abf-afb8-84d7f5999492)

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

## Install Dependencies

The following libraries are used in this project:

- `flask` - Web framework to create the server.
- `requests` - To make HTTP requests for fetching papers.
- `beautifulsoup4` - To parse and extract information from HTML.
- `google-generativeai` - For generating summaries using the Gemini API.
- `gTTS` - Google Text-to-Speech for generating audio summaries.
- `PyPDF2` - To extract text from PDFs.
- `flask` - To build the Flask web application.
- `bs4` - BeautifulSoup to parse HTML/XML documents.
## Running the Project

Follow the steps below to get the project up and running:

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/fazalshai/research_summarizer
2. **Run app.py**

   This will start the web application, and you can access it on your browser at:
   ```bash
          Localhost: http://127.0.0.1:5000/ (for local access)

         Remote Access (Your IP address): http://<your-ip-address>:5000/ (replace <your-ip-address> with your actual machine's IP address)

# Output Examples
Summary Output Example

Title: "Deep Learning in AI"
Summary: This paper explores the various applications of deep learning techniques in artificial intelligence. It covers neural networks, computer vision, and natural language processing advancements in AI systems...
- **Audio Summary Output Example**:
![WhatsApp Image 2025-04-20 at 21 05 12_d310196e](https://github.com/user-attachments/assets/4bf636ee-eafd-41fa-871e-165d384fb8bd)

Audio Version: AI-Predicted Summary is saved as `summary.mp3`.
App Interface & Screenshots
The web app provides an interactive interface to upload papers, visualize summaries, and download audio.

-**1. Home Page – Upload Papers**
Allows users to upload their own PDFs, view summaries, and download audio.

![WhatsApp Image 2025-04-20 at 21 00 20_d6dd92a0](https://github.com/user-attachments/assets/ff4c76c3-5249-4796-a5d6-307eaa779092)


- **2. Search Page – Search Papers**
Search for papers based on topics, with filters like relevance and recency.

![WhatsApp Image 2025-04-20 at 21 05 46_3901d710](https://github.com/user-attachments/assets/40ff24ea-6213-4376-bd9b-8a6026015a22)


- **3. Paper Summarization**
The app generates summaries of research papers and displays them.

![WhatsApp Image 2025-04-20 at 21 05 12_9dc67582](https://github.com/user-attachments/assets/0746928d-68c5-4a57-9daa-3ae4b30d2d4e)


4. Audio Summary
Download or listen to the audio version of the paper summary.

![WhatsApp Image 2025-04-20 at 21 03 56_ac01840a](https://github.com/user-attachments/assets/c6b7c28f-caa7-4774-b758-c56e4c4bd618)

Notes
DOI and URL Handling: The system fetches papers directly from repositories like arXiv or Crossref.

API Key: To use the Gemini API for LLM-powered summaries, you need an API key.

Dependencies: Ensure all dependencies are installed via pip install -r requirements.txt.

# Future Improvements
Multi-Paper Summarization: Improve cross-paper synthesis by handling more papers simultaneously.

Interactive UI: Add more interactive features like saving papers and summaries for later access.

Topic Expansion: Integrate a broader set of topics for paper classification.
