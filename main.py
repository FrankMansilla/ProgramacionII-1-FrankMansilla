from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/ruta")
def ruta():
    return {"bienvenido a la pantalla principal"}

if __name__ == "__main__": 
    uvicorn.run("main:app", port=8000)