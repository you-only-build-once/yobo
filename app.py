# app.py
import streamlit as st

def main():
    st.title("Simple Streamlit Demo")
    
    # 1. Input box
    user_input = st.text_input("Enter your query here:")
    
    # 2. Submit button
    if st.button("Submit"):
        # 3. Generate a response (echoing back for this demo)
        response = f"You entered: {user_input}"
        
        # 4. Output box
        st.text_area("Response", value=response, height=100)

if __name__ == "__main__":
    main()
