import streamlit as st
from question import ask_question
from generate import getModelTokenizer
from htmlTemplates import css, bot_template, user_template

st.set_page_config(
    page_title="OSTIM Question-Answering ChatBot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto"
)
st.write(css, unsafe_allow_html=True)

if "lang" not in st.session_state:
    st.session_state.lang = None

if st.session_state.lang is None:
    lang = st.selectbox("Select Language", ("", "en", "tr"), index=0)
    print(lang)
    if lang:
        st.session_state.lang = lang
        st.session_state.model, st.session_state.tokenizer = getModelTokenizer(lang)
        st.rerun()
text_lang = ""
no_answer_text = ""
processing_text = ""

if st.session_state.lang:
    if st.session_state.lang == 'en':
        st.header("OSTIM Question-Answering ChatBot :robot_face:")
        text_lang = "Please Write Your Question:"
        no_answer_text = "I'm sorry, I don't have an answer for that question at the moment."
        processing_text = "Processing..."
    elif st.session_state.lang == 'tr':
        st.header("OSTİM Soru-Cevaplama ChatBot'u :robot_face:")
        text_lang = "Lütfen Soracağınız Soruyu Yazınız:"
        no_answer_text = "Üzgünüm, şu anda bu soruya verecek bir cevabım yok."
        processing_text = "İşleniyor..."

    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    with st.form(key="user_input_form"):
        user_input = st.text_input(text_lang)
        bot_reply = no_answer_text
        submit_button = st.form_submit_button(label="Send")
        if submit_button and user_input:
            st.session_state.conversation.append(("User", user_input))
            question = "[Q] " + user_input + "\n"
            with st.spinner(processing_text):
                bot_reply = ask_question(
                    question, 
                    max_new_tokens=200, 
                    temperature=0.8, 
                    top_k=50, 
                    top_p=0.95, 
                    model=st.session_state.model, 
                    tokenizer=st.session_state.tokenizer
                )
            st.session_state.conversation.append(("Bot", bot_reply))
            user_input = ""

    conversation_reversed = st.session_state.conversation[::-1]
    for sender, message in conversation_reversed:
        if sender == "User":
            st.write(user_template.replace("{{MSG}}", message), unsafe_allow_html=True)
        elif sender == "Bot":
            st.write(bot_template.replace("{{MSG}}", message), unsafe_allow_html=True)