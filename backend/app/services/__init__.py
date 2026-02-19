"""
Business logic layer — recipe search, scoring, and AI feedback generation.
All service functions are re-exported here so callers can simply do:
    from backend.app.services import search_recipes_logic, validate_plan_logic
"""

from backend.app.services.recipe_service import (
    search_recipes_logic,
    validate_plan_logic,
    generate_ai_feedback,
)

__all__ = ["search_recipes_logic", "validate_plan_logic", "generate_ai_feedback"]
