class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashmaps
        count = set()

        for c in nums:
            if c in count:
                return True
            count.add(c)
        return False
            
            

         