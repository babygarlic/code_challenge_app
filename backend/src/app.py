from fastapi import FastAPI, Request, HTTPException, Response 
from fastapi.middleware.cors import CORSMiddleware
from clerk_backend_api import Clerk 
from .routes import challenge

app = FastAPI()
# CORS middleware to allow requests from the frontend
app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:5173"],  # Adjust this to your frontend's URL in production
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
                   )

app.include_router(challenge.router, prefix="/api")

