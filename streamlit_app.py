from tempfile import TemporaryFile
import streamlit as st
import logging

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

with TemporaryFile(mode="w") as f:
    st.write(f)
    print(f)
    f.write("borp")
    import streamlit as st
    import logging

    log = logging.getLogger("streamlit")

    st.write("Some text of page")

    log.info("Page loaded")
