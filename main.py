from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    heap = [(0, 0, source)]

    shortest_path_info = {}

    while heap:
        dist, edges, node = heappop(heap)

        if node in shortest_path_info:
            continue

        shortest_path_info[node] = (dist, edges)

        for neighbor, weight in graph.get(node, []):
            if neighbor not in shortest_path_info:
                heappush(heap, (dist + weight, edges + 1, neighbor))

    return shortest_path_info

    

    

def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of
      that vertex in the shortest path tree.
    """
    ###TODO
    parents = {source: None}
    queue = deque([source])

    while queue:
        curr = queue.popleft()
        for neighbor in graph.get(curr, set()):
            if neighbor not in parents:
                parents[neighbor] = curr
                queue.append(neighbor)

    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }



def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    path = []
    curr = destination

    while curr in parents and parents[curr] is not None:
        path.append(parents[curr])
        current = parents[curr]

    return ''.join(reversed(path))

