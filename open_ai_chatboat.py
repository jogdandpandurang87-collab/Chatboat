from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv


load_dotenv()

# Set environment variables correctly
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")
os.environ['LANGCHAIN_TRACING_V2'] = "true"


# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user’s queries."),
    ("user", "Question: {question}")
])

st.title('AI Chat Assistant')
inpt_text = st.text_input('Search the topic you want')

# LLM
llm = ChatOpenAI(model='gpt-4o-mini')   # use updated model name
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if inpt_text:
    st.write(chain.invoke({'question': inpt_text}))


