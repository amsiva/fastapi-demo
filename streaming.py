from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

from fastapi.responses import StreamingResponse


app = FastAPI()

class PromptRequest(BaseModel):
    message: str



client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def stream_response(message:str):
    stream = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages =  [{"role":"user", "content":message}],
        stream=True)
    
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            yield content




@app.post("/generate_stream")

def generate_prompt(request: PromptRequest):
    return StreamingResponse(stream_response(request.message), media_type = 'text/plain')



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("streaming:app", host="localhost", port=8000, reload=True)
