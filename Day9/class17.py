# list logic Question 

# Question.1: leetcode 1. Two Sum

 class Solution:
    def twoSum(self, nums:list , target:int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            ex = target - nums[i]
            if ex in d.keys():
                return [d[ex],i]
            else:
                d[nums[i]] = i

s = Solution()
print(s.twoSum(nums=[2,7,11,15], target=13)) 

# Question.2: leetcode 217. Contains Duplicate

class Solution:
    def containsDuplicate(self , nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)
        d = {}
        for i in nums:
            if i in d:
                return True
            else:
                d[i]=1
        return False
    
s = Solution()
print(s.containsDuplicate(nums=[2,3,1])) 