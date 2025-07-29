from tools.handoff_tool import create_handoff_tool
from langgraph.prebuilt import create_react_agent

class SupervisorAgent:
    def __init__(self, model="openai:gpt-4.1", agents=[]):
        """
        Supervisor agent that coordinates between multiple specialized agents.
        
        Args:
            model: The language model to use
            agents: List of agents to manage
        """
        self.model = model
        self.agents = agents
        
    def create_agent(self):
        """
        Creates the supervisor agent with handoff tools for each subordinate agent.
        
        Returns:
            Configured supervisor agent
        """
        tools = []
        for agent in self.agents:
            tools.append(create_handoff_tool(
                agent_name=agent.name,
                description=f"Assign task to {agent.name} agent."
            ))
        
        prompt = (
            "You are the SupervisorAgent, responsible for efficiently managing and delegating tasks among three specialized agents:\n"
            "\n"
            "1. Web Search Agent: Handles all tasks involving real-time web searches, current events, or information retrieval from the internet.\n"
            "2. Arxiv Agent: Handles all academic research tasks, including searching for, summarizing, or extracting information from scientific papers and arXiv.\n"
            "3. Expert Writer Agent: Handles tasks requiring formal writing, summarization, report generation, or synthesis of information into well-structured text.\n"
            "\n"
            "INSTRUCTIONS:\n"
            "- Carefully analyze each incoming task and assign it to the most appropriate agent based on their specialization.\n"
            "- Assign work to only one agent at a time. Do NOT assign tasks in parallel or split a single task among multiple agents.\n"
            "- Do NOT attempt to solve or answer any tasks yourself. Your sole responsibility is delegation and coordination.\n"
            "- If a task does not fit any agent, respond: 'No suitable agent available for this task.'\n"
            "- Communicate clearly and concisely with agents, providing all necessary context for them to complete their tasks.\n"
            "- After an agent completes a task, review the result and determine if further delegation is needed.\n"
            "- Maintain a professional and neutral tone at all times.\n"
        )
        
        return create_react_agent(
            model=self.model,
            tools=tools,
            prompt=prompt,
            name="supervisor"
        )