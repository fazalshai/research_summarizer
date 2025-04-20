from agents.search_agent import PaperSearchAgent
from agents.process_agent import PaperProcessingAgent
from agents.classify_agent import TopicClassificationAgent
from agents.summarize_agent import SummaryGenerationAgent
from agents.synthesize_agent import CrossPaperSynthesisAgent
from agents.audio_agent import AudioGenerationAgent

def main():
    print("\n🎯 Research Paper Summarization Multi-Agent System Starting...\n")

    # Initialize agents
    search_agent = PaperSearchAgent()
    process_agent = PaperProcessingAgent()
    classify_agent = TopicClassificationAgent()
    summarize_agent = SummaryGenerationAgent()
    synthesize_agent = CrossPaperSynthesisAgent()
    audio_agent = AudioGenerationAgent()

    # Simulate search
    papers = search_agent.search_papers("Artificial Intelligence in Healthcare")

    # Process papers
    processed = [process_agent.process(p) for p in papers]     

    # Classify
    classified = [classify_agent.classify(p) for p in processed]

    # Summarize
    summaries = [summarize_agent.generate_summary(p) for p in classified]

    # Synthesize
    full_summary = synthesize_agent.synthesize_summaries(summaries)

    # Generate audio
    audio_agent.generate_audio(full_summary)

    print("\n✅ Done! Audio summary generated as 'summary.mp3'\n")

if __name__ == "__main__":
    main()
