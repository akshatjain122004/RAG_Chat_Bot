# Implimentation Plan

Goal
- Convert the existing `app.py` into a concise FastAPI application that exposes a minimal Gradio chat UI.
- Provide two endpoints: `/` (main page) and `/api/chat` (JSON chat API).

Constraints
- Keep the code compact and readable; avoid extra features or clutter.
- Do not set or rely on `max_tokens` anywhere.

High-level Steps
1. Create a single-file `app.py` (FastAPI app) that:
   - Loads environment variables and initializes the existing `OpenAI` client and `QdrantVectorStore` as currently done.
   - Implements a `respond(message, history)` function reusing the current logic (similarity search + chat completion).
   - Adds POST `/api/chat` that accepts `{"message": "..."}` and returns `{"reply": "..."}`.
   - Adds GET `/` that returns a tiny HTML redirect or link to `/chat`.

2. Add a minimal Gradio chat interface and mount it on the FastAPI app at `/chat` using `gr.mount_gradio_app(app, demo, path="/chat")` so the UI is reachable.

3. Keep the HTTP handler small: the Gradio UI may call the `/api/chat` endpoint or call `respond` directly — either is fine; calling the local function is simplest and keeps the app self-contained.

4. Run and test with `uvicorn app:app --reload` and verify:
   - GET `/` redirects/links to `/chat`
   - POST `/api/chat` returns a reply string
   - The Gradio page at `/chat` sends/receives messages as expected

Dependencies
- `fastapi`, `uvicorn`, `gradio`, plus any existing libraries used by the current `respond` workflow (e.g., `python-dotenv`, `openai`, `langchain_qdrant`).

Deliverable
- A single, tidy `app.py` replacing the selected file. No other files changed unless you ask.

Next step
- If you confirm, I'll replace `app.py` with the minimal FastAPI + Gradio implementation (concise, readable, no `max_tokens`).
