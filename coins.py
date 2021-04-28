#note: denominations is S, and 
def find_coins(denominations, change):
    memo = [float('inf') for i in range(change+1)]
    backtrack = [0 for i in range(change+1)]
    backtrack[0] = 0
    backtrack[1]=1

    #O(k) here, dominated by O(nk)
    for d in denominations:
        memo[d] = 1
    
    #nested for loop O(nk)
    #n part
    for i in range(1,change+1):
        #k part
        for d in denominations:
            if i - d < 1: continue #case where we get negative index

            #pick the optimal coin to add to get to change n
            elif memo[i-d] + 1 < memo[i]:
                memo[i] = memo[i-d] + 1 
                backtrack[i] = d
    coins = []
    index = change

    #O(n) backtrack dominated by O(nk)
    while backtrack[index] != 0:
        coins.append(backtrack[index])
        new_index = index - backtrack[index]
        index = new_index
    coins.append(index)
    
    return memo[change],coins

print(find_coins([1,10,25], 30))
print(find_coins([1,10,25], 31))
print(find_coins([1,10,25], 36))


