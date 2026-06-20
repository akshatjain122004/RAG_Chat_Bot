import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
import gradio as gr
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

load_dotenv()

openai_client = OpenAI()

# Vector Embeddings
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

# Load existing collection once at startup
vector_db = QdrantVectorStore.from_existing_collection(
    url=os.getenv("QDRANT_URL", "http://localhost:6333"),
    api_key=os.getenv("QDRANT_API_KEY"),
    collection_name="learning_rag",
    embedding=embedding_model,
)


def respond(message, history):
    search_results = vector_db.similarity_search(query=message)
    context = "\n\n\n".join(
        [
            f"Page Content: {r.page_content}\nPage Number: {r.metadata.get('page_label')}\nFile Location: {r.metadata.get('source')}"
            for r in search_results
        ]
    )

    system_prompt = f"""
You are a helpful AI Assistant who answers user queries based on the available context retrieved from a PDF.
Answer using only the context below and point the user to the relevant page number.

Context:
{context}
"""

    response = openai_client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ],
    )

    try:
        return response.choices[0].message.content
    except Exception:
        return str(response)


app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/", response_class=HTMLResponse)
def index():
    return """<!doctype html><html><head><meta http-equiv='refresh' content='0; url=/chat' /></head><body>Redirecting to <a href='/chat'>/chat</a></body></html>"""


@app.post("/api/chat")
def api_chat(req: ChatRequest):
    reply = respond(req.message, [])
    return {"reply": reply}


demo = gr.ChatInterface(fn=respond, title="PDF Chat", description="Ask questions about the PDF content.")

gr.mount_gradio_app(app, demo, path="/chat")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)
