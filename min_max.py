input_nums = [234,234,2345,23,5,678,2,6,789,3245,8,6,345,1,324,2]
print(len(input_nums)) #16 <-- power of 2

def min_max(nums):
    if len(nums) == 1:
        # constant time base case
        return nums[0], nums[0]
    else:
        mid = len(nums) // 2
        #2 calls to min_max, each of size ~n/2 (n/2 if n is a power of 2 like given in problem)
        minimum_frist_half, maximum_frist_half = min_max(nums[:mid])
        minimum_second_half, maximum_second_half = min_max(nums[mid:])

        ret_min, ret_max = 0, 0
        #just two comparisons --> O(2) = O(1), or constant time at layer of the recurrence
        if (minimum_frist_half <= minimum_second_half): 
            ret_min = minimum_frist_half
        else:
            ret_min = minimum_second_half

        if (maximum_frist_half >= maximum_second_half): 
            ret_max = maximum_frist_half
        else:
            ret_max = maximum_second_half

        return ret_min, ret_max

print(min_max(input_nums)) #(1,3245)