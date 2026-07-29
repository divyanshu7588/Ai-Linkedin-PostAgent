from langgraph.graph import StateGraph, START, END

from state import LinkedInState

from agents.writer import writer_agent
from agents.image import image_agent

builder = StateGraph(LinkedInState)
builder.add_node("writer", writer_agent)
builder.add_node("image", image_agent)

builder.add_edge(START, "writer")
builder.add_edge("writer", "image")
builder.add_edge("image", END)
graph = builder.compile()