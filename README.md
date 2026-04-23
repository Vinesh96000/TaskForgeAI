# ⚡ TaskForge AI: Multi-Agent Autonomous Operations System

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![CrewAI](https://img.shields.io/badge/CrewAI-Orchestration-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## 📌 Executive Summary
TaskForge AI is a premium, multi-agent generative AI system designed to autonomously deconstruct, research, and execute highly complex user objectives. Moving beyond traditional single-prompt chatbots, this system utilizes an assembly-line architecture of specialized AI agents with distinct roles, real-time web access, and contextual memory to deliver consultant-grade deliverables.

## 🏗️ System Architecture
The application is built on a modular, highly scalable foundation:
* **Orchestration Engine:** [CrewAI](https://github.com/joaomdmoura/crewAI) to manage sequential task delegation and agent communication.
* **Intelligence Layer:** OpenAI GPT integration for advanced logical reasoning and synthesis.
* **Tooling & Live Data:** Autonomous Web Scraping integrations, allowing agents to bypass training data cutoffs and fetch real-time market insights.
* **Memory Layer:** Integrated vector memory (FAISS) to retain contextual awareness across complex tasks.
* **Interface:** An ultra-minimal, responsive Streamlit dashboard designed for a frictionless user experience.

## 🤖 The Autonomous Squad
1.  **Lead Strategist:** Acts as the system architect. Parses complex user prompts and generates a strict, logical, multi-point operational blueprint.
2.  **Autonomous Researcher:** The data-gathering engine. Equipped with live web-scraping tools to autonomously hunt for empirical data, industry trends, and factual evidence required by the blueprint.
3.  **Execution Specialist:** The synthesizer. Merges the initial strategy with the raw research dossier to author a final, polished, highly professional deliverable.

## 🚀 Quick Start / Local Deployment
To run this autonomous operations system locally:

**1. Clone the repository and navigate to the directory:**
```bash
git clone [https://github.com/YOUR_USERNAME/TaskForgeAI.git](https://github.com/YOUR_USERNAME/TaskForgeAI.git)
cd TaskForgeAI
```

**2. Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Environment Variables:**
Create a `.env` file in the root directory and add your API key:
```env
OPENAI_API_KEY=your_api_key_here
```

**5. Initialize the Engine:**
```bash
streamlit run app.py
```

## 🧠 Engineering Philosophy
This project was designed with a focus on **separation of concerns** and **agentic design patterns**. By strictly isolating the planning, research, and execution phases, the system significantly reduces LLM hallucination and produces outputs grounded in real-time, verifiable data.