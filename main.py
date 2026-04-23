import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool

# 1. Open the safe
load_dotenv()

# 2. EQUIP THE TOOLS (The Smart Glasses)
# We are giving the Researcher a tool to read a specific Wikipedia page about Marketing.
# You can change this URL to any website you want them to read!
web_reader_tool = ScrapeWebsiteTool(website_url='https://en.wikipedia.org/wiki/Marketing_operations')

# 3. HIRE THE TEAM (The Agents)
planner = Agent(
    role='Content Planner',
    goal='Plan an engaging outline for a short report.',
    backstory='You are a brilliant strategist who breaks down complex topics into easy-to-follow outlines.',
    verbose=True,
    allow_delegation=False
)

researcher = Agent(
    role='Research Analyst',
    goal='Find detailed, factual information based on a provided outline using the internet.',
    backstory='You are a relentless researcher who knows how to find the most accurate and interesting facts.',
    verbose=True,
    allow_delegation=False,
    tools=[web_reader_tool] # <--- WE GAVE THE TOOL TO THE RESEARCHER HERE!
)

writer = Agent(
    role='Senior Technical Writer',
    goal='Write a final, polished report using the provided research.',
    backstory='You are an expert writer. You take raw facts and turn them into beautiful, easy-to-read reports.',
    verbose=True,
    allow_delegation=False
)

# 4. WRITE THE ORDER TICKETS (The Tasks)
plan_task = Task(
    description='Create a 3-point outline for a short report on Marketing Operations.',
    expected_output='A clear, 3-point bulleted outline.',
    agent=planner
)

research_task = Task(
    description='Take the outline created by the Planner. Use your web_reader_tool to read the provided website and gather 2 specific facts for every point in the outline.',
    expected_output='A list of facts organized by the outline points.',
    agent=researcher
)

write_task = Task(
    description='Take the facts gathered by the Researcher and write a short, cohesive 3-paragraph report. Make it sound professional.',
    expected_output='A 3-paragraph report about Marketing Operations.',
    agent=writer
)

# 5. HIRE THE MANAGER AND ADD THE FILING CABINET
my_crew = Crew(
    agents=[planner, researcher, writer],
    tasks=[plan_task, research_task, write_task],
    verbose=True,
    process=Process.sequential,
    memory=True # <--- WE TURNED ON THE MEMORY FILING CABINET HERE!
)

# 6. START WORKING! 
if __name__ == "__main__":
    print("Manager: 'Assembly line starting! Remember to use your tools and check the filing cabinet.'\n")
    
    result = my_crew.kickoff()
    
    print("\n=== THE FINAL COMPLETED REPORT ===")
    print(result)