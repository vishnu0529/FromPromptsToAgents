# 🤖 From Prompts to Agents

An AI workshop demonstrating the evolution from simple prompts to sophisticated multi-agent systems. This project showcases how AI agents can be progressively enhanced with tools, reasoning, and real-world problem-solving capabilities.

**Workshop | 18 April 2026 | University of Hertfordshire**

---

## 👥 Presenters

| Presenter | Role | LinkedIn |
|---|---|---|
| **Abolfazl Zaraki** | Senior Lecturer in Robotics and AI | [Profile](https://www.linkedin.com/in/abolfazl-zaraki-8b48b12a/) |
| **M. Reza Shahabian A.** | Principal AI Engineer \| AI Researcher | [Profile](https://www.linkedin.com/in/mrshahabian/) |
| **Khashayar Ghamati** | Principal AI Engineer \| AI Researcher | [Profile](https://www.linkedin.com/in/khashayarghamati/) |
| **Ali Fallahi** | AI UX Researcher \| HRI | [Profile](https://www.linkedin.com/in/ali-fallahi/) |
| **Danial Zafaranchizadeh M.** | AI Engineer \| Robotics Researcher | [Profile](https://www.linkedin.com/in/danial-za/) |

Brought to you by **PARSAI** and the **School of Physics, Engineering and Computer Science, University of Hertfordshire**.

---

## 🎯 Project Overview

This repository contains **five progressive sessions** plus a **final challenge**:

| Session | Topic | Focus |
|---------|-------|-------|
| **Session 1** | Hello LLM | Basic LLM calls, conversations, prompt engineering |
| **Session 2** | Robotics Agent | Tools, MCP protocol, agentic loops |
| **Session 3** | RAG System | Retrieval-augmented generation, knowledge grounding |
| **Session 4** | Recipe Agent | Domain-specific agents, multi-tool orchestration |
| **Session 5** | Budget Meal Planner ⭐ | Complete system: UI, optimization, reasoning |
| **Challenge** | Two Prompts 🏆 | Evaluate agent reasoning and design |

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/vishnu0529/FromPromptsToAgents.git
cd FromPromptsToAgents

# Set up Python environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Start with Session 5 (complete system)
cd session5
pip install -r requirements.txt
cp .env.example .env      # Configure API keys (see below)
streamlit run app.py
```

Visit `http://localhost:8501` and set a budget to see AI-powered meal planning in action!

---

## 📁 Repository Structure

```
FromPromptsToAgents/
├── README.md
├── pyproject.toml
├── streamlit_app.py
│
├── session1/                          # Hello LLM (5 steps)
│   ├── llm_client.py
│   ├── requirements.txt
│   ├── .env.example
│   └── steps/
│       ├── step1_hello_llm.py         # First LLM call
│       ├── step2_conversation.py      # Multi-turn chat
│       ├── step3_temperature.py       # Output control
│       ├── step4_chatbot.py           # Streamlit UI
│       └── step5_personas.py          # Role-playing
│
├── session2/                          # Robotics Agent + MCP
│   ├── llm_client.py
│   ├── robotics_agent.py              # Agent implementation
│   ├── robotics_mcp_server.py         # MCP server with tools
│   ├── test_server.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── robotics_data/
│   │   ├── sensors.json
│   │   ├── actuators.json
│   │   └── components.json
│   └── steps/
│       ├── step1_explore_data.py
│       ├── step2_test_tools.py
│       └── step3_run_agent.py
│
├── session3/                          # RAG System
│   ├── llm_client.py
│   ├── rag_demo.py                    # Core RAG implementation
│   ├── rag_streamlit.py               # Interactive UI
│   ├── requirements.txt
│   └── .env.example
│
├── session4/                          # Recipe Agent
│   ├── llm_client.py
│   ├── recipe_agent.py
│   ├── recipe_mcp_server.py           # Recipe tools
│   ├── test_server.py
│   ├── requirements.txt
│   ├── .env.example
│   └── steps/
│       ├── step1_explore_dishes.py
│       ├── step2_test_tools.py
│       └── step3_run_agent.py
│
├── session5/                          # Budget Meal Planner (Final)
│   ├── app.py                         # Main Streamlit UI
│   ├── budget_meal_planner.py         # MCP server with 10-dish database
│   ├── meal_planning_agent.py         # Agent with reasoning
│   ├── llm_client.py
│   ├── agents.py
│   ├── recipe_mcp_server.py
│   ├── robotics_mcp_server.py
│   ├── requirements.txt
│   └── .env.example
│
└── challenge/                         # Challenge Evaluation
    └── app.py                         # Two-prompt evaluator for submission
```

---

## 📚 Sessions Explained

### **Session 1: Hello LLM**
Learn the basics of connecting to LLMs and building conversations.

**What you'll learn:**
- Simple LLM API calls
- Multi-turn conversations
- Temperature and output control
- Prompt engineering techniques
- Building simple Streamlit UIs

**Run a step:**
```bash
cd session1
python steps/step1_hello_llm.py
```

---

### **Session 2: Robotics Agent**
Build agents that can use external tools and search databases.

**What you'll learn:**
- MCP (Model Context Protocol) server architecture
- Tool definitions and calling
- Agentic loop implementation
- Reasoning with external knowledge
- Domain-specific problem solving

**Key files:**
- `robotics_mcp_server.py` - Defines tools for robotics problems
- `robotics_agent.py` - Agent that uses the tools
- `robotics_data/` - Sensor, actuator, and component databases

**Run the agent:**
```bash
cd session2
python steps/step3_run_agent.py
```

---

### **Session 3: RAG System**
Implement Retrieval-Augmented Generation to ground AI in real data.

**What you'll learn:**
- Document indexing and search
- Embedding and vector stores
- Combining search with LLM reasoning
- Building knowledge-aware AI systems

**Key files:**
- `rag_demo.py` - Core RAG implementation
- `rag_streamlit.py` - Interactive interface

**Try it:**
```bash
cd session3
streamlit run rag_streamlit.py
```

---

### **Session 4: Recipe Agent**
Multi-tool agent for recipe analysis and meal planning.

**What you'll learn:**
- Domain-specific tool orchestration
- Recipe database querying
- Nutrition analysis
- Multi-constraint optimization

**Run the agent:**
```bash
cd session4
python steps/step3_run_agent.py
```

---

### **Session 5: Budget Meal Planner** ⭐
Complete production-ready system with UI and reasoning.

**Features:**
- 🍽️ AI-powered meal planning within budget constraints
- 💰 Cost vs. nutrition optimization
- 🧠 Transparent reasoning with 5-step breakdown
- 🎨 User-friendly Streamlit interface
- 📊 Multiple meal suggestions with alternatives
- 10-dish database with complete nutrition data

**Architecture:**
- `app.py` - Streamlit UI with sliders and filters
- `budget_meal_planner.py` - 10-meal database with analysis tools
- `meal_planning_agent.py` - Synchronous agent with optimization logic

**Try it:**
```bash
cd session5
streamlit run app.py
```

Set your budget (£5-£100), number of people, dietary preferences, and click "Find Best Meals" to see the AI recommend optimized meals with reasoning.

---

### **The Challenge** 🏆

Evaluate an AI agent's ability to balance multiple constraints and provide clear reasoning.

**Location:** `challenge/`

**Two Evaluation Prompts:**

**PROMPT 1 - Budget-focused 💰**
```
I have £12 for two people. We need a high-protein meal. Design a robot to cook it.
```

**PROMPT 2 - Nutrition-focused 🥗**
```
£20 budget, two people. One person is vegetarian. Plan a balanced meal + robot.
```

**Judging Criteria (100 points total):**
- ✅ **Balance Quality (35%)** - Does it optimize nutrition vs. cost?
- ✅ **Reasoning (25%)** - Are decisions clearly explained?
- ✅ **UI & Usability (20%)** - Can non-coders use it?
- ✅ **Code Quality (20%)** - Is the code clean and documented?

**Try the challenge:**
```bash
cd challenge
streamlit run app.py
```

Select each prompt, click "Generate", and copy both the prompt and response for submission.

---

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.9+
- macOS, Linux, or Windows
- 2GB RAM minimum
- Internet connection

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vishnu0529/FromPromptsToAgents.git
   cd FromPromptsToAgents
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   
   # On Linux / macOS:
   source venv/bin/activate
   
   # On Windows (Command Prompt):
   venv\Scripts\activate.bat
   
   # On Windows (PowerShell):
   venv\Scripts\Activate.ps1
   ```

   Your prompt should show `(venv)` when active.

3. **Install dependencies:**
   ```bash
   cd session5
   pip install -r requirements.txt
   ```

4. **Configure API keys** (see below)

---

## 🔑 LLM Backend Configuration

Each session requires at least one LLM backend configured. Create a `.env` file in the session directory:

### Option 1: Local University LLM (Recommended during workshop)

```env
LLM_SERVICE_URL=https://uhhpc.herts.ac.uk/qwen
LLM_API_TOKEN=<provided-by-instructor>
```

The university runs **Qwen2.5-72B-Instruct** on a GPU cluster. Your instructor will provide the token.

### Option 2: Google Gemini (Free)

1. Go to https://aistudio.google.com
2. Sign in with your Google account
3. Click "Get API Key" in the left sidebar
4. Create a new API key
5. Add to `.env`:
   ```env
   GEMINI_API_KEY=your-key-here
   GEMINI_MODEL=gemini-2.5-flash-lite
   ```

### Option 3: OpenAI API (Paid)

1. Get an API key at https://platform.openai.com/api-keys
2. Add to `.env`:
   ```env
   OPENAI_API_KEY=your-key-here
   OPENAI_MODEL=gpt-4o-mini
   ```

**Test your connection:**
```bash
cd session1
python llm_client.py
```

You should see which backend is active and a test response.

---

## 🏃 Running Each Session

### Session 1: Basic LLM
```bash
cd session1
python steps/step1_hello_llm.py        # First LLM call
python steps/step2_conversation.py     # Multi-turn chat
streamlit run steps/step4_chatbot.py   # UI version
```

### Session 2: Robotics Agent
```bash
cd session2
python steps/step1_explore_data.py     # Browse database
python steps/step2_test_tools.py       # Test tools
python steps/step3_run_agent.py        # Run agent
```

### Session 3: RAG System
```bash
cd session3
python rag_demo.py                     # Console demo
streamlit run rag_streamlit.py         # Interactive UI
```

### Session 4: Recipe Agent
```bash
cd session4
python steps/step1_explore_dishes.py
python steps/step3_run_agent.py
```

### Session 5: Budget Meal Planner
```bash
cd session5
streamlit run app.py
```

### Challenge Evaluation
```bash
cd challenge
streamlit run app.py
```

---

## 🔑 Key Concepts

### LLM Client
Centralized abstraction for communicating with language models. Automatically detects available backend (local, Gemini, or OpenAI).

### MCP (Model Context Protocol)
Standard protocol defining how agents communicate with external tools and databases. Each session uses MCP servers to provide structured tool interfaces.

### Agentic Loop
Core pattern where agents:
1. Receive user input
2. Decide which tools to call (or generate response)
3. Execute tools and get results
4. Feed results back to the LLM
5. Repeat until generating final response

### Budget Meal Planner Architecture
```
User Input (Budget, People, Preferences)
        ↓
Meal Planning Agent
        ↓
Tool: Filter by budget/preferences
        ↓
Tool: Calculate nutrition value scores
        ↓
Ranking and selection
        ↓
AI Reasoning generation
        ↓
Recommendation + Alternatives + Explanation
```

---

## 🎓 Learning Path

**Recommended order:**
1. Start with **Session 1** - Understand LLM basics
2. Progress to **Session 2** - Learn agents and tools
3. Explore **Session 3** - See RAG patterns
4. Complete **Session 4** - Domain-specific applications
5. Master **Session 5** - Full system with UI
6. Tackle **Challenge** - Evaluate your understanding

---

## ❓ Troubleshooting

**"No LLM backend available"**
→ Create a `.env` file in the session directory with API keys. See LLM Backend Configuration section above.

**"ModuleNotFoundError"**
→ Did you run `pip install -r requirements.txt`? Make sure you're in the correct session directory.

**Gemini 429 Too Many Requests**
→ The shared workshop key has rate limits. Get your own free key at https://aistudio.google.com → Get API Key

**Python version issues**
→ This project requires Python 3.9+. Check with `python --version`

**Streamlit app not responding**
→ Try running from a standalone terminal (not IDE-embedded terminals which can intercept keyboard input)

**Port already in use**
→ Run on a different port: `streamlit run app.py -- --server.port 8502`

---

## 🌐 Resources

- [Model Context Protocol (MCP)](https://spec.modelcontextprotocol.io/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API](https://platform.openai.com/docs/api-reference)
- [Google Gemini API](https://ai.google.dev/)
- [Discord Community](https://discord.gg/UGsfhZq3)

---

## 📞 Support

**Issues or questions?**
- Check the Troubleshooting section above
- Review individual session `.env.example` files for configuration
- Join our Discord: https://discord.gg/UGsfhZq3

---

## 📝 License

Educational use only. University of Hertfordshire AI Workshop 2026.

---

**Created by:** PARSAI & University of Hertfordshire  
**Date:** 18 April 2026  
**Repository:** https://github.com/vishnu0529/FromPromptsToAgents
# 🤖 From Prompts to Agents

An AI workshop demonstrating the evolution from simple prompts to sophisticated multi-agent systems.

**Workshop | 18 April 2026 | University of Hertfordshire**

---

## 👥 Presenters

| Presenter | Role | LinkedIn |
|---|---|---|
| **Abolfazl Zaraki** | Senior Lecturer in Robotics and AI | [Profile](https://www.linkedin.com/in/abolfazl-zaraki-8b48b12a/) |
| **M. Reza Shahabian A.** | Principal AI Engineer \| AI Researcher | [Profile](https://www.linkedin.com/in/mrshahabian/) |
| **Khashayar Ghamati** | Principal AI Engineer \| AI Researcher | [Profile](https://www.linkedin.com/in/khashayarghamati/) |
| **Ali Fallahi** | AI UX Researcher \| HRI | [Profile](https://www.linkedin.com/in/ali-fallahi/) |
| **Danial Zafaranchizadeh M.** | AI Engineer \| Robotics Researcher | [Profile](https://www.linkedin.com/in/danial-za/) |

Brought to you by **PARSAI** and the **School of Physics, Engineering and Computer Science, University of Hertfordshire**.

---

## 🎯 Five Progressive Sessions + Challenge

This repository contains five sessions that build from basic LLM interactions to a complete multi-agent meal planning system, plus a final challenge to evaluate your understanding.

### **Session 1: Hello LLM** 
Basic LLM interaction and conversation management

- `step1_hello_llm.py` - Your first LLM API call
- `step2_conversation.py` - Multi-turn conversations
- `step3_temperature.py` - Control output randomness
- `step4_chatbot.py` - Chatbot UI with Streamlit
- `step5_personas.py` - Prompt engineering & personas

**Run:**
```bash
cd session1
python steps/step1_hello_llm.py
```

---

### **Session 2: Robotics Agent**
AI agents with external tools and MCP server integration

- `robotics_mcp_server.py` - MCP server with robotics tools
- `robotics_agent.py` - Agent that searches & uses tools
- `robotics_data/` - Sensor, actuator, and component databases

**Features:**
- Tool-based architecture for robotics problems
- Agentic loop with reasoning
- MCP protocol implementation

**Run:**
```bash
cd session2
python steps/step3_run_agent.py
```

---

### **Session 3: RAG System**
Retrieval-Augmented Generation for knowledge-based AI

- `rag_demo.py` - Core RAG implementation
- `rag_streamlit.py` - Interactive RAG UI

**Learn:**
- Document indexing and search
- Grounding AI responses in real data
- RAG architecture patterns

**Run:**
```bash
cd session3
streamlit run rag_streamlit.py
```

---

### **Session 4: Recipe Agent**
Multi-tool agent for recipe and meal planning

- `recipe_mcp_server.py` - MCP server with recipe tools
- `recipe_agent.py` - Agent for recipe analysis
- Domain-specific tool orchestration

**Run:**
```bash
cd session4
python steps/step3_run_agent.py
```

---

### **Session 5: Budget Meal Planner** ⭐
Complete system with UI, budget optimization, and reasoning

**Features:**
- 🍽️ AI-powered meal planning within budget
- 💰 Cost vs nutrition optimization
- 🧠 Transparent agent reasoning
- 🎨 User-friendly Streamlit interface
- 📊 Multiple meal suggestions

**Files:**
- `app.py` - Main Streamlit UI
- `budget_meal_planner.py` - MCP server with 10-dish database
- `meal_planning_agent.py` - Agent logic with reasoning
- `llm_client.py` - LLM integration

**Try it:**
```bash
cd session5
streamlit run app.py
```

Then set budget, people count, dietary preferences, and click "Find Best Meals".

---

### **The Challenge** 🏆
Evaluate an AI agent's ability to balance multiple constraints and provide clear reasoning.

**Location:** `challenge/`

**Two Evaluation Prompts:**

1. **PROMPT 1 - Budget-focused 💰**
   - "I have £12 for two people. We need a high-protein meal. Design a robot to cook it."

2. **PROMPT 2 - Nutrition-focused 🥗**
   - "£20 budget, two people. One person is vegetarian. Plan a balanced meal + robot."

**Judging Criteria (100 points):**
- ✅ **Balance Quality (35%)** - Cost vs nutrition optimization
- ✅ **Reasoning (25%)** - Clear decision explanation
- ✅ **UI & Usability (20%)** - Non-coder friendly
- ✅ **Code Quality (20%)** - Clean, documented code

**Run:**
```bash
cd challenge
streamlit run app.py
```

Select each prompt, generate output, copy both prompt and response for submission.

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/vishnu0529/FromPromptsToAgents.git
cd FromPromptsToAgents

# Set up Python environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Start with Session 5 (complete system)
cd session5
pip install -r requirements.txt
streamlit run app.py
```

Visit `http://localhost:8501` and try the meal planner!

---

## 📁 Repository Structure

```
FromPromptsToAgents/
├── README.md
├── pyproject.toml
├── streamlit_app.py
│
├── session1/                    # Basic LLM (5 steps)
│   ├── llm_client.py
│   ├── requirements.txt
│   └── steps/
│       ├── step1_hello_llm.py
│       ├── step2_conversation.py
│       ├── step3_temperature.py
│       ├── step4_chatbot.py
│       └── step5_personas.py
│
├── session2/                    # Robotics Agent + MCP
│   ├── llm_client.py
│   ├── robotics_agent.py
│   ├── robotics_mcp_server.py
│   ├── test_server.py
│   ├── requirements.txt
│   ├── robotics_data/
│   │   ├── sensors.json
│   │   ├── actuators.json
│   │   └── components.json
│   └── steps/
│       ├── step1_explore_data.py
│       ├── step2_test_tools.py
│       └── step3_run_agent.py
│
├── session3/                    # RAG System
│   ├── llm_client.py
│   ├── rag_demo.py
│   ├── rag_streamlit.py
│   └── requirements.txt
│
├── session4/                    # Recipe Agent
│   ├── llm_client.py
│   ├── recipe_agent.py
│   ├── recipe_mcp_server.py
│   ├── test_server.py
│   ├── requirements.txt
│   └── steps/
│       ├── step1_explore_dishes.py
│       ├── step2_test_tools.py
│       └── step3_run_agent.py
│
├── session5/                    # Budget Meal Planner (Final)
│   ├── app.py                   # Main UI
│   ├── budget_meal_planner.py   # MCP Server
│   ├── meal_planning_agent.py   # Agent Logic
│   ├── llm_client.py
│   ├── requirements.txt
│   └── .env.example
│
└── challenge/                   # Challenge Submission
    └── app.py                   # Two-prompt evaluator
```

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.9+
- macOS, Linux, or Windows
- 2GB RAM
- Internet connection

### Installation Steps

1. **Clone repository:**
   ```bash
   git clone https://github.com/vishnu0529/FromPromptsToAgents.git
   cd FromPromptsToAgents
   ```

2. **Create virtual environment:**
```bash
python -m venv venv

# On Linux / macOS:
source venv/bin/activate

# On Windows (Command Prompt):
venv\Scripts\activate.bat

# On Windows (PowerShell):
venv\Scripts\Activate.ps1
```

Your prompt will show `(venv)` when active.

3. **Install dependencies:**
   ```bash
   cd session5
   pip install -r requirements.txt
   ```

---

## 🔑 LLM Backend Configuration

This workshop supports multiple LLM backends. Create a `.env` file in each session directory:

### Option 1: Local University LLM (Recommended)

```env
LLM_SERVICE_URL=https://uhhpc.herts.ac.uk/qwen
LLM_API_TOKEN=<token-provided-by-instructor>
```

### Option 2: Google Gemini (Free)

---

## How to Follow Along — Step by Step

Each session has a `steps/` folder with numbered files. **Run them in order:**

### Session 1 : Building Blocks
```bash
cd session1
pip install -r requirements.txt
cp .env.example .env        # Edit with your keys

python steps/step1_hello_llm.py          # Your first LLM call
python steps/step2_conversation.py       # Multi-turn chat
python steps/step3_temperature.py        # Temperature comparison
streamlit run steps/step4_chatbot.py     # Build a chatbot UI
streamlit run steps/step5_personas.py    # Prompt engineering
```

### Session 2 : MCP & Robotics Agent
```bash
cd session2
pip install -r requirements.txt
cp .env.example .env

python steps/step1_explore_data.py       # Browse the parts database
python steps/step2_test_tools.py         # Test MCP tools directly
python steps/step3_run_agent.py          # Run the full agent!
```

### Session 3 : RAG Concepts
```bash
cd session3
pip install -r requirements.txt
cp .env.example .env

python rag_demo.py                       # See RAG in action (demo only)
streamlit run rag_streamlit.py 
```

### Session 4 : Recipe Agent
```bash
cd session4
pip install -r requirements.txt
cp .env.example .env

python steps/step1_explore_dishes.py     # Browse the recipe database
python steps/step2_test_tools.py         # Test recipe tools
python steps/step3_run_agent.py          # Run the recipe agent
```

### Session 5 : A2A
```bash
cd session5
pip install -r requirements.txt
cp .env.example .env

streamlit run app.py                     # Run the full platform!
```
---

## Prerequisites

- Python 3.10+
- A Google account (for Gemini API key)
- A code editor (VS Code recommended)
- A GitHub account (for challenge submission)

---

## Troubleshooting

**"No LLM backend available"**
→ Check your `.env` file has either a working `LLM_API_TOKEN` or `GEMINI_API_KEY`.

**"ModuleNotFoundError"**
→ Make sure you ran `pip install -r requirements.txt` in the current session folder.

**Gemini 429 Too Many Requests**
→ The shared workshop key is rate-limited. You must get your own free key:
1. Go to **https://aistudio.google.com** → sign in → click **"Get API Key"**
2. Click **"Create API key"** → copy it
3. Open your `.env` file and replace the existing value: `GEMINI_API_KEY=your-new-key`

**Gemini returns another error**
→ Check your API key at https://aistudio.google.com. The free tier has rate limits (15 requests/minute).

**Streamlit text box not accepting keyboard input**
→ Run `streamlit run` from a **standalone terminal**, not from inside PyCharm or VS Code. IDE-embedded terminals keep keyboard focus and intercept your keystrokes.

**Local service not reachable**
→ Check your `LLM_SERVICE_URL` and `LLM_API_TOKEN` in `.env`. Try `curl https://uhhpc.herts.ac.uk/qwen/health` to verify the service is up.

---

## Community & Communication

Join our Discord to ask questions, share progress, and connect with other participants:

**Discord:** https://discord.gg/UGsfhZq3

---

**The Workshop Team — PARSAI**
School of Physics, Engineering and Computer Science | University of Hertfordshire
