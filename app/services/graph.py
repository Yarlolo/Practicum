import heapq

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)

        if node not in seen:
            seen.add(node)
            path = path + [node]

            if node == end:
                return (path, cost)

            for neig, c in graph.get(node, {}).items():
                heapq.heappush(queue, (cost + c, neig, path))

    return float('inf'), []

def shortest_path(graph: dict, start: int, end: int):
    graph_dict = {}

    for edge in graph['edges']:
        if edge['start'] not in graph_dict:
            graph_dict[edge['start']] = {}

        graph_dict[edge['start']][edge['end']] = edge['weight']
    path, total_distance = dijkstra(graph_dict, start, end)

    return {'path': path, 'total_distance': total_distance}