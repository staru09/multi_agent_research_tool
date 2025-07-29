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
from langchain_core.messages import HumanMessage,AIMessage
from graph.multi_agent_graph import MultiAgentGraph
from agents.supervisor_agent import SupervisorAgent
from dotenv import load_dotenv
load_dotenv()

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
    
    chat_history = []  # Store chat history as list of (role, message)

    # Interactive chat loop
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break

        chat_history.append(("user", query))  # Save user message

        print(f"\n{'='*50}")
        print(f"Processing query: {query}")
        print(f"{ '='*50}\n")

        # Build message objects from chat history for context
        messages = []
        for role, msg in chat_history:
            if role == "user":
                messages.append(HumanMessage(content=msg))
            elif role == "agent":
                messages.append(AIMessage(content=msg))

        # Prepare input state with full context
        input_state = {
            "messages": messages
        }

        # Stream and gather the agent's response
        agent_response_fragments = []  # Accumulate partial responses
        for chunk in compiled_graph.stream(input_state):
            pretty_print_messages(chunk, last_message=True)
            if "messages" in chunk and chunk["messages"]:
                # append all chunked messages
                for m in chunk["messages"]:
                    if m.content:
                        agent_response_fragments.append(m.content)

        # Combine partial responses into one
        final_agent_message = "\n".join(agent_response_fragments).strip()

        if final_agent_message:
            chat_history.append(("agent", final_agent_message))

        print("\n" + "-"*80 + "\n")

    # After chat loop, offer to export chat
    export = input("Do you want to export the chat history? (y/n): ").strip().lower()
    if export == "y":
        filename = input("Enter filename to save chat (e.g., chat_history.txt): ").strip()
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for role, line in chat_history:
                    prefix = "You:" if role == "user" else "Agent:"
                    f.write(f"{prefix} {line}\n\n")
            print(f"Chat history exported to {filename}")
        except Exception as e:
            print(f"Failed to export chat: {e}")

if __name__ == "__main__":
    main()