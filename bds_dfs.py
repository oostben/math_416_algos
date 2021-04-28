p1 = [2,4,6]
p2 = [1,3,7,8]
p3 = [2,4,5,6]
p4 = [1,3]
p5 = [3,8]
p6 = [1,3,7]
p7 = [2,6]
p8 = [2,5]

graph1 = [p1,p2,p3,p4,p5,p6,p7,p8]

print(graph1)
for p in range(len(graph1)):
    print(p)
    for e in range(len(graph1[p])):
        graph1[p][e] -=1

print(graph1)

found = [False for i in range(len(graph1))]
# found[0] = True

q = [0]
k = 0
# while len(q) != 0:
#     curr = q.pop(-1)
#     print(curr + 1)
#     # if curr == -1:
#     #     print(curr, "layer: ", k)
#     #     k +=1

#     if found[curr]: print("error")
#     else: found[curr] = True
#     for i in range(len(graph1[curr])):
#         if not found[graph1[curr][i]] and graph1[curr][i] not in q:
#             print("edge", curr +1, "--", graph1[curr][i] + 1)
#             q.append(graph1[curr][i])
#             break
#             # q.insert(0,graph1[curr][i])

def dfs(inner):
    found[inner] = True
    print("inner", inner +1)
    for i in range(len(graph1[inner])):
        if not found[graph1[inner][i]] and graph1[inner][i] not in q:
            print("edge", inner +1, "--", graph1[inner][i] + 1)
            dfs(graph1[inner][i])
dfs(0)