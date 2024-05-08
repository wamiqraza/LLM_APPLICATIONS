# import libraries
from dotenv import load_dotenv
import streamlit as st
from PyPDF import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with PDF", page_icon=":book")
    st.header("Chat with PDFs ask your questions from your pdf  💬")

    # upload file
    pdf = st.file_uploader("Upload your PDF", type="pdf")

    # extract the text from pdf
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

    # split into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # create embeddings
    embeddings = get_openai_callback()
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    # show user input
    


if __name__ == '__main__':
    main()
