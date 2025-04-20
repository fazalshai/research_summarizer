from flask import Flask, render_template, request, send_file
from agents.summarize_agent import SummaryGenerationAgent
from agents.audio_agent import AudioGenerationAgent
from utils.paper_fetcher import fetch_paper_from_url
from agents.search_agent import PaperSearchAgent

from PyPDF2 import PdfReader
import os

app = Flask(__name__)

# Initialize agents
summarizer = SummaryGenerationAgent()
audio_gen = AudioGenerationAgent()

# Folder for saving uploaded PDFs
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
search_agent = PaperSearchAgent()
# 🏠 Home route - Upload UI
@app.route('/')
def index():
    return render_template('index.html')

# 📄 Upload PDF file
@app.route('/upload', methods=['POST'])
def upload():
    if 'pdf' not in request.files:
        return 'No file uploaded', 400

    file = request.files['pdf']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Extract text
    text = ""
    with open(file_path, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages[:3]:  # Limit to 3 pages for quick summary
            text += page.extract_text()

    paper = {'title': file.filename, 'clean_text': text}
    summarized = summarizer.generate_summary(paper)
    summary = summarized['summary']

    # Generate podcast
    audio_gen.generate_audio(summary)

    return render_template('result.html', summary=summary, paper=paper)


@app.route('/fetch_url', methods=['POST'])
def fetch_url():
    try:
        url = request.form['url']
        print(f"📥 Received URL/DOI: {url}")

        # Fetch the paper based on the URL (arXiv or DOI)
        paper = fetch_paper_from_url(url)
        print(f"Fetched paper: {paper}")  # Debug line

        # Ensure that the 'paper' object contains valid data
        if 'clean_text' not in paper or not paper['clean_text']:
            return f"<h3 style='color:red;'>❌ Unable to extract paper summary from this URL or DOI.</h3>", 400
        
        # Generate the summary using the summarizer
        summarized = summarizer.generate_summary(paper)
        summary = summarized['summary']

        # Generate the audio podcast
        audio_gen.generate_audio(summary)

        # Pass both paper and summary to the result page
        return render_template('result.html', summary=summary, paper=paper)

    except Exception as e:
        print(f"❌ Error during DOI/URL processing: {e}")
        return f"<h3 style='color:red;'>❌ Error processing the URL: {str(e)}</h3>", 500

# 🎧 Download the generated audio
@app.route('/download_audio')
def download_audio():
    return send_file('summary.mp3', as_attachment=True)
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    papers = search_agent.search_papers(query=query)
    return render_template('search.html', papers=papers)

@app.route('/summarize_selected', methods=['GET'])
def summarize_selected():
    url = request.args.get('url')
    
    # Fetch the paper using the URL
    paper = fetch_paper_from_url(url)
    
    # Generate summary of the paper
    summarized = summarizer.generate_summary(paper)
    summary = summarized['summary']
    
    # Pass both paper and summary to the result.html template
    return render_template('result.html', summary=summary, paper=paper)


# 🔁 Run the server
if __name__ == '__main__':
    app.run(debug=True)
