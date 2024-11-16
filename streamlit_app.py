from tempfile import TemporaryFile
import streamlit as st
import logging
import sys

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

with TemporaryFile(mode="w") as f:
    st.write(f)
    print(f)
    f.write("borp")

    # log = logging.getLogger("Flowco")


    # st.write("Some text of page")
    # log.setLevel(logging.INFO)
    # log.info("Page loaded")

    logger = logging.getLogger("streamlit")
    level = logging.INFO

    handler = logging.StreamHandler()

    # Define a custom formatter
    formatter = logging.Formatter(
        fmt='%(message)s'
    )

    # Set the formatter to the handler
    handler.setFormatter(formatter)

    logger.log(level, "MOO")