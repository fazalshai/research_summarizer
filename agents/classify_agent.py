class TopicClassificationAgent:
    def __init__(self):
        self.topics = ["AI", "Machine Learning", "Healthcare", "Computer Vision", "Robotics"]

    def classify(self, paper):
        text = paper['clean_text'].lower()
        for topic in self.topics:
            if topic.lower() in text:
                paper['topic'] = topic
                break
        else:
            paper['topic'] = "Other"
        return paper
