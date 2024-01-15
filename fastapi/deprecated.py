from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(version="0.0.0", title="Teste", summary="um teste", description="Usado para testar")

@app.get('/item', response_class=JSONResponse, deprecated=True)
def item():
    return {"item": {"id": 1, "produto": "notebook"}}


@app.get('/itens', response_class=JSONResponse)
def item():
    return {"itens": [
        {"id": 1, "produto": "notebook"},
        {"id": 2, "produto": "notebook"},
    ]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)