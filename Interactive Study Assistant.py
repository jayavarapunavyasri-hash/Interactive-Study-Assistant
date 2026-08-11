import streamlit as st
from google import genai

st.set_page_config(
    page_title="Interactive Question Generator",
    page_icon="📝"
)

st.title("📝 Interactive Question Generator")
st.write("Generate questions for any topic using AI.")

# Gemini API
api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

# Topic
topic = st.text_input(
    "Enter the topic:",
    placeholder="Example: Machine Learning"
)

# Number of questions
number = st.number_input(
    "Number of questions:",
    min_value=1,
    max_value=20,
    value=5
)

# Difficulty
difficulty = st.selectbox(
    "Select difficulty:",
    ["Easy", "Medium", "Hard"]
)

# Generate
if st.button("Generate Questions"):

    if not topic:
        st.warning("Please enter a topic.")

    else:
        prompt = f"""
You are an Interactive Question Generator.

Generate {number} questions about:
{topic}

Difficulty level:
{difficulty}

Give clear and educational questions.
Number the questions from 1 to {number}.
Do not provide answers.
"""

        with st.spinner("Generating questions..."):

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

        st.subheader("📚 Generated Questions")
        st.write(response.text)
