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

    logger = logging.getLogger()
    level = logging.INFO

    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s',
        # handlers=[
        #     logging.StreamHandler(sys.stdout)  # Logs will be output to stderr
        # ]
    )

    logger.log(level, "MOO")