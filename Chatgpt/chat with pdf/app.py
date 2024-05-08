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


def main():
    # setup openai key
    # TODO
    st.set_page_config(page_title="Chat with PDF", page_icon=":book")
    st.header("Chat with PDFs ask your questions from your pdf  💬")

    # upload file
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    # extract the text from pdf
    # split into chunks
    # create embeddings
    # show user input


if __name__ == '__main__':
    main()
