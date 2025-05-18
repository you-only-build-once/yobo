# app.py
import streamlit as st
from llama_backend import query_model
# import streamlit_shadcn_ui as ui # No longer using shadcn for input/button here

def main():
    st.title("Lama Buddy Chat")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What would you like to ask Lama Buddy?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            with st.spinner("Lama Buddy is thinking..."):
                response_data = query_model(prompt)
                response = response_data.get("response", "Sorry, I couldn't get a response.")
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
