class Vertex:
    visited = False
    edges = []
    paths = 0
    def __init__(self, edges):
        self.edges = edges
        self.vistied = False
        self.paths = 0

# p0 = [1,2]
# p1 = [0,3]
# p2 = [0,3]
# p3 = [1,2]
#    1
#   / \
# 0    3
#  \  /
#   2

verts1 = [ Vertex([1,2]), Vertex([0,3]), Vertex([0,3]), Vertex([1,2]) ]


# p0 = [1,2]
# p1 = [0,2,3]
# p2 = [0,1,3]
# p3 = [1,2,4,5]
# p4 = [3,6]
# p5 = [3,6]
# p6 = [4,5]
#    1    4
#   / \  / \
# 0    3    6
#  \  / \  /
#   2    5

verts2 = [ Vertex([1,2]), Vertex([0,2,3]), Vertex([0,1,3]), Vertex([1,2,4,5]), Vertex([3,6]), Vertex([3,6]), Vertex([4,5]) ]

def find_number_of_shortest_paths(start_vert_idx, end_vert_idx, verts):
    if start_vert_idx == end_vert_idx: return 1 #assumes no parallel edges
    
    q = [start_vert_idx] #initalize queue
    verts[start_vert_idx].paths = 1 #initalize the # of paths to starting vertex to 1
    found_shortest_path = False
    num_shortest_paths = 0
    while len(q) != 0 and not found_shortest_path:
        num_nodes_to_explore = len(q)
        while num_nodes_to_explore > 0:
            num_nodes_to_explore -= 1
            cur_vert_idx = q.pop(0)
            if cur_vert_idx == end_vert_idx:
                found_shortest_path = True
                num_shortest_paths += 1
            if verts[cur_vert_idx].visited:
                verts[cur_vert_idx].paths += 1
            else:
                for vert_idx in verts[cur_vert_idx].edges:
                    q.append(vert_idx)
                    verts[vert_idx].paths = verts[cur_vert_idx].paths
                verts[vert_idx].vistied = True
    return num_shortest_paths

print(find_number_of_shortest_paths(0,3,verts1)) #prints --> 2
print(find_number_of_shortest_paths(0,6,verts2)) #prints --> 4