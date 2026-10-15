class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #if length is not same, return false directly
        if len(s) != len(t):
            return False

        # create 2 hashmaps
        countS , countT = {} , {}

        #run a for-loop with length of string and then for each character add 1 ,if the char 
        #already exists it will increment by 1 and store them in countS and countT
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i] ,0)
        return countS == countT
            