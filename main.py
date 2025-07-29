from fastapi import FastAPI
from router.router import download_router
app=FastAPI()

@app.get("/ping")
def ping():
    return{"ping":"pong"}

app.include_router(router=download_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7000, log_level="info",
                workers=1, timeout_keep_alive=5)