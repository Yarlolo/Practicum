from pydantic import BaseModel
from typing import List
class Edge(BaseModel):
    start: int
    end: int
    weight: float
class GraphRequest(BaseModel):
    nodes: List[int]
    edges: List[Edge]
    start: int
    end: int
class PathResult(BaseModel):
    path: List[int]
    total_distance: float