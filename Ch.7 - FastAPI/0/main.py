# Import Package
from fastapi import FastAPI

# Defining Package
app = FastAPI()

# Using get method
@app.get('/')
# Create root function
async def root():
    return {"message":"Hello World !"}