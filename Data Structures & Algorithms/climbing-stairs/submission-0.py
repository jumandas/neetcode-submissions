class Solution:
    def climbStairs(self, n: int) -> int:

        #Finding Combination of Steps to Reach the Number n
        if n <= 2:
            return n

        two_steps_back = 1
        one_steps_back = 2

        for current_step in range(3 ,n +1):
            ways_to_reach_here = two_steps_back + one_steps_back

            two_steps_back = one_steps_back
            one_steps_back = ways_to_reach_here

        return one_steps_back

        
        