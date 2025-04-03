import streamlit as st
from transcribe import transcribe

st.set_page_config(page_title="Audio/Video Transcriber", layout="centered")

st.title("Whisper Transcription")

uploaded_file = st.file_uploader("Upload an audio or video file", type=["mp3", "mp4", "m4a", "wav", "webm"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/mp3")
    with st.spinner("Transcribing... this may take a few seconds depending on the file size"):
        transcription = transcribe(uploaded_file)
    st.success("Transcription complete!")
    st.markdown("### 📝 Transcription:")
    st.text_area("Transcript", transcription, height=300)
