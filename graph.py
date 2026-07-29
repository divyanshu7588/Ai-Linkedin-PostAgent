from langgraph.graph import StateGraph, START, END

from state import LinkedInState
from agents.writer import writer

builder = StateGraph(LinkedInState)

builder.add_node("writer", writer)

builder.add_edge(START, "writer")
builder.add_edge("writer", END)

graph = builder.compile()