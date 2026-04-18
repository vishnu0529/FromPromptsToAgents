"""
Budget Meal Planner MCP Server
==============================
Provides tools for finding nutritious meals within budget constraints.
Includes expanded dish database with pricing and nutritional information.
"""

import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Budget Meal Planner")

# ============================================================================
# ENHANCED DISH DATABASE (with prices, nutrition, and dietary info)
# ============================================================================

DISHES = {
    "lentil curry": {
        "name": "Lentil & Chickpea Curry",
        "cuisine": "Indian",
        "difficulty": "easy",
        "prep_time_minutes": 15,
        "cook_time_minutes": 30,
        "servings": 4,
        "price_gbp": 8.50,  # Total cost for 4 servings
        "protein_g": 28,  # Per serving
        "calories_kcal": 350,  # Per serving
        "fat_g": 8,
        "carbs_g": 45,
        "fiber_g": 12,
        "key_vitamins": ["Iron", "Folate", "Vitamin C", "Magnesium"],
        "dietary_flags": ["vegan", "gluten-free", "high-protein"],
        "ingredients": [
            {"item": "red lentils", "quantity": "200g", "price_gbp": 1.20},
            {"item": "chickpeas", "quantity": "2 cans", "price_gbp": 1.50},
            {"item": "onion", "quantity": "2", "price_gbp": 0.60},
            {"item": "garlic", "quantity": "4 cloves", "price_gbp": 0.30},
            {"item": "ginger", "quantity": "2 tbsp", "price_gbp": 0.50},
            {"item": "coconut milk", "quantity": "400ml", "price_gbp": 2.00},
            {"item": "tomatoes", "quantity": "1 can", "price_gbp": 0.60},
            {"item": "spinach", "quantity": "200g", "price_gbp": 1.50},
            {"item": "spices", "quantity": "mixed", "price_gbp": 0.40},
        ],
        "description": "Protein-rich vegan curry with lentils and chickpeas, perfect for budget dining.",
    },
    "tofu stir-fry": {
        "name": "Crispy Tofu Stir-Fry",
        "cuisine": "Asian",
        "difficulty": "intermediate",
        "prep_time_minutes": 20,
        "cook_time_minutes": 15,
        "servings": 4,
        "price_gbp": 12.00,
        "protein_g": 22,
        "calories_kcal": 320,
        "fat_g": 14,
        "carbs_g": 28,
        "fiber_g": 6,
        "key_vitamins": ["Iron", "Calcium", "Vitamin K", "Vitamin C"],
        "dietary_flags": ["vegan", "gluten-free"],
        "ingredients": [
            {"item": "firm tofu", "quantity": "500g", "price_gbp": 2.50},
            {"item": "broccoli", "quantity": "300g", "price_gbp": 1.50},
            {"item": "bell pepper", "quantity": "2", "price_gbp": 1.80},
            {"item": "snap peas", "quantity": "200g", "price_gbp": 2.00},
            {"item": "ginger", "quantity": "1 tbsp", "price_gbp": 0.30},
            {"item": "garlic", "quantity": "3 cloves", "price_gbp": 0.20},
            {"item": "soy sauce", "quantity": "3 tbsp", "price_gbp": 0.40},
            {"item": "sesame oil", "quantity": "2 tbsp", "price_gbp": 2.00},
            {"item": "rice", "quantity": "200g", "price_gbp": 1.30},
        ],
        "description": "Colorful vegan stir-fry packed with vegetables and plant-based protein.",
    },
    "quinoa salad": {
        "name": "Mediterranean Quinoa Salad",
        "cuisine": "Mediterranean",
        "difficulty": "easy",
        "prep_time_minutes": 20,
        "cook_time_minutes": 15,
        "servings": 4,
        "price_gbp": 10.50,
        "protein_g": 12,
        "calories_kcal": 280,
        "fat_g": 9,
        "carbs_g": 38,
        "fiber_g": 8,
        "key_vitamins": ["Magnesium", "Manganese", "Phosphorus", "Vitamin E"],
        "dietary_flags": ["vegetarian", "vegan", "gluten-free"],
        "ingredients": [
            {"item": "quinoa", "quantity": "200g dry", "price_gbp": 2.50},
            {"item": "cherry tomatoes", "quantity": "300g", "price_gbp": 2.00},
            {"item": "cucumber", "quantity": "1", "price_gbp": 0.80},
            {"item": "red onion", "quantity": "0.5", "price_gbp": 0.30},
            {"item": "feta cheese", "quantity": "100g", "price_gbp": 1.80},
            {"item": "olives", "quantity": "100g", "price_gbp": 1.50},
            {"item": "olive oil", "quantity": "3 tbsp", "price_gbp": 0.80},
            {"item": "lemon", "quantity": "1", "price_gbp": 0.40},
            {"item": "fresh herbs", "quantity": "handful", "price_gbp": 0.60},
        ],
        "description": "Complete protein salad with all 9 amino acids, packed with Mediterranean vegetables.",
    },
    "bean soup": {
        "name": "Mixed Bean Soup",
        "cuisine": "Global",
        "difficulty": "easy",
        "prep_time_minutes": 15,
        "cook_time_minutes": 40,
        "servings": 6,
        "price_gbp": 7.50,
        "protein_g": 16,
        "calories_kcal": 220,
        "fat_g": 3,
        "carbs_g": 42,
        "fiber_g": 11,
        "key_vitamins": ["Iron", "Folate", "Potassium", "Manganese"],
        "dietary_flags": ["vegan", "gluten-free", "high-fiber"],
        "ingredients": [
            {"item": "mixed canned beans", "quantity": "3 cans", "price_gbp": 1.80},
            {"item": "carrots", "quantity": "3", "price_gbp": 0.90},
            {"item": "celery", "quantity": "2 stalks", "price_gbp": 0.60},
            {"item": "onion", "quantity": "1", "price_gbp": 0.30},
            {"item": "garlic", "quantity": "2 cloves", "price_gbp": 0.15},
            {"item": "tomatoes", "quantity": "1 can", "price_gbp": 0.60},
            {"item": "vegetable broth", "quantity": "1 liter", "price_gbp": 1.50},
            {"item": "herbs", "quantity": "mixed", "price_gbp": 0.75},
        ],
        "description": "Budget-friendly soup loaded with plant proteins and fiber, makes 6 hearty servings.",
    },
    "egg fried rice": {
        "name": "Vegetable Egg Fried Rice",
        "cuisine": "Asian",
        "difficulty": "easy",
        "prep_time_minutes": 15,
        "cook_time_minutes": 10,
        "servings": 4,
        "price_gbp": 6.50,
        "protein_g": 14,
        "calories_kcal": 310,
        "fat_g": 10,
        "carbs_g": 42,
        "fiber_g": 3,
        "key_vitamins": ["Choline", "Selenium", "Vitamin B12", "Vitamin A"],
        "dietary_flags": ["vegetarian", "gluten-free"],
        "ingredients": [
            {"item": "rice (cooked)", "quantity": "400g", "price_gbp": 0.80},
            {"item": "eggs", "quantity": "4", "price_gbp": 1.20},
            {"item": "mixed vegetables", "quantity": "300g", "price_gbp": 1.80},
            {"item": "peas", "quantity": "100g", "price_gbp": 0.60},
            {"item": "corn", "quantity": "100g", "price_gbp": 0.50},
            {"item": "soy sauce", "quantity": "2 tbsp", "price_gbp": 0.30},
            {"item": "garlic", "quantity": "2 cloves", "price_gbp": 0.15},
            {"item": "sesame oil", "quantity": "1 tbsp", "price_gbp": 0.45},
        ],
        "description": "Quick, affordable meal with eggs and vegetables over rice. Perfect for leftovers.",
    },
    "lentil pasta": {
        "name": "Lentil Bolognese Pasta",
        "cuisine": "Italian",
        "difficulty": "easy",
        "prep_time_minutes": 10,
        "cook_time_minutes": 30,
        "servings": 4,
        "price_gbp": 9.00,
        "protein_g": 18,
        "calories_kcal": 420,
        "fat_g": 4,
        "carbs_g": 72,
        "fiber_g": 13,
        "key_vitamins": ["Iron", "Folate", "Magnesium", "Manganese"],
        "dietary_flags": ["vegan", "high-protein"],
        "ingredients": [
            {"item": "pasta", "quantity": "400g", "price_gbp": 1.00},
            {"item": "green lentils", "quantity": "250g dry", "price_gbp": 1.50},
            {"item": "tomatoes", "quantity": "2 cans", "price_gbp": 1.20},
            {"item": "onion", "quantity": "1", "price_gbp": 0.30},
            {"item": "garlic", "quantity": "3 cloves", "price_gbp": 0.20},
            {"item": "carrot", "quantity": "1", "price_gbp": 0.30},
            {"item": "olive oil", "quantity": "2 tbsp", "price_gbp": 0.40},
            {"item": "herbs", "quantity": "mixed", "price_gbp": 0.60},
            {"item": "vegetable broth", "quantity": "500ml", "price_gbp": 0.50},
        ],
        "description": "Hearty plant-based bolognese with lentils and whole grain pasta.",
    },
    "chickpea curry": {
        "name": "Spiced Chickpea Curry",
        "cuisine": "Indian",
        "difficulty": "easy",
        "prep_time_minutes": 15,
        "cook_time_minutes": 25,
        "servings": 4,
        "price_gbp": 8.00,
        "protein_g": 15,
        "calories_kcal": 280,
        "fat_g": 9,
        "carbs_g": 38,
        "fiber_g": 10,
        "key_vitamins": ["Iron", "Manganese", "Magnesium", "Folate"],
        "dietary_flags": ["vegan", "gluten-free", "high-fiber"],
        "ingredients": [
            {"item": "chickpeas", "quantity": "2 cans", "price_gbp": 1.50},
            {"item": "onion", "quantity": "1", "price_gbp": 0.30},
            {"item": "tomatoes", "quantity": "1 can", "price_gbp": 0.60},
            {"item": "coconut milk", "quantity": "200ml", "price_gbp": 1.00},
            {"item": "spinach", "quantity": "150g", "price_gbp": 1.20},
            {"item": "garlic", "quantity": "3 cloves", "price_gbp": 0.20},
            {"item": "ginger", "quantity": "1 tbsp", "price_gbp": 0.30},
            {"item": "curry powder", "quantity": "2 tbsp", "price_gbp": 0.50},
            {"item": "rice", "quantity": "200g dry", "price_gbp": 0.40},
            {"item": "oil", "quantity": "2 tbsp", "price_gbp": 0.30},
        ],
        "description": "Budget-friendly Indian curry with chickpeas and greens, served over rice.",
    },
    "vegetable stew": {
        "name": "Root Vegetable & Barley Stew",
        "cuisine": "Global",
        "difficulty": "easy",
        "prep_time_minutes": 20,
        "cook_time_minutes": 40,
        "servings": 6,
        "price_gbp": 9.50,
        "protein_g": 10,
        "calories_kcal": 240,
        "fat_g": 3,
        "carbs_g": 48,
        "fiber_g": 9,
        "key_vitamins": ["Potassium", "Manganese", "Vitamin A", "Vitamin C"],
        "dietary_flags": ["vegan", "gluten-free"],
        "ingredients": [
            {"item": "barley", "quantity": "150g", "price_gbp": 0.80},
            {"item": "carrots", "quantity": "4", "price_gbp": 1.20},
            {"item": "potatoes", "quantity": "500g", "price_gbp": 1.00},
            {"item": "parsnips", "quantity": "2", "price_gbp": 0.80},
            {"item": "onion", "quantity": "1", "price_gbp": 0.30},
            {"item": "garlic", "quantity": "3 cloves", "price_gbp": 0.20},
            {"item": "vegetable broth", "quantity": "1.5 liters", "price_gbp": 2.00},
            {"item": "thyme", "quantity": "2 sprigs", "price_gbp": 0.40},
            {"item": "bay leaf", "quantity": "2", "price_gbp": 0.20},
            {"item": "oil", "quantity": "1 tbsp", "price_gbp": 0.10},
        ],
        "description": "Warming stew perfect for budget meals, makes 6 servings with whole grains.",
    },
    "tuna salad": {
        "name": "Mediterranean Tuna Salad",
        "cuisine": "Mediterranean",
        "difficulty": "easy",
        "prep_time_minutes": 15,
        "cook_time_minutes": 0,
        "servings": 2,
        "price_gbp": 7.50,
        "protein_g": 28,
        "calories_kcal": 220,
        "fat_g": 6,
        "carbs_g": 15,
        "fiber_g": 4,
        "key_vitamins": ["Omega-3", "Selenium", "Vitamin D", "Vitamin B12"],
        "dietary_flags": ["gluten-free", "high-protein"],
        "ingredients": [
            {"item": "canned tuna", "quantity": "2 cans", "price_gbp": 2.50},
            {"item": "mixed salad", "quantity": "150g", "price_gbp": 1.50},
            {"item": "cherry tomatoes", "quantity": "150g", "price_gbp": 1.00},
            {"item": "cucumber", "quantity": "0.5", "price_gbp": 0.40},
            {"item": "olives", "quantity": "50g", "price_gbp": 0.80},
            {"item": "feta cheese", "quantity": "50g", "price_gbp": 0.90},
            {"item": "olive oil", "quantity": "1 tbsp", "price_gbp": 0.30},
            {"item": "lemon", "quantity": "0.5", "price_gbp": 0.20},
        ],
        "description": "High-protein salad with omega-3 rich tuna and Mediterranean vegetables.",
    },
}

# ============================================================================
# MCP TOOLS
# ============================================================================


@mcp.tool()
def get_nutrition(dish_name: str) -> dict:
    """Get nutritional information for a dish.
    
    Args:
        dish_name: Name of the dish (e.g., 'lentil curry', 'tofu stir-fry')
    
    Returns:
        Dict with nutritional info per serving including protein, calories, vitamins.
    """
    dish_key = dish_name.lower()
    if dish_key not in DISHES:
        available = ", ".join(DISHES.keys())
        return {"error": f"Dish not found. Available: {available}"}
    
    dish = DISHES[dish_key]
    return {
        "name": dish["name"],
        "protein_g": dish["protein_g"],
        "calories_kcal": dish["calories_kcal"],
        "fat_g": dish["fat_g"],
        "carbs_g": dish["carbs_g"],
        "fiber_g": dish["fiber_g"],
        "key_vitamins": dish["key_vitamins"],
        "servings": dish["servings"],
    }


@mcp.tool()
def get_price(dish_name: str, servings: int = 1) -> dict:
    """Get price information for a dish.
    
    Args:
        dish_name: Name of the dish
        servings: Number of servings (1, 2, 3, 4, or more)
    
    Returns:
        Dict with price per serving and total price.
    """
    dish_key = dish_name.lower()
    if dish_key not in DISHES:
        return {"error": "Dish not found"}
    
    dish = DISHES[dish_key]
    base_price = dish["price_gbp"]
    base_servings = dish["servings"]
    
    # Calculate price for requested servings
    price_per_serving = base_price / base_servings
    total_price = price_per_serving * servings
    
    return {
        "name": dish["name"],
        "price_per_serving_gbp": round(price_per_serving, 2),
        "total_price_gbp": round(total_price, 2),
        "servings": servings,
    }


@mcp.tool()
def fit_budget(budget_gbp: float, people: int, preferences: str = "") -> dict:
    """Find meals that fit within a budget for a given number of people.
    
    Args:
        budget_gbp: Total budget in pounds
        people: Number of people to feed
        preferences: Dietary preferences ('vegan', 'vegetarian', 'high-protein', etc.)
    
    Returns:
        Dict with recommendations and meal combinations.
    """
    budget_per_person = budget_gbp / people if people > 0 else 0
    
    # Filter dishes based on preferences
    matching_dishes = []
    for dish_name, dish_data in DISHES.items():
        price_per_person = dish_data["price_gbp"] / dish_data["servings"]
        
        # Check budget
        if price_per_person <= budget_per_person:
            # Check preferences
            if preferences:
                prefs = preferences.lower().split(",")
                flags = dish_data.get("dietary_flags", [])
                if any(pref.strip() in flags for pref in prefs):
                    matching_dishes.append({
                        "name": dish_data["name"],
                        "price_per_person": round(price_per_person, 2),
                        "protein_g": dish_data["protein_g"],
                        "calories_kcal": dish_data["calories_kcal"],
                        "key_vitamins": dish_data["key_vitamins"],
                        "dietary_flags": flags,
                    })
            else:
                matching_dishes.append({
                    "name": dish_data["name"],
                    "price_per_person": round(price_per_person, 2),
                    "protein_g": dish_data["protein_g"],
                    "calories_kcal": dish_data["calories_kcal"],
                    "key_vitamins": dish_data["key_vitamins"],
                    "dietary_flags": dish_data.get("dietary_flags", []),
                })
    
    # Sort by protein content (descending)
    matching_dishes.sort(key=lambda x: x["protein_g"], reverse=True)
    
    return {
        "budget_gbp": budget_gbp,
        "people": people,
        "budget_per_person": round(budget_per_person, 2),
        "recommendations": matching_dishes[:5],  # Top 5 options
        "total_found": len(matching_dishes),
    }


@mcp.tool()
def list_all_dishes() -> dict:
    """List all available dishes with their key information."""
    dishes = []
    for key, dish in DISHES.items():
        dishes.append({
            "name": dish["name"],
            "total_price_gbp": dish["price_gbp"],
            "protein_g": dish["protein_g"],
            "calories_kcal": dish["calories_kcal"],
            "servings": dish["servings"],
            "dietary_flags": dish.get("dietary_flags", []),
        })
    return {"dishes": dishes, "total_available": len(dishes)}


@mcp.tool()
def get_shopping_list(dish_name: str, servings: int = 1) -> dict:
    """Get shopping list for a dish with quantities and prices.
    
    Args:
        dish_name: Name of the dish
        servings: Number of servings
    
    Returns:
        Shopping list with items, quantities, and prices.
    """
    dish_key = dish_name.lower()
    if dish_key not in DISHES:
        return {"error": "Dish not found"}
    
    dish = DISHES[dish_key]
    base_servings = dish["servings"]
    multiplier = servings / base_servings
    
    shopping_list = []
    total_price = 0
    
    for ingredient in dish["ingredients"]:
        item_price = ingredient.get("price_gbp", 0) * multiplier
        total_price += item_price
        shopping_list.append({
            "item": ingredient["item"],
            "quantity": ingredient["quantity"],
            "estimated_price_gbp": round(item_price, 2),
        })
    
    return {
        "dish": dish["name"],
        "servings": servings,
        "shopping_list": shopping_list,
        "total_estimated_price": round(total_price, 2),
    }
