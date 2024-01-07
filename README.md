# AugmentED: AI Augmented Learning Library - Backend

AugmentED is a digital library/document storage that allows you to use AI for enhanced learning, using features like document chat, semantic search and summarization of concepts into notes.  
Users can upload their own books to the server, and summarize certain sections of them to make notes or search for similar sections in other books.
All documents are stored only on the server and local, private LLMs are used to ensure that sensetive documents are not sent to external APIs. 

AI:
- Vector index querying for pdfs - Using FOSS models for text embeddings
- Custom retrieval for semantic search
- Notemaker using LLMs for summarization
- RAG and ReAct agent for document chat

Backend: 
- conversations endpoint
- semantic search and summarization endpoint
- file uploading and downloading endpoints


## Setup

This project uses FastAPI, llama_index and llama_cpp_python, and it requires Python 3.10+.  
It only supports linux (tested on Fedora 39).

To start the application, navigate to the project folder and execute the command:

python main.py

The application will be available at `http://localhost:5555`.

## Key Features

- Document conversation endpoint that generates a unique, AI-generated response based on the user's question.
- Uploading books to the library
- Making custom notes for topics using AI for summarization

## Running the project:

To run this project, you will need to do the following:  
  
  1. Clone the project repo or download zip and extract it   
   `git clone https://github.com/nusaturn/augmentED-backend`
  2. Create a venv and activate it: `python -m venv augmentED-env` & `source augmentED-env/bin/activate`
  3. Install requirements: `pip install -r requirements.txt`

