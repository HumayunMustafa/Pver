"""
Created By Humayun Mustafa on 29 Januray 2026
This program is yet another fun project to help me read specific protions 
of the documents without ever caring to find or scroll them.
For this purpose LLM with RAG is used
"""
import argparse
from src.embeddings import get_or_create_vectorstore
import traceback
from src.chat import create_chain
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# This fucntion not in use for now
def exception_handle(function_name : str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                traceback.print_exc()
                print(f"Error Occured in {function_name}\n: {e}")
        return wrapper
    return decorator

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF Retrieval with RAG")
    parser.add_argument(
        "--doc_path",
        type=str,
        required=True,
        help="Path to the PDF document to process"
    )
    parser.add_argument(
        "--recreate",
        action="store_true",
        help="Force recreate the vectorstore even if it exists"
    )
    args = parser.parse_args()
    
    # Load or create vectorstore (cached on disk)
    vectorstore = get_or_create_vectorstore(args.doc_path, force_recreate=args.recreate)
    rtvr = vectorstore.as_retriever(search_kwargs={"k":4})
    q_chain = create_chain(rtvr)
    print()
    while True:
        print()
        print("Press q to exit")
        print()
        a = input("Alright ask question related to pdf you shared\n")
        if a == "q":
            break
        res = q_chain.invoke(a)
        print("*"*30)
        print("LLM Result: ")
        print(f"{res.get('result')}")
        print("*"*30)
        print()