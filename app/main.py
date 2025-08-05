from fastapi import FastAPI
from .router import questions, form

app = FastAPI()

app.include_router(form.router)
app.include_router(questions.router)
