from typing import Optional, List

from fastapi import FastAPI, Query

from settings import settings

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/")
async def read_items(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    print(settings.debug)
    return query_items
