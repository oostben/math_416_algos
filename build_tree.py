class Graph:
    edges = []
    degree_sequence = []

def deg_sequence_done(graph):
    for deg_vertex in graph.degree_sequence:
        if deg_vertex != 0:
            return False
    return True

def minimize_a_vertex(graph):
    if deg_sequence_done(graph):
        print("ERROR: degree sequence empty and minimize_a_vertex called")
        return -1

    index_of_vertex_we_are_minimizing = 0
    while(graph.degree_sequence[index_of_vertex_we_are_minimizing] == 0) and index_of_vertex_we_are_minimizing < len(graph.degree_sequence):
        index_of_vertex_we_are_minimizing +=1

    index_of_other_vertex = index_of_vertex_we_are_minimizing + 1
    while(graph.degree_sequence[index_of_other_vertex] == 0): index_of_other_vertex+=1

    while(graph.degree_sequence[index_of_vertex_we_are_minimizing] > 0):
        print("v1:", index_of_vertex_we_are_minimizing,
            "v2:", index_of_other_vertex, "current degree sequence:", graph.degree_sequence)
        graph.edges.append((index_of_vertex_we_are_minimizing, index_of_other_vertex))
        graph.degree_sequence[index_of_vertex_we_are_minimizing] -= 1
        graph.degree_sequence[index_of_other_vertex] -= 1
        index_of_other_vertex += 1

def build_tree(degree_sequence_in):
    graph = Graph()
    graph.degree_sequence = sorted(degree_sequence_in,reverse = True)
    print(graph.degree_sequence)
    while not deg_sequence_done(graph):
        minimize_a_vertex(graph)
    graph.edges.sort()
    print("EDGES:",graph.edges, "\n\n")
    return graph

test_deg_sequence_1 = [4,2,1,1,1,1]
build_tree(test_deg_sequence_1)
# output --> EDGES: [(0, 1), (0, 2), (0, 3), (0, 4), (1, 5)]

test_deg_sequence_2 = [1,1,4,1,1]
build_tree(test_deg_sequence_2)
# output --> EDGES: [(0, 1), (0, 1), (0, 2), (0, 2), (0, 3), (0, 3), (0, 4), (0, 4), (1, 5)]

test_deg_sequence_3 = [4,3,3,3,3,2,1,1,1,1,1,1,1,1]
build_tree(test_deg_sequence_3)
# output --> EDGES: [(0, 1), (0, 1), (0, 1), (0, 2), (0, 2), (0, 2), (0, 3), (0, 3), (0, 3), (0, 4), 
# (0, 4), (0, 4), (1, 2), (1, 3), (1, 5), (2, 3), (4, 5), (4, 6), (5, 7), (8, 9), (10, 11), (12, 13)]
