# this is a print fucntion I made to print the memo grid mainly for debugging
def print_memo(memo):
   print("Starting Print Memo")   
   print(" ", [i for i in range(len(memo))])
   for i in range(len(memo)):
       print(i,memo[i])
   print()
 
# this is a test funtion I wrote for testing
def test(number, sequence, correct):
   print("Test #", number)
   if (longest_palindromic_subsequence(sequence) != correct):
       print("Test Failed\n")
       return
   print("Test Passed\n")
 
# this is the important algorithm that actually computes the length of the longest palindromic subsequence
def longest_palindromic_subsequence(sequence):
   # this is just a variable I made to store the length of the sequence passed in so I didn't have to keep typing len(sequence)
   length = len(sequence)
 
   # if the length of the sequence is zero we return 0
   if length == 0: return 0
 
   # here we build the memoization table
   # basically how I interpret this table is memo[x][y] is the length of the longest subsequence contained within character y plus the next x characters
   # note the dimensions, its actually more like half a table with the bottom right diagonal cut off.  This is because if x plus y is greater than the
   # length of the sequence is is not valid
   # you could have a full square matrix but this cuts the amount of space used in half
   memo = [[0 for x in range(length-y)] for y in range(length)]
 
   # first off we initialize the top row of the matrix
   # basically the longest subsequence within character y plus zero is 1, a single character
   for i in range(length):
       memo[0][i] = 1
  
   # ok now this is where the actual algorithm is
   # we for loop through each character y considering the next y characters to find the longest subsequence contained within sequence[x:x+y]
   # first for loop starts at zero because we've already initialized the first row
   for x in range(1,length):
       for y in range(0,length - x):
 
           # this is one of the most important sections of the algorithm
           # basically if we are in the first row we are considering character y plus the one immediately to the right of it
           # if both are the same character, then the longest subsequence is 2, if not it's 1, which is handled in the case below
           # this part is very important because it deals with the alternate cases of a subsequence with odd number of chars vs an even number
           if x == 1 and sequence[x+y] == sequence[y]:
               memo[x][y]= 2
          
           # if we are not in the first row we need to find the longest subsequence in the general case
           else:
               # There are 2 possibilities
               # this one I interpret is adding 2 of the same char onto the end of an existing palindromic subsequence
               # example:
               # ABBA
               # ^  ^ we compare these 2 chars if they are the same we take the longest subsequence of the chars inside of the As and then
               # add 2 to it
               if sequence[x+y] == sequence[y]:
                   memo[x][y]= memo[x-2][y+1] + 2
              
               # If the above case is not true we cannot add 2 new chars on the end of an existing subsequence
               # However there are 2 subcases
               # Case 1 example:
               # ABAC
               # ^  ^ for this sequence ABA is the longest and it is still considering A but with one less char (C) to consider additionally (x-1)
               #      this value will have already been computed at memo[x-1][y]
 
               # Case 2 example:
               # ACBC
               # ^  ^ for this sequence if we are considering A the longest subsequence is CBC which is already computed and
               #      stored at memo[x-1][y+1] basically the next char over (C) but only considering the next 2 chars
 
               # we take the max value of these two subcases if this is the two cases
               else:
                   memo[x][y]= max(memo[x-1][y],memo[x-1][y+1])
   print_memo(memo)
   #we return the value at memo[length-1][0] because it's the first character considering the next length - 1 chars after it
   return memo[length-1][0]
 
 
 
test(1, "ACGTGTCAAAATCG", 8)
test(2, "AAAB", 3)
test(3, "AA", 2)
test(4, "AB", 1)
test(5, "A", 1)
test(6, "ABCDEFGFBCD", 5)
test(7, "", 0)
 
 
 
 
 
 

