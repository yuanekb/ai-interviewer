import os

from dotenv import load_dotenv
import openai
import PyPDF2
import streamlit as st

# Example config.env: 
# OPENAI_API_KEY=your_api_key_here

load_dotenv('config.env')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

st.title('AI Interviewer App')
resume_file = st.file_uploader('Please upload your resume (PDF)', type='pdf')