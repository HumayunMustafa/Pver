"""
Created By Humayun Mustafa on 29 Januray 2026
This program is yet another fun project to help me read specific protions 
of the documents without ever caring to find or scroll them.
For this purpose LLM with RAG is used
"""
import argparse
from src.embeddings import create_chunks

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF Retrieval with RAG")
    parser.add_argument(
        "--doc_path",
        type=str,
        required=True,
        help="Path to the PDF document to process"
    )
    args = parser.parse_args()
    
    chunks = create_chunks(args.doc_path)
    print(f"type of chunks is {type(chunks)}")