class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        brackets = {")" : "(" , "}" : "{" , "]" : "["}

        for i in s:
            if i in brackets:
                if stk and stk[-1] == brackets[i]:
                    stk.pop()
                else:
                    return False        
            else:
                stk.append(i)
        
        return True if not stk else False

                
        