import os
from faster_whisper import WhisperModel

# Aapne jo links bheje un mein se Video IDs
video_ids = [
    'KD3wu9lgMe0',
    'gOtfTIVMMpA',
    'gEg-52xMtkg',
    'bs2-4LsNBG0'
]


def download_and_transcribe():
    # Folder banayein data ke liye
    os.makedirs("../src/data/youtube_text", exist_ok=True)

    # M4 ke liye Whisper Model setup (Small is best for Pashto)
    print("Loading Private Whisper Model on your Mac...")
    model = WhisperModel("small", device="cpu", compute_type="int8")

    for vid in video_ids:
        url = f"https://www.youtube.com/watch?v={vid}"
        print(f"\nProcessing Video: {url}")

        # 1. Download Audio Locally
        # 1. Download Audio Locally (More robust command)
        os.system(f'yt-dlp -x --audio-format wav --ffmpeg-location /opt/homebrew/bin/ffmpeg -o "temp.wav" {url}')

        # 2. Convert Audio to Pashto Text
        print("Transcribing... (Working offline on your M4)")
        segments, _ = model.transcribe("temp.wav", language="ps")

        # 3. Save to file
        with open("../src/data/youtube_text/pashto_chat.txt", "a", encoding="utf-8") as f:
            for segment in segments:
                f.write(segment.text + "\n")

        # Safayi (temp file delete)
        if os.path.exists("../temp.wav"):
            os.remove("../temp.wav")

    print("\n--- MUBARAK! Sara Data 'data/youtube_text/pashto_chat.txt' mein save ho gaya hai ---")


if __name__ == "__main__":
    download_and_transcribe()