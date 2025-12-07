import streamlit as st
import os
import openai
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY"," ")
grok_api_key = os.getenv("MY_KEY_GROQ")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT_V2"," ")

## PROMPT TEMPLATE

prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant please response to the user query"),
    ("user","question:{question}")
])

def generate_response(question,api_key,llm,temperature,max_tokens):  ## temprature means creative or not : range(0,1).
    openai.api_key = api_key
    llm = ChatOpenAI(model=llm)
    outputparser = StrOutputParser()
    chain = prompt | llm | outputparser
    response = chain.invoke({"question":question})
    return response

## TITLE OF THE APP
st.title("Enhanced Q&A Chatbot with openai")

## sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your openai key:",type="password")

## drop down to select various open ai models
model = st.sidebar.selectbox("Select an OpenAI Model",["gpt-4o","gpt-4-turbo","gpt-4"])

## Adjusting the response parameter

temperature = st.sidebar.slider("Temprature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)


## main interface for user input

st.write("GO ahead and ask any question")
user_input = st.text_input("YOU:")

if user_input and api_key:
    response= generate_response(user_input,api_key,model,temperature,max_tokens)
    st.write(response)
elif user_input:
    st.write("Please enter the openai api key:")
else:
    st.write("Please provide the query:")


