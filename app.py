import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Barry's Space", page_icon=":bowtie:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_yMpiqXia1k.json")
img_contact_form = Image.open("images/phonebox.png")
img_lottie = Image.open("images/willie.png")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I'm Barry :wave:")
    st.title("I love whisky, women and willies")
    st.write(
        "This is me pissing about and showing how smart I am."
    )
    st.write("[Learn More >](https://Barryisking.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my IG I share pics of:
            - Whisky,
            - Women, and
            - Willy waving
            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any pics.
            """
        )
        st.write("[Instagram >](https://youtube.com/c/Barryisking)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Videos")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie)
    with text_column:
        st.subheader("Willie shouts...")
        st.write(
            """
            Willie says EEL IS A CUNT!!!!!
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/i2q0T7QXETs)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Soho Phone Box")
        st.write(
            """
            Want to see a woman shit in a Phone Box?
            In this video, we see a woman shit in a Phone Box. Dirty Cunt!
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/rNM-hFXwVCA)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/1982lukejones@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()