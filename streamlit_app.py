from tempfile import TemporaryFile
import streamlit as st


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

with TemporaryFile() as f:
    f.write("Boop")
