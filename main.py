from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data from file
with open("q-vercel-python.json", "r") as f:
    students_data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = []):
    marks_dict = {student["name"]: student["marks"] for student in students_data}
    result = [marks_dict.get(n, None) for n in name]
    return {"marks": result}