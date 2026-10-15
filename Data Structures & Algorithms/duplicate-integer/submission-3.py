class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashmaps
        counthashset = set()

        for c in nums:
            if c in counthashset:
                return True
            counthashset.add(c)
        return False
            
            

         