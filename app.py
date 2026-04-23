import os
import streamlit as st
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool

# 1. Open the safe
load_dotenv()

# --- 🎨 UI CONFIGURATION (Ultra-Minimal & Premium) ---
st.set_page_config(page_title="TaskForge AI | Operations System", page_icon="⚡", layout="wide")

# --- 🗄️ SIDEBAR: TECH STACK & ARCHITECTURE ---
with st.sidebar:
    st.markdown("### ⚡ TaskForge AI Engine")
    st.markdown("An advanced multi-agent autonomous operations system designed to handle complex, multi-step goals.")
    
    st.divider()
    
    st.markdown("#### 🛠️ System Architecture")
    st.markdown("""
    - **Orchestration:** CrewAI Framework
    - **Intelligence:** OpenAI GPT Models
    - **Interface:** Streamlit (Python)
    - **Memory Layer:** FAISS Vector Database
    - **Tooling:** Autonomous Web Scraping
    """)
    
    st.divider()
    
    st.markdown("#### 🤖 Agent Squad")
    with st.expander("1. Lead Strategist"):
        st.write("Deconstructs the user's prompt into a structured, actionable plan.")
    with st.expander("2. Autonomous Researcher"):
        st.write("Equipped with Web Scraping Tools to pull live, real-world data based on the Strategist's plan.")
    with st.expander("3. Execution Specialist"):
        st.write("Synthesizes all research and strategy into the final, polished output.")
        
    st.divider()
    st.success("🟢 System Online & Ready")

# --- 🖥️ MAIN DASHBOARD ---
st.title("TaskForge AI Operations Center")
st.markdown("Deploy a specialized squad of AI agents to autonomously research, plan, and execute your complex goals.")

# The input box for the user
user_goal = st.text_area(
    "Define your objective (The more complex, the better):", 
    placeholder="e.g., 'Analyze the current market landscape for AI in the healthcare sector and propose a 3-step business strategy.'",
    height=100
)

# The Execution Button
if st.button("🚀 Initialize Autonomous Agents", type="primary"):
    
    if not user_goal:
        st.warning("⚠️ Please define an objective before initializing the system.")
    else:
        # --- ⚙️ THE CREWAI FACTORY LOGIC ---
        
        # 1. The Tools
        web_tool = ScrapeWebsiteTool() # Left blank so the agent can search wherever it needs

        # 2. The Agents (Renamed for a professional context)
        strategist = Agent(
            role='Lead Strategist',
            goal='Break down the user objective into a clear, logical step-by-step blueprint.',
            backstory='You are a master systems thinker. You take complex user requests and turn them into highly organized blueprints.',
            verbose=True,
            allow_delegation=False
        )

        researcher = Agent(
            role='Autonomous Researcher',
            goal='Execute the Strategist\'s blueprint by finding the most accurate and up-to-date information.',
            backstory='You are a relentless data analyst. You use tools to scour the internet and extract high-value insights.',
            verbose=True,
            allow_delegation=False,
            tools=[web_tool]
        )

        executor = Agent(
            role='Execution Specialist',
            goal='Synthesize the strategy and research into a highly professional, final deliverable.',
            backstory='You are an elite technical synthesizer. You transform raw data and plans into actionable, premium-quality outputs.',
            verbose=True,
            allow_delegation=False
        )

        # 3. The Tasks (Dynamic based on user input)
        plan_task = Task(
            description=f'Analyze this objective: "{user_goal}". Create a detailed, multi-point strategy blueprint to achieve this.',
            expected_output='A structured strategic blueprint.',
            agent=strategist
        )

        research_task = Task(
            description='Take the strategic blueprint. Use your web tools to research necessary data, market trends, or facts required to fulfill the blueprint.',
            expected_output='A comprehensive dossier of research data.',
            agent=researcher
        )

        execute_task = Task(
            description='Take the strategic blueprint and the research dossier. Create the final, comprehensive response to the user\'s original objective.',
            expected_output='A high-quality, professional final output formatted cleanly in Markdown.',
            agent=executor
        )

        # 4. The Manager
        taskforge_crew = Crew(
            agents=[strategist, researcher, executor],
            tasks=[plan_task, research_task, execute_task],
            verbose=True,
            process=Process.sequential,
            memory=True
        )

        # --- 🎬 VISUAL EXECUTION ---
        # This creates a beautiful loading status box on the UI
        with st.status("🤖 **TaskForge Squad Deployed...**", expanded=True) as status:
            st.write("⚙️ Lead Strategist is formulating the blueprint...")
            st.write("🔍 Autonomous Researcher is gathering data...")
            st.write("✍️ Execution Specialist is synthesizing final output...")
            
            # Start the actual CrewAI work
            final_result = taskforge_crew.kickoff()
            
            status.update(label="✅ **Mission Accomplished!**", state="complete", expanded=False)
        
        # Display the result in a clean, professional way
        st.markdown("---")
        st.subheader("📊 Final Deliverable")
        st.markdown(final_result)