from langgraph.prebuilt import create_react_agent
from tools.arxiv_tools import ArxivTools

class ArxivAgent:
    def __init__(self, model="openai:gpt-4.1"):
        self.model = model
        self.tools = ArxivTools().get_tools()
        
    def create_agent(self):
        return create_react_agent(
            model=self.model,
            tools=self.tools,
            prompt=(
                "You are an expert research agent.\n\n"
                "INSTRUCTIONS:\n"
                "- Assist ONLY with research related tasks\n"
                "- After you're done with your tasks, respond to the supervisor directly\n"
                "- Respond ONLY with the results of your work, do NOT include ANY other text."
            ),
            name="arxiv_agent"
        )