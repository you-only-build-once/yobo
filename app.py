# app.py
import streamlit as st
from llama_backend import query_model
from streamlit_pdf_viewer import pdf_viewer
import os # Import os for path manipulation
# import streamlit_shadcn_ui as ui # No longer using shadcn for input/button here

def main():
    # Inject Fontshare CSS link and custom styles
    font_css = """
    <link href="https://api.fontshare.com/v2/css?f[]=jet-brains-mono@300,700&display=swap" rel="stylesheet">
    <style>
        /* Apply light weight to general body text and background color */
        body {
            font-family: 'JetBrains Mono', sans-serif !important;
            font-weight: 300 !important;
            background-color: #f0f2f6 !important; /* Light grey background */
        }
        /* Apply bolder weight to the Streamlit title element */
        h1 {
            font-family: 'JetBrains Mono', sans-serif !important;
            font-weight: 700 !important;
        }
        /* You might want to add more specific rules for other elements if needed */
    </style>
    """
    st.markdown(font_css, unsafe_allow_html=True)

    st.title("Your Pet Llama")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            # Ensure chat messages also use the body font settings
            # Or, if you want a different weight for chat, style the specific chat container class
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What would you like to ask Lama Buddy?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # --- Assistant's turn --- 
        # Create a placeholder for the assistant's entire response area
        assistant_response_area = st.empty()

        # Show temporary loading message with video as avatar
        with assistant_response_area.container():
            loading_avatar_col, loading_bubble_col = st.columns([1, 5], gap="small")
            project_root = os.path.dirname(os.path.abspath(__file__))
            video_path = os.path.join(project_root, "assets", "loading_llama.mp4")
            try:
                with open(video_path, "rb") as video_file:
                    video_bytes = video_file.read()
                loading_avatar_col.video(video_bytes, format="video/mp4", start_time=0, end_time=5, loop=True, autoplay=True, muted=True)
            except FileNotFoundError:
                loading_avatar_col.markdown("🦙") # Fallback static avatar if video not found
            
            with loading_bubble_col.container(border=True):
                st.markdown("Lama Buddy is thinking...")
        
        # Get response from model
        response_data = query_model(prompt)
        response = response_data.get("response", "Sorry, I couldn't get a response.")
        pdf_files = response_data.get("files", [])
        
        # Clear the temporary loading message
        assistant_response_area.empty()
        
        # Display final assistant response with static avatar
        with st.chat_message("assistant", avatar="🦙"):
            st.markdown(response)
            
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        if pdf_files:
            with st.chat_message("assistant", avatar="🦙"):
                st.subheader("Source Documents")
                for f in pdf_files:
                    print(f)
                    pdf_viewer(f['file_path'])

if __name__ == "__main__":
    main()
