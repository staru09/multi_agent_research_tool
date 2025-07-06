from langchain_community.tools import DuckDuckGoSearchResults
from langgraph.prebuilt import create_react_agent

class WebSearchAgent:
    def __init__(self, model="openai:gpt-4.1"):
        self.model = model
        self.tools = [DuckDuckGoSearchResults(output_format="list")]
        
    def create_agent(self):
        return create_react_agent(
            model=self.model,
            tools=self.tools,
            prompt=(
                "You are a web_search agent.\n\n"
                "INSTRUCTIONS:\n"
                "- Assist ONLY with web search related tasks.\n"
                "- After you're done with your tasks, respond to the supervisor directly\n"
                "- Respond ONLY with the results of your work, do NOT include ANY other text."
            ),
            name="web_search_agent"
        )