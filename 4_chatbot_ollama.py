import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

st.title("Chatbot")

# Initialize chat history and add SystemMessage if first run
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(SystemMessage("Act like an astronaut"))

# Display chat history
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# Chat input bar
prompt = st.chat_input("Type your message…")

if prompt:
    # Display user message immediately
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append(HumanMessage(prompt))

    # Call Llama model safely
    llm = ChatOllama(model="llama3.2:1b", temperature=0.5)  # lower temp for stability

    try:
        # Show spinner while AI is processing
        with st.spinner("AI is typing…"):
            result = llm.invoke(st.session_state.messages).content

        # Display AI response
        with st.chat_message("assistant"):
            st.markdown(result)
            st.session_state.messages.append(AIMessage(result))

    except Exception as e:
        # If anything goes wrong, show error instead of blank
        st.error(f"Error from Llama: {e}")
