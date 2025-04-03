import whisper
import tempfile
import os

model = whisper.load_model("base")  # can be "small", "medium", "large"

def transcribe(file):

    # create temporary file
    # because whisper expects a file path
    # (need to temporarily save it)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_audio.write(file.read())
        temp_audio_path = temp_audio.name

    result = model.transcribe(temp_audio_path)

    os.remove(temp_audio_path)

    return result["text"]
