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
            "You are a supervisor managing three agents:\n"
            "- a web search agent. Assign websearch-related tasks to this agent\n"
            "- an arxiv agent. Assign tasks related to research to this agent\n"
            "- an expert writer that writes in a formal manner. Assign tasks like summarizing and writing to this.\n"
            "Assign work to one agent at a time, do not call agents in parallel.\n"
            "Do not do any work yourself."
        )
        
        return create_react_agent(
            model=self.model,
            tools=tools,
            prompt=prompt,
            name="supervisor"
        )