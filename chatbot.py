import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key='-')
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''
st.link_button("Homepage", "https://google.com")
st.markdown(hide_img_fs, unsafe_allow_html=True)
st.image('virallogo.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
         output_format="auto")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

prompt = st.chat_input("How can I assist you today?")
st.markdown("Model is turned off right now, contact developer for more details, contacts are on the homepage.")

# Original prompt and parts of code are stored securely, contact developer for more details

# if prompt:
#   with st.chat_message("user", avatar="bear.png"):
#      st.markdown(prompt)
# st.session_state.messages.append({"role": "user", "content": prompt, "avatar": "bear.png"})
#
#   prompt = "Respond as a qualified social media instructor. User will give you a prompt in a specific format. Format: social network / name of the post / ideas (user can specify or you can generate yourself). User should give information about first 2 cells, if not ask him to do so. Do not respond in this format yourself. You should generate ideas for the third part yourself, based on what user gave you. Your job is to generate description for a post, so it would get viral. Include important hashtags. Don't add additional information. Din't add headings. Don't forget to add necessary spacing and new lines. Here is users request: " + prompt
#  response = model.generate_content(prompt)
# response = response.text
#
#   with st.chat_message("assistant", avatar='rabbit.png'):
#      st.markdown(response)
#
#   st.session_state.messages.append({"role": "assistant", "content": response, "avatar": "rabbit.png"})
