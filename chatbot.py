import streamlit as st
from streamlit import session_state
from streamlit_chat import message
from utils import get_initial_message, get_chatgpt_response, update_chat
import os
from dotenv import load_dotenv
import time
import openai
from openai import OpenAI

# load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = "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"
# rint(openai.api_key)

# client = OpenAI(api_key="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")

st.title("Chatbot for Manufacturing: Using ChatGPT and Streamlit")
st.subheader("AI Customer Assistant: ")


model = st.selectbox(
    "Select a model",
    (
        "gpt-3.5-turbo",
        "gpt-4",
        "ft:gpt-3.5-turbo-0125:personal::99yL0Uit",
    ),  # Here we will use our fine tuned model as a selection
)

if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []  # we store our chat history


query = st.text_input("Query: ", key="input")  # what our user asks as a query

if "messages" not in st.session_state:
    st.session_state["messages"] = (
        get_initial_message()
    )  # stores all the messages for chatgpt and maintains the prompt history

if query:
    with st.spinner("generating..."):
        messages = st.session_state["messages"]  # take all the messages
        messages = update_chat(messages, "user", query)
        response = get_chatgpt_response(messages, model)
        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(query)  # update for the user on the UI
        st.session_state.generated.append(response)  # update for the bot on the UI

if st.session_state["generated"]:
    for i in range(
        len(st.session_state["generated"]) - 1, -1, -1
    ):  # go backwards and head ot the 0th index
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
        message(st.session_state["generated"][i], key=str(i) + "_assistant")

with st.expander("Show Messages"):
    st.write(st.session_state["messages"])
