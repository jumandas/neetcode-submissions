class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #we will use a hashmap(dict)

        seen = {}

        for i, numbers in enumerate(nums):
            diff = target - numbers

            if diff in seen:
                return [seen[diff], i]
            
            seen[numbers] = i