class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        duplicates = set()

        for c in nums:
            if c in duplicates:
                return True
            else:
                duplicates.add(c)

        return False
            
        