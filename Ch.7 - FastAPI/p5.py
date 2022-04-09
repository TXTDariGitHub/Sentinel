# Path Parameter

from fastapi import FastAPI

app = FastAPI()

@app.get('/number/{rand}')
def show_number(rand : int):
    return {'Your Number':rand}