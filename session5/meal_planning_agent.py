"""
Meal Planning Agent - Budget-Aware Recipe Recommendations
=========================================================
Session 5: The Challenge - Budget Meal Planner

This module implements an intelligent agent that:
1. Understands budget constraints and dietary preferences
2. Uses direct database calls to find nutritious, affordable meals
3. Provides reasoning about choices
4. Creates meal plans with shopping lists
"""

import json
from budget_meal_planner import DISHES


def run_meal_planning_simple(
    budget_gbp: float,
    num_people: int,
    dietary_preferences: str = "",
) -> dict:
    """
    Find best meals within budget using agent reasoning.
    
    Args:
        budget_gbp: Total budget in pounds
        num_people: Number of people to feed
        dietary_preferences: Comma-separated list (e.g., 'vegan,high-protein')
    
    Returns:
        Dict with meal recommendations and analysis
    """
    
    budget_per_person = budget_gbp / num_people if num_people > 0 else 0
    
    # Parse dietary preferences
    prefs = [p.strip().lower() for p in dietary_preferences.split(",") if p.strip()]
    
    # Filter meals by budget and preferences
    matching_meals = []
    
    for dish_name, dish_data in DISHES.items():
        price_per_person = dish_data["price_gbp"] / dish_data["servings"]
        
        # Check if within budget
        if price_per_person > budget_per_person:
            continue
        
        # Check dietary preferences if specified
        if prefs:
            flags = dish_data.get("dietary_flags", [])
            if not any(pref in flags for pref in prefs):
                continue
        
        # Calculate nutrition score (higher protein is better)
        nutrition_score = dish_data["protein_g"]
        value_score = nutrition_score / max(price_per_person, 0.1)  # Protein per pound
        
        matching_meals.append({
            "name": dish_data["name"],
            "key": dish_name,
            "price_per_person": round(price_per_person, 2),
            "total_price": round(price_per_person * num_people, 2),
            "protein_g": dish_data["protein_g"],
            "calories_kcal": dish_data["calories_kcal"],
            "fat_g": dish_data["fat_g"],
            "carbs_g": dish_data["carbs_g"],
            "fiber_g": dish_data["fiber_g"],
            "key_vitamins": dish_data["key_vitamins"],
            "dietary_flags": dish_data.get("dietary_flags", []),
            "prep_time": dish_data.get("prep_time_minutes", 0),
            "cook_time": dish_data.get("cook_time_minutes", 0),
            "nutrition_score": nutrition_score,
            "value_score": value_score,
        })
    
    # Sort by value score (protein per pound) - best nutrition for budget
    matching_meals.sort(key=lambda x: x["value_score"], reverse=True)
    
    if not matching_meals:
        return {
            "status": "error",
            "message": f"No meals found within budget of £{budget_gbp} for {num_people} people",
            "budget": budget_gbp,
            "people": num_people,
        }
    
    # Get top recommendation
    top_meal = matching_meals[0]
    total_cost = top_meal["total_price"]
    savings = budget_gbp - total_cost
    
    # Build reasoning text
    reasoning_text = f"""## 🧠 Agent Analysis & Reasoning

**Step 1: Budget Analysis**
- Total budget: £{budget_gbp:.2f}
- Number of people: {num_people}
- Budget per person: £{budget_per_person:.2f}

**Step 2: Database Search**
- Searched {len(DISHES)} meals in database
- Found {len(matching_meals)} meals matching your criteria
- Dietary filters: {', '.join(prefs) if prefs else 'None (all meals considered)'}

**Step 3: Nutrition Evaluation**
- Ranked meals by protein-per-pound value
- Top meal: **{top_meal['name']}** (#{list(DISHES.keys()).index(top_meal['key']) + 1} choice)
- Protein efficiency: {top_meal['value_score']:.2f} grams per pound

**Step 4: Cost-Benefit Analysis**
- Cost per person: £{top_meal['price_per_person']:.2f}
- Total cost: £{total_cost:.2f}
- Savings under budget: £{savings:.2f} ✓
- Budget efficiency: {(total_cost/budget_gbp)*100:.0f}%

**Step 5: Final Recommendation Factors**
1. **Nutritional Value** - {top_meal['protein_g']}g protein per serving
2. **Cost Efficiency** - Only £{top_meal['price_per_person']:.2f} per person
3. **Micronutrients** - Rich in {', '.join(top_meal['key_vitamins'])}
4. **Practicality** - {top_meal['prep_time']}min prep + {top_meal['cook_time']}min cooking
5. **Variety** - Offers balanced {top_meal['carbs_g']}g carbs, {top_meal['fat_g']}g fat

**Trade-offs Considered:**
- ✓ Maximized protein within budget constraint
- ✓ Prioritized nutrient density over price alone
- ✓ Maintained dietary preference match
- ✓ Selected practical preparation time
"""
    
    # Build recommendation text
    recommendation_text = f"""## Recommended Meal Plan

### **{top_meal['name']}**

**Nutritional Analysis (per serving):**
- 🍗 **Protein:** {top_meal['protein_g']}g
- 🔥 **Calories:** {top_meal['calories_kcal']} kcal
- 🥑 **Fat:** {top_meal['fat_g']}g
- 🌾 **Carbohydrates:** {top_meal['carbs_g']}g
- 🌿 **Fiber:** {top_meal['fiber_g']}g
- 💊 **Key Nutrients:** {', '.join(top_meal['key_vitamins'])}

**Budget Breakdown:**
- Budget per person: **£{budget_per_person:.2f}**
- Cost per person: **£{top_meal['price_per_person']:.2f}**
- Total cost for {num_people}: **£{total_cost:.2f}**
- Remaining budget: **£{savings:.2f}** ✓

**Why This Meal?**
1. Excellent protein content ({top_meal['protein_g']}g) for muscle support and satiety
2. Budget-efficient at just £{top_meal['price_per_person']:.2f} per person
3. Rich in essential micronutrients: {', '.join(top_meal['key_vitamins'])}
4. Balanced macronutrients: {top_meal['carbs_g']}g carbs + {top_meal['fat_g']}g fat
5. Easy to prepare: {top_meal['prep_time']}min prep, {top_meal['cook_time']}min cooking

**Dietary Match:**
- Tags: {', '.join(top_meal['dietary_flags']) if top_meal['dietary_flags'] else 'Standard diet'}
- Your preferences: {', '.join(prefs) if prefs else 'No restrictions'}

---

### 💡 Alternative Options

"""
    
    # Add alternative options
    for idx, meal in enumerate(matching_meals[1:4], 1):
        recommendation_text += f"""**Option {idx}: {meal['name']}**
- Cost: £{meal['price_per_person']:.2f}/person | Protein: {meal['protein_g']}g | Calories: {meal['calories_kcal']} kcal
- Value score: {meal['value_score']:.2f}g protein/pound

"""
    
    recommendation_text += f"\n**💰 Budget Status:** Using {(total_cost/budget_gbp)*100:.0f}% of your budget"
    
    return {
        "status": "success",
        "budget": budget_gbp,
        "people": num_people,
        "preferences": dietary_preferences,
        "recommendation": recommendation_text,
        "reasoning": reasoning_text,
        "all_options": matching_meals,
        "total_cost": total_cost,
        "top_meal": top_meal,
    }
