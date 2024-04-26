
from fastapi import FASTAPI
app = FASTAPI()

@app.get('/', tags=["Root"])
async def hello():
    return {"hello":"sucess"}
