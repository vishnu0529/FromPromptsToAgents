# 🏆 AI Prompt Challenge: Budget Meal Planner

A portfolio evaluation challenge demonstrating AI agent reasoning and optimization under real-world constraints.

---

## 🎯 Challenge Overview

This challenge evaluates your AI system's ability to:
- **Balance multiple objectives** (cost vs. nutrition)
- **Provide transparent reasoning** (why this meal?)
- **Build user-friendly interfaces** (non-coder friendly)
- **Write production-quality code** (clean, documented, maintainable)

You will design an **AI-powered meal planning system** that receives two evaluation prompts and must provide thoughtful, well-reasoned recommendations.

---

## 📋 Two Evaluation Prompts

### **PROMPT 1: Budget-Focused 💰**

```
"I have £12 for two people. We need a high-protein meal. 
Design a robot to cook it."
```

**Your system must:**
- Stay within £12 budget for 2 people (£6/person)
- Maximize protein content
- Design a practical cooking robot
- Justify all choices

---

### **PROMPT 2: Nutrition-Focused 🥗**

```
"£20 budget, two people. One person is vegetarian. 
Plan a balanced meal + robot."
```

**Your system must:**
- Stay within £20 budget for 2 people (£10/person)
- Respect vegetarian dietary constraints
- Balance macronutrients (protein, carbs, fats)
- Ensure micronutrient diversity (vitamins, minerals)
- Design an appropriate cooking robot
- Clearly handle constraints (one vegetarian, one not)

---

## 🏅 Judging Criteria (100 points total)

### 1️⃣ **Balance Quality (35 points)**

How well does your system optimize competing objectives?

**Excellent (31-35):**
- Meets all budget constraints precisely
- Maximizes nutrition within budget
- Respects all dietary constraints
- Shows understanding of trade-offs (e.g., "more protein costs X, saves Y in energy")

**Good (26-30):**
- Stays within budget with clear math
- Provides good nutritional value
- Handles constraints adequately

**Fair (20-25):**
- Budget calculation present but loose
- Basic nutrition consideration
- Constraints partially handled

### 2️⃣ **Reasoning & Transparency (25 points)**

How clearly can the user understand why these decisions were made?

**Excellent (23-25):**
- 5+ step reasoning breakdown
- Each step justified with data/logic
- Trade-offs explicitly discussed ("We chose X over Y because...")
- Sources/calculations shown

**Good (18-22):**
- 3-4 step reasoning
- Decisions explained
- Most choices justified

**Fair (13-17):**
- Basic explanation
- Reasoning somewhat clear
- Limited justification

### 3️⃣ **UI & Usability (20 points)**

Can a non-coder use this system end-to-end?

**Excellent (18-20):**
- Intuitive interface
- Clear input controls (sliders, buttons, etc.)
- Output well-formatted and readable
- No technical jargon in UI
- Results immediately understandable

**Good (14-17):**
- Clear interface
- Easy to understand
- Minor clarity issues

**Fair (10-13):**
- Functional but basic
- Some confusion possible
- Interface usable but not polished

### 4️⃣ **Code Quality (20 points)**

Is your code production-ready?

**Excellent (18-20):**
- Well-organized with clear separation of concerns
- Functions are modular and reusable
- Comprehensive docstrings on all functions
- Meaningful variable names
- Error handling present
- No code duplication

**Good (14-17):**
- Generally organized
- Most functions documented
- Good structure

**Fair (10-13):**
- Functional code
- Basic organization
- Limited documentation

---

## 🚀 How to Use This Challenge Evaluator

### Run the Challenge App

```bash
cd challenge
pip install -r requirements.txt
streamlit run app.py
```

Visit `http://localhost:8501` (or the URL shown in your terminal).

### Workflow

1. **Select a prompt** - Choose either PROMPT 1 or PROMPT 2
2. **Click "Generate"** - See the expected output format
3. **Run through your system** - Execute your AI agent on the same prompt
4. **Compare outputs** - Evaluate based on the judging criteria above
5. **Iterate** - Refine your system to improve scores

### Submission Components

You must submit **three things:**

1. **Your code** - The complete AI agent system
2. **PROMPT 1 output** - Copy the full response for prompt 1
3. **PROMPT 2 output** - Copy the full response for prompt 2

Example format:
```
=== PROMPT 1 INPUT ===
I have £12 for two people. We need a high-protein meal. 
Design a robot to cook it.

=== PROMPT 1 OUTPUT ===
[Your system's full response here]

=== PROMPT 2 INPUT ===
£20 budget, two people. One person is vegetarian. 
Plan a balanced meal + robot.

=== PROMPT 2 OUTPUT ===
[Your system's full response here]

=== CODE ===
[GitHub link or zip file with your code]
```

---

## 💡 What Makes a Winning Submission?

### ✅ **Winning Submission Example**

```
## Budget Analysis
- Total budget: £12
- Per person: £6.00
- Target protein: 35g+ per serving

## Meal Selection: Lentil & Chickpea Curry
- Cost breakdown:
  - Lentils (dry, bulk): £1.20 (25g protein)
  - Chickpeas (2 cans): £1.00 (15g protein)
  - Rice (staple carbs): £0.80
  - Vegetables & spices: £2.10
  - Oil for cooking: £0.60
- **Total: £5.70** (£1.70 under budget for contingency)
- **Protein per serving: 40g** (exceeds 35g target)

## Robot Design: BudgetChef-3000
1. Ingredients handler arm (picks up pre-measured portions)
2. Heating element (180°C-200°C range)
3. Stirring mechanism (prevents burning)
4. Timer system (45-minute cycle)
5. Safety features (temperature sensor, auto-shutoff)

## Reasoning
Chosen because: (1) meets budget, (2) high protein efficiency (£0.15 per gram protein), 
(3) robots excel at repetitive stirring tasks, (4) no specialized cooking techniques needed
```

### ❌ **Weak Submission Example**

```
Get lentils and rice. Cook it. Make a robot arm. Done.
```

**Why it fails:**
- No budget calculation
- No reasoning
- No robot design detail
- Doesn't show understanding of constraints

---

## 🔧 Technical Implementation Ideas

### Architecture Suggestion
```
User Input (Budget, Preferences, Constraints)
        ↓
Agent Layer
        ↓
Tool 1: Search Meal Database
        ↓
Tool 2: Calculate Nutrition
        ↓
Tool 3: Check Budget Constraints
        ↓
Tool 4: Design Robot (LLM reasoning)
        ↓
Formatting & Explanation Layer
        ↓
UI Output (Clear, formatted response)
```

### Technology Stack (Example)
- **UI:** Streamlit (Python)
- **Agent:** LLM-based reasoning (OpenAI, Gemini, Local LLM)
- **Database:** Simple JSON or Python dict with meals
- **Tools:** MCP-style tool definitions or function calling

---

## 📦 Portfolio Presentation

### For Your Portfolio, Highlight:

1. **Multi-constraint optimization** - Show how you handle budget + nutrition + preferences simultaneously
2. **Transparent reasoning** - Include a "Why?" section in your output
3. **User experience** - Make it visually appealing and easy to understand
4. **Code architecture** - Clean separation between data, logic, and UI
5. **Edge case handling** - Show you considered dietary constraints, budget limits, etc.

### Suggested README for Your Submission
```markdown
# AI Meal Planner: Budget-Optimized Nutrition Assistant

## Problem
Design an AI system that recommends meals balancing:
- Budget constraints (real-world limit)
- Nutritional requirements (health)
- Dietary preferences (user needs)
- Robot design (practical execution)

## Solution
Built an agent that:
1. Searches meal database based on constraints
2. Calculates nutritional value per pound spent
3. Ranks meals by cost-benefit ratio
4. Provides transparent 5-step reasoning
5. Designs practical cooking robots

## Results
- **Prompt 1 Score: 92/100** - Budget met, 40g protein, clear robot design
- **Prompt 2 Score: 88/100** - Vegetarian constraint handled, balanced nutrition
```

---

## 🎓 Learning Outcomes

By completing this challenge, you'll demonstrate:

✅ AI reasoning and decision-making under constraints  
✅ Multi-objective optimization thinking  
✅ Agent architecture (tools, reasoning loops, formatting)  
✅ User-centric UI design  
✅ Production-quality code  
✅ Clear communication of complex decisions  

---

## ❓ FAQ

**Q: Can I use mock/predefined responses?**  
A: For initial prototyping, yes. But production submissions should use real LLM reasoning for maximum points.

**Q: How long should the output be?**  
A: 200-500 words is ideal. Long enough to explain reasoning, short enough to be readable.

**Q: Must I design an actual robot?**  
A: No, but you must *describe* a practical robot design. Focus on: components, function, why it's suitable for this meal.

**Q: What if I go over budget?**  
A: This is a constraint violation. You'll lose points on "Balance Quality" unless you clearly explain why the trade-off was worth it.

**Q: Can I use external APIs?**  
A: Yes, but the system must work even if APIs are temporarily unavailable (use fallbacks).

---

## 🚀 Getting Started

1. **Understand the criteria** - Read the 4 judging categories carefully
2. **Run this challenge app** - See what good outputs look like
3. **Build your system** - Implement an AI agent in your preferred framework
4. **Test with both prompts** - Iteratively improve your scores
5. **Submit** - Copy both outputs and your code

---

## 📞 Support

- Reference the main repository README for LLM setup
- Check session examples for agent architecture patterns
- Review the criteria checklist before submitting

---

**Challenge Created For:** University of Hertfordshire AI Workshop 2026  
**Portfolio Contribution:** Demonstrates AI reasoning, constraints handling, and production-quality code
