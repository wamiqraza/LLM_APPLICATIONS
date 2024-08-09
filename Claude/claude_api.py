import streamlit as st
import anthropic
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv('CLAUDE_API_KEY')

# Set up the Anthropic API client
client = anthropic.Anthropic(api_key=api_key)

# Streamlit app
def main():
    st.title("Claude Text Generator")

    # User input
    prompt = st.text_area("Enter your prompt:", height=100)
    
    if st.button("Generate Text"):
        if prompt:
            try:
                # Call the Claude API
                response = client.messages.create(
                    model="claude-3-5-sonnet-20240620",
                    max_tokens=1024,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                
                # Display the generated text
                st.write("Generated Text:")
                st.write(response.content[0].text)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()
