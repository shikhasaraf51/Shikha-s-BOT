import streamlit as st
import openai

# Initialize the OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Function to interact with the GPT model
def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or use 'gpt-4' if you have access
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {e}"

# Streamlit app setup
st.title("GPT Chat Interface")

# Input from the user
user_input = st.text_input("Enter your message:")

if st.button("Send") and user_input:
    # Generate response
    output = generate_response(user_input)
    st.text_area("Response from GPT:", value=output, height=200)

st.sidebar.header("About")
st.sidebar.write("This is a simple chat interface using Streamlit and OpenAI's GPT API.")

# Reminder to replace API key
st.sidebar.warning("Ensure to replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key.")
