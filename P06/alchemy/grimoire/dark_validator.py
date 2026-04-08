from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = dark_spell_allowed_ingredients()

    for spell in allowed_ingredients:
        if spell.lower() in ingredients.lower():
            return ingredients + " - VALID"
    return ingredients + " - INVALID"
