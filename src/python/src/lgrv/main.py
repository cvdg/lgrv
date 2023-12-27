from fastapi import FastAPI

app = FastAPI()

from .projectname import generate, search, names


@app.get("/health")
async def health() -> str:
    """Check if the API is up and running"""
    return {"Status": "OK"}


@app.get("/projectnames/{code:str}")
async def projectnames(code: str):
    regex = search(code)
    projectnames = names(regex)

    return {"code": code, "names": projectnames}


@app.get("/projectnames/")
async def projectnames():
    projectnames = None

    while not projectnames:
        code = generate()
        regex = search(code)
        projectnames = names(regex)

    return {"code": code, "names": projectnames}
