from fastapi import APIRouter
from app.schemas.graph import GraphRequest, PathResult
from app.services.graph import shortest_path

router = APIRouter()

@router.post('/кратчайший-путь/', response_model=PathResult)
def find_shortest_path(request: GraphRequest):
    graph_dict = {
        'nodes': request.nodes,
        'edges': [{'start': edge.start, 'end': edge.end, 'weight': edge.weight} for edge in request.edges]}

    answer = shortest_path(graph_dict, request.start, request.end)

    return answer