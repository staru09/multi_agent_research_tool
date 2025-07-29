from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_core.messages import AIMessage

class MultiAgentGraph:
    def __init__(self, agents):
        """
        Multi-agent graph that coordinates workflow between agents
        
        Args:
            agents: Dictionary of agent names to agent functions
        """
        self.agents = agents
        self.graph = StateGraph(MessagesState)
        
    def build_graph(self):
        """Builds the execution graph with all agents"""
        # Add all agent nodes
        for name, agent in self.agents.items():
            self.graph.add_node(name, agent)
        
        # Define edges between agents
        self.graph.add_edge("web_search_agent", "supervisor")
        self.graph.add_edge("arxiv_agent", "supervisor")
        self.graph.add_edge("writer_agent", "supervisor")
        
        # Set entry point
        self.graph.add_edge(START, "supervisor")
        
        # Set conditional edges from supervisor
        self.graph.add_conditional_edges(
            "supervisor",
            self.decide_next,
            {
                "web_search_agent": "web_search_agent",
                "arxiv_agent": "arxiv_agent",
                "writer_agent": "writer_agent",
                "end": END
            }
        )
        
    def decide_next(self, state: MessagesState) -> str:
        """
        Determines next agent based on supervisor's tool call
        
        Args:
            state: Current conversation state
            
        Returns:
            Name of next agent or 'end' to terminate
        """
        last_message = state["messages"][-1]
        
        if isinstance(last_message, AIMessage) and last_message.tool_calls:
            tool_name = last_message.tool_calls[0]["name"]
            return tool_name.replace("transfer_to_", "")
        
        return "end"
    
    def compile(self):
        """Compiles the execution graph"""
        return self.graph.compile()