import whisper
import speech_recognition as sr
import os
import torch
import numpy as np

# M4 GPU Setup
device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"🚀 Processing on: {device.upper()}")

# Load Small Model
print("🧠 Loading Whisper Small...")
model = whisper.load_model("small").to(device)


def listen_and_convert():
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=16000) as source:  # 16kHz lock kiya
        print("\n🎤 Background noise check... (1 second khamoshi)")
        r.adjust_for_ambient_noise(source, duration=1)

        print("🎤 Ma khpal awaz rora (Ab bolien...)")
        try:
            # phrase_time_limit lagaya taake audio bohot lambi na ho jaye
            audio = r.listen(source, timeout=10, phrase_time_limit=5)

            # Temporary WAV file save karna
            with open("temp_audio.wav", "wb") as f:
                f.write(audio.get_wav_data())

            print("🧠 AI Analyzing...")
            # 'initial_prompt' AI ko ishara dega ke hum Pashto bol rahe hain
            result = model.transcribe(
                "temp_audio.wav",
                language="ps",
                fp16=False,
                initial_prompt="دا پښتو ژبه ده، پښتونولي، احمد شاه بابا"
            )

            final_text = result['text'].strip()
            print("-" * 30)
            print(f"✅ AI ne Samjha: {final_text}")
            print("-" * 30)

        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            if os.path.exists("temp_audio.wav"):
                os.remove("temp_audio.wav")


if __name__ == "__main__":
    listen_and_convert()