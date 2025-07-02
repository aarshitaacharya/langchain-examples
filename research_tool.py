from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

# Load the API key
google_api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the model
model = ChatGoogleGenerativeAI(google_api_key=google_api_key,
                               model="gemini-2.0-flash")

st.header('Research Tool')

# static prompting

# user_input = st.text_input("Enter your prompt")

# if st.button('Summarize'):
#     if user_input.strip():
#         result = model.invoke(user_input)
#         st.markdown(result.content)
#     else:
#         st.warning("Please enter a prompt.")

#dynamic prompting:

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    st.write(result.content)

