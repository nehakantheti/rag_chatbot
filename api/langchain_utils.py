import os
import uuid
import sqlite3
from datetime import datetime
from pprint import pprint
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_history_aware_retriever
from chroma_utils import vectorstore

# Load environment variables
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "default"

output_parser = StrOutputParser()
retriever = vectorstore.as_retriever(search_kwargs={"k":2})
google_llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY"))


contextualise_q_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful and assistive AI."),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

contextualise_chain = contextualise_q_prompt | google_llm | output_parser

qa_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Use the following context to answer."),
    ("system", "Context: {context}"),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

def get_rag_chain(model='gemini-2.0-flash'):
    history_aware_retriever = create_history_aware_retriever(google_llm, retriever, contextualise_q_prompt)
    question_answer_chain = create_stuff_documents_chain(google_llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    return rag_chain