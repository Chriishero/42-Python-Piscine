
def validate_ingredients(ingredients: str) -> str:
    if any(element in ingredients for element in
           ["fire", "water", "earth", "air"]):
        return (f"{ingredients} - VALID")
    else:
        return (f"{ingredients} - INVALID")
