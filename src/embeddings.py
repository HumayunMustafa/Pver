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
import os

def create_chunks(doc_path : str = "documents.pdf") -> any:
    loader = PyPDFLoader(doc_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )  
    chunks = text_splitter.split_documents(documents)
    return chunks


def create_embeddings(chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore


def get_or_create_vectorstore(doc_path: str, force_recreate: bool = False):
    doc_name = os.path.splitext(os.path.basename(doc_path))[0]
    vectorstore_path = f"vectorstore_{doc_name}"
    
    embeddings = OpenAIEmbeddings()
    if os.path.exists(vectorstore_path) and not force_recreate:
        print(f"Loading existing vectorstore from {vectorstore_path}...")
        vectorstore = FAISS.load_local(vectorstore_path, embeddings, allow_dangerous_deserialization=True)
        print("Vectorstore loaded successfully!")
    else:
        print("Creating new vectorstore (this may take a moment)...")
        chunks = create_chunks(doc_path)
        vectorstore = create_embeddings(chunks)
        vectorstore.save_local(vectorstore_path)
        print(f"Vectorstore created and saved to {vectorstore_path}")
    
    return vectorstore