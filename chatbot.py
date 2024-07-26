import streamlit as st

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''
st.link_button("Homepage", "https://google.com")
st.markdown(hide_img_fs, unsafe_allow_html=True)
st.image('viralistlogo.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
         output_format="auto")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

prompt = st.chat_input("How can I assist you today?")

if prompt:
    with st.chat_message("user", avatar="bear.png"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f'Echo: {prompt}'

    with st.chat_message("assistant", avatar='rabbit.png'):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
