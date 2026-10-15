class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        duplicate = set()

        for c in nums:
            if c in duplicate:
                return True
            else:
                duplicate.add(c)
        return False
                
        