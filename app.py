# app.py
import streamlit as st
from llama_backend import query_model
import streamlit_shadcn_ui as ui

def main():
    st.title("Lama Buddy")
    
    # 1. Input box using shadcn UI
    user_input = ui.input(placeholder="Enter your query here:", key="user_input")
    
    # 2. Submit button using shadcn UI
    submit_btn = ui.button(text="Submit", key="submit_btn", variant="default")
    
    # 3. Generate a response when button is clicked
    if submit_btn:
        # Generate response
        out = query_model(user_input)
        
        # 4. Output box
        st.text_area("Response", value=out["response"], height=100)

if __name__ == "__main__":
    main()
