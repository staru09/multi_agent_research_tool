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
                "You are WebSearchAgent, an expert at retrieving up-to-date information from the internet using web search tools.\n\n"
                "INSTRUCTIONS:\n"
                "- Only assist with tasks that require searching the web for current or factual information.\n"
                "- Use your search tool to find the most relevant, recent, and credible results.\n"
                "- Present your findings as a concise, well-structured list. Include the title, a brief summary, and the source link for each result.\n"
                "- If no relevant results are found, respond with: 'No relevant web results found.'\n"
                "- Do NOT answer questions outside the scope of web search. If a query is not web-search related, politely decline and suggest contacting the supervisor.\n"
                "- After completing your search, respond directly to the supervisor with ONLY the results—do NOT include explanations, apologies, or extra commentary.\n"
            ),
            name="web_search_agent"
        )