# Import Streamlit library for building interactive web apps
import streamlit as st

# Import message types from langchain_core.messages
# - HumanMessage: represents user input
# - AIMessage: represents AI output
# - SystemMessage: (not used here, but available for system instructions)
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Set the title of the Streamlit app
st.title("Chatbot")

# Initialize chat history in Streamlit's session state
# - session_state persists data across reruns of the app
# - This ensures chat history is not lost when the page updates
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages from history on app rerun
# - This loop goes through all messages stored in session_state
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        # If the message is from the user, display it in a user chat bubble
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        # If the message is from the assistant/AI, display it in an assistant chat bubble
        with st.chat_message("assistant"):
            st.markdown(message.content)
            
# Create a chat input bar where the user can type messages
# - Placeholder text is "How are you?"
prompt = st.chat_input("How are you?")

# Check if the user submitted a message
if prompt:

    # Display the user's message immediately in a user chat bubble
    with st.chat_message("user"):
        st.markdown(prompt)

        # Add the user's message to the session_state for history
        st.session_state.messages.append(HumanMessage(prompt))

    # Create a simple echo response (just repeats what the user typed)
    response = f"Echo: {prompt}"

    # Display the AI/assistant's response in a chat bubble
    with st.chat_message("assistant"):
        st.markdown(response)

        # Add the assistant's response to session_state for history
        st.session_state.messages.append(AIMessage(response))
