class Solution:
    def isValid(self, s: str) -> bool:

        stack= []
        valid_parentheses = {'}':'{',']':'[',')':'('}

        for c in s:
            if c in valid_parentheses:
                if stack and stack[-1] == valid_parentheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

        
        