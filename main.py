from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from router.downloadrouter import download_router

app=FastAPI()
template=Jinja2Templates(directory="static")
@app.get("/",response_class=HTMLResponse)
def home(request:Request):
    return template.TemplateResponse("index.html", {"request": request, "message": "Hello, World!"})

app.include_router(router=download_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7000, log_level="info",
                workers=1, timeout_keep_alive=5)