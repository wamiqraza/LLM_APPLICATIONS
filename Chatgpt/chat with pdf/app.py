# import libraries
from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
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

    # extract the text
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
            else:
                st.warning("No text found in one or more pages.")
                return

        if not text:
            st.warning("No text could be extracted from the PDF.")
            return

        # split into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
        if not chunks:
            st.warning("Failed to create text chunks from the PDF.")
            return

        # create embeddings
        embeddings = OpenAIEmbeddings()
        if embeddings:
            try:
                knowledge_base = FAISS.from_texts(chunks, embeddings)
            except Exception as e:
                st.error(f"Error creating knowledge base: {str(e)}")
                return
        else:
            st.error("Failed to load embeddings model.")
            return
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # show user input
        user_question = st.text_input("Ask a question about your PDF:")
        if user_question:
            docs = knowledge_base.similarity_search(user_question)

            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs,
                                     question=user_question)
                print(cb)

            st.write(response)


if __name__ == '__main__':
    main()
