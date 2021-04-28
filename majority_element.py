def majorityElement(nums):
    print(nums)
    if len(nums) == 0: return None
    if len(nums) == 1: return nums[0]

    mid = len(nums) //2
    first = majorityElement(nums[:mid])
    second = majorityElement(nums[mid:])

    if first == second: 
        print(first)
        return first
    if nums.count(first) > mid: 
        print(first)
        return first
    if nums.count(second) > mid: 
        print(second)
        return second

    #if len(nums) == 1: return nums[0]
    #if len(nums) % 2 == 1:
    #   check = nums.pop(-1)
    #    if nums.count(check) >= len(nums) // 2: return check
    #for i in range(len(nums)-1,0,-2):
     #   if nums[i] == nums[i-1]:
      #      nums.pop(i-1)
       # elif nums[i] != nums[i-1]:
       #     nums.pop(i-1)
      #      nums.pop(i-1)
    #return majorityElement(nums)

input = [1,2,1,3,1,4,1,3,1,4,1]

print(majorityElement(input))
