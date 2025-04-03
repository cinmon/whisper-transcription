# whisper-transcrption

A Streamlit App that uses OpenAI's Whisper (small) to transcribe video (mp4, webm) or audio (mp3, m4a, wav) into text (only files under 200 MB).

## Current Features

- Choose the original language manually, or let Whisper auto-detect it.
- Download the transcription as a `.txt` file.

## Libraries

The libraries used are:
- `streamlit`
- `torch`
- `torchaudio`
- `openai-whisper`
- `ffmpeg-python` 

`package.txt` contains system-level dependencies. In this case, it only contains `ffmpeg`, so this file is telling Streamlit to install `ffmpeg` on the server at runtime.

## To-Do List

- Format the output for better readability (e.g., punctuation, speaker turns).
- Add a button to copy the transcription to the clipboard.
- Add the option to download the transcription as a `.pdf`.