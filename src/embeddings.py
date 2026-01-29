"""
Created By Humayun Mustafa on 29 Januray 2026
This program is yet another fun project to help me read specific protions 
of the documents without ever caring to find or scroll them.
For this purpose LLM with RAG is used
"""

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS  

def create_chunks(doc_path : str = "documents.pdf") -> any:
    loader = PyPDFLoader(doc_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )  
    chunks = text_splitter.split_documents(documents)


def create_embeddings(chunks):
    pass