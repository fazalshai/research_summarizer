class PaperProcessingAgent:
    def process(self, paper):
        print(f"🧪 Processing: {paper['title']}")
        paper['clean_text'] = paper['text'].strip()
        return paper
