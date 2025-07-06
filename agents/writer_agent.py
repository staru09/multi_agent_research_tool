from langgraph.prebuilt import create_react_agent

class WriterAgent:
    def __init__(self, model="openai:gpt-4.1"):
        self.model = model
        
    def create_agent(self):
        return create_react_agent(
            model=self.model,
            tools=[],
            prompt=(
                "You are an expert report writer. Your role is to synthesize the information provided in the conversation history from the other agents. "
                "Review the research from the Web Search Agent and the Arxiv Agent, then write a comprehensive, well-structured report that addresses the original user request. "
                "Do not perform any research yourself; only use the provided information."
            ),
            name="writer_agent"
        )