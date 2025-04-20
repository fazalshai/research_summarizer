import google.generativeai as genai

# Configure with your key
genai.configure(api_key="AIzaSyDo34CgnUM1BGN9_Mo2TM-VTCRx698p5q4")

class SummaryGenerationAgent:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def generate_summary(self, paper):
        print(f"Summarizing: {paper['title']}")
        prompt = f"Summarize this academic paper in simple terms:\n\n{paper['clean_text'][:3000]}"

        try:
            response = self.model.generate_content(prompt)
            paper['summary'] = response.text
        except Exception as e:
            paper['summary'] = f"[Gemini Error] {e}"
            print(f"⚠️ Gemini Exception: {e}")
        return paper
