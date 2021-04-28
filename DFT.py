import numpy as np
from fractions import Fraction

def DFT(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, x)

sizer = 9
input_lists = [[] for i in range(sizer)]
for i in range(sizer):
    for j in range(i):
        input_lists[i].append(1/(3.0**j))


for idx,liz in enumerate(input_lists):
    print("\n----" , idx,"----")
    print(liz)
    print("------------")
    print(DFT(liz),"\n")
