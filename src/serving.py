from fastapi import FastAPI
from pydantic import BaseModel
from chat import create_chain

app = FastAPI()
qa_chain  = create_chain()

class QuestionRequest(BaseModel):
    question : str

@app.post("/ask")
def ask_question(req: QuestionRequest):
    result = qa_chain.run(req.question)
    return {"answer": result}