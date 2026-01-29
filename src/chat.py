from langchain_openai import ChatOpenAI
from langchain_classic.chains import RetrievalQA
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    temperature=0,
    model="gpt-4o-mini"
)
def create_chain(retriever):
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, 
        retriever=retriever,
        return_source_documents=False
    )
    return qa_chain