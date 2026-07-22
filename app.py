import os

import streamlit as st
from dotenv import load_dotenv
from google import genai


# Load environment variables from the .env file
load_dotenv()

# Configure the Streamlit page before displaying other UI elements
st.set_page_config(
    page_title="Gemini LLM App",
    page_icon="🤖",
    layout="centered",
)

st.header("Gemini LLM Application 🤖")
st.write("Enter a question and receive a response from Google Gemini.")

# Read the API key securely
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error(
        "Gemini API key was not found. "
        "Add GEMINI_API_KEY to your .env file."
    )
    st.stop()

# Create the Gemini client
client = genai.Client(api_key=api_key)


def get_gemini_response(question: str) -> str:
    """Send a question to Gemini and return its text response."""
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=question,
    )

    return response.text or "Gemini did not return a text response."


user_input = st.text_area(
    "Input:",
    placeholder="Enter your question here...",
    height=120,
)

submit = st.button(
    "Submit",
    type="primary",
    disabled=not user_input.strip(),
)

if submit:
    try:
        with st.spinner("Generating response..."):
            response_text = get_gemini_response(user_input.strip())

        st.subheader("Response from Gemini")
        st.write(response_text)

    except Exception as error:
        st.error(f"Unable to generate a response: {error}")