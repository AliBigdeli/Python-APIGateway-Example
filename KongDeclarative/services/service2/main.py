from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse, HTMLResponse

servers = [
    {"url": "http://127.0.0.1:8000/service2", "description": "Kong Development"},
    {"url": "http://127.0.0.1:9001", "description": "Staging"},    
]

app = FastAPI(
    title="Service 2 API",
    description="Demo FastAPI service behind Kong",
    version="1.0.0",
    servers=servers,
)

# ---- CORS CONFIG ----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # allow all origins
    allow_credentials=True,
    allow_methods=["*"],        # allow all HTTP methods
    allow_headers=["*"],        # allow all headers
)

# ---- Routes ----
@app.get("/hello")
def hello():
    return {"version": "2", "message": "Hello from Service 2!"}



