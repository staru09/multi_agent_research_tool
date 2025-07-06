from agents.arxiv_agent import ArxivAgent
from agents.web_search_agent import WebSearchAgent
from agents.writer_agent import WriterAgent
from utils.message_utils import pretty_print_messages
from utils.config_utils import setup_environment
from typing import Annotated
from langchain_core.tools import tool
from langgraph.prebuilt import InjectedState
from langgraph.graph import StateGraph, START, MessagesState, END
from langgraph.types import Command
from langchain_core.messages import HumanMessage
from graph.multi_agent_graph import MultiAgentGraph
from agents.supervisor_agent import SupervisorAgent
from dotenv import load_dotenv
load_dotenv()
import os

def main():
    setup_environment()
    
    # Initialize agents
    web_agent = WebSearchAgent().create_agent()
    arxiv_agent = ArxivAgent().create_agent()
    writer_agent = WriterAgent().create_agent()
    
    # Create supervisor
    supervisor = SupervisorAgent(
        agents=[web_agent, arxiv_agent, writer_agent]
    ).create_agent()
    
    # Build multi-agent graph
    agent_graph = MultiAgentGraph(
        agents={
            "web_search_agent": web_agent,
            "arxiv_agent": arxiv_agent,
            "writer_agent": writer_agent,
            "supervisor": supervisor
        }
    )
    agent_graph.build_graph()
    compiled_graph = agent_graph.compile()
    
    # Sample queries
    queries = [
        "Find upcoming AI conferences in USA. What are the latest papers on arxiv related to image dehazing?",
        "What are dates of NeurIPS 2025 and Name the title of the latest paper by sergey levine?"
    ]
    
    # Process each query
    for query in queries:
        print(f"\n{'='*50}")
        print(f"Processing query: {query}")
        print(f"{'='*50}\n")
        
        # Prepare input state
        input_state = {
            "messages": [HumanMessage(content=query)]
        }
        
        # Stream and process results
        for chunk in compiled_graph.stream(input_state):
            pretty_print_messages(chunk, last_message=True)
        
        print("\n" + "-"*80 + "\n")

if __name__ == "__main__":
    main()