from heapq import heappop, heappush
from math import inf

# creates basic directional graph
graph = {
    'A': [('B', 10), ('C', 3)],
    'C': [('D', 2)],
    'D': [('E', 10)],
    'E': [('A', 7)],
    'B': [('C', 3), ('D', 2)],
    'F': [('E', 1)]
}


def dijkstras(graph, start):
    # creates dictionary where every vertex with its travel value will be stored
    distances = {}
    # sets all distances to infinity
    for vertex in graph:
        distances[vertex] = inf
    # overwrites distance from starting vertex from infinity to 0
    distances[start] = 0
    # start vertex for while loop
    vertices_to_explore = [(0, start)]
    # runs as long there are vertices to explor
    while vertices_to_explore:
        # pops from vertices_to_explore and sets the current distance and vertex to a variable
        current_distance, current_vertex = heappop(vertices_to_explore)
        # iterates through a vertex's connections neighbors with the weight between them
        for neighbor, edge_weight in graph[current_vertex]:
            # sets new distance based on path already traveled + new pathway
            new_distance = current_distance + edge_weight
            # if the new distance is shorter than the current distance it is replaced and calls heappush
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(vertices_to_explore, (new_distance, neighbor))

    return start, distances


distances_from_d = dijkstras(graph, 'D')
distances_from_a = dijkstras(graph, 'A')
distances_from_f = dijkstras(graph, 'F')

print("\nShortest distances from {0}: {1}".format(distances_from_d[0], distances_from_d[1]))
print("\nShortest distances from {0}: {1}".format(distances_from_a[0], distances_from_a[1]))
print("\nWith A as starting point:")
for key, item in distances_from_a[1].items():
    print("from " + distances_from_a[0] + " to " + key + " - " + str(item))
print("\nShortest distances from {0}: {1}".format(distances_from_f[0], distances_from_f[1]))

