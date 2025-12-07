import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


## LANGSMITH TRACKING 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")



## desiging of prompt template

template = ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant that helps what people ask you."),
    ("user","question:{question}")
])

## ollama model
llm = Ollama(model="gemma:2b")

chain = template | llm | StrOutputParser()
st.title("Chat with ollama llms")
input = st.text_input("Ask something whatever you have in mind")

if st.button("Submit"):
    response = chain.invoke({"question":input})
    st.write(response)
