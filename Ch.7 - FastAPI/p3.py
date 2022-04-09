from fastapi import FastAPI

app = FastAPI()

# @app.operation(path)
@app.get('/register')
"""
Index function will perform with this path and this operation
"""
# path operation function
def index():
    return "Welcome to Registration Page !"