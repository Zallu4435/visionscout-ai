"""
API route definitions for recipe endpoints.
The FastAPI router is re-exported here so main.py can simply do:
    from backend.app.routes import router
"""

from backend.app.routes.recipes import router

__all__ = ["router"]
