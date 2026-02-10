# Import the Streamlit library and give it the alias 'st'
# Streamlit is used to create interactive web apps easily with Python
import streamlit as st

# Create a chat input widget in the Streamlit app
# - This displays an input box at the bottom of the app
# - The placeholder text says "Say something"
# - When the user types something and presses Enter, the input is stored in 'prompt'
prompt = st.chat_input("Say something")

# Check if the user has provided input (i.e., 'prompt' is not empty)
if prompt:
    # Display the user's message in the chat interface
    # - st.chat_message("user") creates a chat bubble for the user
    # - st.markdown(prompt) displays the actual text inside the bubble
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display the assistant's response in the chat interface
    # - st.chat_message("assistant") creates a chat bubble for the assistant
    # - st.markdown(f"You said: {prompt}") echoes back what the user typed
    #   Here, it’s just a simple demonstration; no AI model is called
    with st.chat_message("assistant"):
        st.markdown(f"You said: {prompt}")
