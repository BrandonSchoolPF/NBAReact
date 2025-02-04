'''FastAPI Entry Point'''
from fastapi import FastAPI
import uvicorn
from routers.routes import nba_router

app = FastAPI()

app.include_router(nba_router)

@app.get("/")
def read_root():
    return {"message": "Route Endpoint of NBA API"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)