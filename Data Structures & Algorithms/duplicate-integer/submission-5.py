class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        val = set()

        for c in nums:
            if c in val:
                return True
            val.add(c)
        return False
        