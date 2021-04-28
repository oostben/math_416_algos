
import random
# This is a function I made for debugging/testing
def test(test_number, hotels, correct_seq, correct_cost):
   sequence_out, cost_out = optimal_sequence(hotels)
   failed = False
   print("---------", "TEST #", test_number, "---------")
   print("sequence:", sequence_out)
   print("cost:", cost_out)
   if correct_seq != sequence_out:
       print("INCORRECT SEQUENCE")
       print("correct:", correct_seq)
       print("output:", sequence_out)
       failed = True
   if correct_cost != cost_out:
       print("INCORRECT COST")
       print("correct:", correct_cost)
       print("output:", cost_out)
       failed = True
   if failed: print(test_number, "FAILED")
   else: print(test_number, "PASSED")
   print()
 
# This is the actual important function that determines optimal sequence of hotels at which to stop
def optimal_sequence(hotels):
   # if there are no hotels passed in then we return an empty sequence and a cost of zero
   if len(hotels) == 0: return ([],0)
 
   # if there is only one hotel passed in, we only have one option: drive to that hotel in one go, and accept the loss
   if len(hotels) == 1: return ([1],(200-hotels[0])**2)
 
   # backtrack is used to store the optimal path
   # basically backtrack[i] is stores the previous hotel in the optimal journey to said hotel
   # we also treat the 0 mile marker as a sort of zero hotel, which is why we add the first zero in the initialization
   # we also know that the optimal path to get from zero mile marker to the first hotel is to simply go from the zero mile
   # marker to the first hotel, so we add a second zero to the initialization to symbolize that the optimal path to the first
   # hotel is from 0 mile marker
   # because we deal with the 0 and 1 hotel case above we then start considering hotel 2 as you'll see below
   backtrack = [0,0]
 
   # memo is our memoization array
   # memo[i] stores the cost of the lowest cost path from 0 mile marker to hotel i
   # because we start at hotel 2 we need to add hotel 0, which has a cost of zero, and hotel 1
   # which has a cost of (200-hotels[0])**2. It is optimal because there is only 1 path from zero mile marker to hotel 1
   memo = [0,(200-hotels[0])**2]
 
   # here we add the zero mile marker into to the hotels passed in at index zero
   # this is mainly just so that the indexes line up hotel i is at hotels[i], not hotels[i-1]
   hotels.insert(0,0)
 
   # this for loop considers each hotel and computes the minimal cost to get from zero mile marker to that hotel and stores it in memo
   # it starts at hotel 2 because we've already considered hotel 1, and added appropriate values to the data structures
   for i in range(2,len(hotels)):
       # here we compute the minimal cost to get to hotel i
 
       # we initialize the min cost to infinity so that any cost we find will be less than the starting value of min cost
       min_cost = float('inf')
 
       # min index starts out as negative one, it will be overwritten later
       min_index = -1
 
       # here is the secret sauce of the algorithm
       # to find the lowest cost of hotel i we consider going from hotel j (all the previous hotels) and then to hotel i
       # we take the minimal cost path of these paths
       # but how do we know the minimal path
       # well we've already computed the minimal cost of all the previous hotels, so the minimal cost to get to hotel i
       # using hotel j is the minimal cost it takes to get to hotel j plus the cost to get from hotel j to i in one go
       # it's also worth noting that we inserted zero mile marker into hotels so we are also factoring in the possibility of
       # going from zero mile marker to hotel i (which is why the loop starts at zero)
       for j in range(0,i):
           # here we compute the cost of going from zero to hotel j with minimal cost from memo plus the cost of going from hotel j to i
           temp_cost = memo[j] + (200 - (hotels[i]- hotels[j]))**2
           # if this cost is the lowest we've seen we save it
           # note we also need to save the index of hotel j to backtrack
           if temp_cost < min_cost:
               min_cost = temp_cost
               min_index = j
       # append the new cost to memo and add the backtracking info to backtracking
       backtrack.append(min_index)
       memo.append(min_cost)
   # this is the sequence we will be returning
   sequence = []
   # this is the index variable we will be using to traverse back through the path, it starts out as the last hotel
   index = len(hotels) - 1
   # while we are not back at the zero marker
   while (index != 0):
       # add the index to the sequence, we add it at the start because we are traversing the path backwards
       sequence.insert(0,index)
       index = backtrack[index]
   # we return the sequence and the minimal cost to the last hotel
   return sequence, memo[-1]
 
# these are the small tests I wrote to make sure it works
test(0,[],[],0)
test(1,[100,200],[2],0)
test(2,[125],[1],75**2)
test(3,[50,100,225],[3],25**2)
test(4,[120,170,220,295],[2, 4],(30**2 + (200-125)**2))
# temp = [random.randint(1,1000) for x in range(10)]
# temp.sort()
# test(5,temp,[],0)
# print(temp)
