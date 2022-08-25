# -*- coding: utf-8 -*-

# Two Sum
def Two_Sum(nums=[3,2,4], target=6):  # Because nums[0] + nums[1] == 9, we return [0, 1]
    
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]

# res=Two_Sum()            

           
nums=[3,2,4]
target=6
hash_table={}

for i in range(len(nums)):
    if nums[i] in hash_table:
        print( [hash_table[nums[i]], i] )
    else:
        hash_table[target-nums[i]] = i            
