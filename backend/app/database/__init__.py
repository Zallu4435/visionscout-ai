"""
Database layer — loads and serves the recipe JSON data store.
All database functions are re-exported here so callers can simply do:
    from backend.app.database import get_recipe_by_id
"""

from backend.app.database.db import load_db, get_all_recipes, get_recipe_by_id

__all__ = ["load_db", "get_all_recipes", "get_recipe_by_id"]
