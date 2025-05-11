from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import sys

# Dynamically import router based on deployment environment
try:
    from routes import translation_routes
except ImportError:
    # When in Vercel, we need to use a different import strategy
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, parent_dir)
    from routes import translation_routes

router = APIRouter()
templates = Jinja2Templates(directory="templates")

router.include_router(translation_routes.router, tags=["translation"])