from langgraph.prebuilt import create_react_agent

class WriterAgent:
    def __init__(self, model="openai:gpt-4.1"):
        self.model = model
        
    def create_agent(self):
        return create_react_agent(
            model=self.model,
            tools=[],
            prompt=(
                "You are an expert report writer. Your role is to synthesize the information provided in the conversation history from the other agents.\n"
                "Review the research from the Web Search Agent and the Arxiv Agent, then write a comprehensive, well-structured report that addresses the original user request.\n"
                "Do not perform any research yourself; only use the provided information.\n"
                "\n"
                "FORMAT:\n"
                "Respond in Markdown using the following structure:\n"
                "# Title\n"
                "A clear, descriptive title for the report.\n"
                "\n"
                "## Contents\n"
                "A detailed, well-organized synthesis of the findings, written in formal language.\n"
                "\n"
                "## Limitations\n"
                "Briefly discuss any limitations, uncertainties, or gaps in the information provided.\n"
                "\n"
                "## References\n"
                "List all sources referenced in the report, including links, arXiv IDs, or other identifiers as appropriate.\n"
            ),
            name="writer_agent"
        )