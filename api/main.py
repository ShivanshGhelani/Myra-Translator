from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import importlib.util
import sys
import os
import logging

# Dynamically import the router based on current environment (local vs Vercel)
if os.path.exists("routes/translation_routes.py"):
    sys.path.insert(0, ".")
    from routes.translation_routes import router
else:
    # When deployed on Vercel
    from .routes import router

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("pygame").setLevel(logging.WARNING)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

# Mount static directories
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/SVG/bot.svg")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/translate.html", "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)


def create_app():
    return app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:create_app()", host="0.0.0.0", port=8000, reload=True)
