import math
d = 7
N = [0,0,0,1]
i = len(N) -1
val = 0


Q = [0,0,0,0]
r = 0



while i >= 0:
    val+=N[i]
    Q[i] = math.floor(val/d)
    val = (val -  Q[i] * d) * 10
    i -= 1
print()
print(val/10)
print(Q)

# temp = 0

# bottom = 0
# top = N[0]
# while i <= len(N):
#     Q[i-1] = math.floor(top/d)
#     # Q.append(math.floor(top/d))
#     bottom = math.floor(top/d) * d
#     if i != len(N):
#         top = ((top - bottom) * 10) + N[i]
#     i += 1

# print(top,bottom)
# print(Q)


