from fastapi import FastAPI
from controllers import auth, books

app = FastAPI()

app.include_router(auth.router)
app.include_router(books.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)