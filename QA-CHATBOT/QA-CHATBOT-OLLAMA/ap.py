## models i have : gemma:2b ,gemma3:1b, llama3.2:1b

from langchain_core.prompts import ChatPromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
## setup of env
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "QNA WITH OLLAMA "
os.environ["LANGCHAIN_TRACING_V2"] = "true"

## prompt

prompt = ChatPromptTemplate.from_messages([
    ("system","You have to answer all the question which is asked by the user "),
    ("user","question:{question}")
])

# llm = Ollama(model="gemma:2b")
output_parser = StrOutputParser()
# chain = prompt | llm | output_parser

def get_response(question,llm,temperature,max_tokens):
    llm = Ollama(model=llm)
    chain = prompt | llm | output_parser
    return chain.invoke({"question":question},
                        options={
                            "temperature":temperature,
                            "num_predict":max_tokens
                        })

st.title("Enhanced Q&A with open source models using ollama")

st.sidebar.title("Settings:")

model = st.sidebar.selectbox("select which model do you want to use:",["gemma:2b","gemma3:1b","llama3.2:1b"])
temp = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_token = st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)

st.write("Ask Anything :")

input_text = st.text_input("You:")

if input_text and model:
    response = get_response(input_text,model,temp,max_token)
    st.write(response)
elif input_text:
    st.write("Select the model first: ")



