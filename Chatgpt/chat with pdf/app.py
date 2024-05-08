# import libraries
from dotenv import load_dotenv
import streamlit as st
from PyPDF import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import faiss
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

# main function
# setup openai key
# upload file
# extract the text from pdf
# split into chunks
# create embeddings
# show user input
