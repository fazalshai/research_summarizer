# agents/synthesize_agent.py
class CrossPaperSynthesisAgent:
    def synthesize_summaries(self, papers):
        combined = "\n".join([paper['summary'] for paper in papers])
        return f"Synthesized Summary of {len(papers)} Papers:\n{combined}"
