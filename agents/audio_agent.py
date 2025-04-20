from gtts import gTTS

class AudioGenerationAgent:
    def generate_audio(self, text):
        print("🔊 Generating audio...")
        tts = gTTS(text)
        tts.save("summary.mp3")
