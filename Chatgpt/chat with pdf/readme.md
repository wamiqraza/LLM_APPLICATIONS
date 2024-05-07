# Chat with PDF using Langchain


This is a Python program that lets you open a PDF file and use natural language to ask questions about it. A LLM is used by the app to make a comment about your PDF. The LLM won't answer questions that aren't about the paper.

## How it works

The app reads the PDF and breaks up the text into smaller pieces that can be put into an LLM. OpenAI embeddings are used to turn the chunks into vector models. The app then finds chunks that are semantically related to the user's question and sends them to the LLM so that it can come up with an answer.

For the GUI, the app uses Streamlit, and for the LLM, it uses Langchain.


## Installation

Clone this repository and install the requirements:

```
pip install -r requirements.txt
```

You will also need to create a `.env` file and then add your OpenAI API key to the `.env` file.

## Usage

To use the application, run the `app.py` file with the streamlit CLI:
```
streamlit run app.py
```


## Contributing

For instructional purposes only, this repository is not intended to receive any additional contributions; it is just for educational purposes. It is intended to serve as supplementary content for the YouTube lesson that demonstrates how to construct the project.
