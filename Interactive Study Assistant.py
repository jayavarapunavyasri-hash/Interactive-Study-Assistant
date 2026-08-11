import streamlit as st
from google import genai

st.set_page_config(
    page_title="Interactive Study Assistant",
    page_icon="📚"
)

st.title("📚 Interactive Study Assistant")
st.write("Ask questions and learn with an AI study assistant.")

# Gemini API
api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

# Topic
topic = st.text_input(
    "Enter the topic you want to study:",
    placeholder="Example: Machine Learning"
)

# Question
question = st.text_area(
    "Ask your question:",
    placeholder="Example: What is supervised learning?"
)

# Button
if st.button("Get Answer"):

    if not topic:
        st.warning("Please enter a topic.")

    elif not question:
        st.warning("Please enter a question.")

    else:

        prompt = f"""
You are an Interactive Study Assistant.

The student is studying: {topic}

Answer the student's question in a simple
and easy-to-understand way.

Give examples when useful.
Explain step by step when necessary.

Student's question:
{question}
"""

        with st.spinner("Generating answer..."):

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

        st.subheader("🤖 Assistant")
        st.write(response.text)
