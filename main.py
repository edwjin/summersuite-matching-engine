from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import supabase

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "SummerSuite backend is running"}

@app.get("/profiles")
def get_profiles():
    response = supabase.table("public_profiles").select("*").execute()
    return response.data