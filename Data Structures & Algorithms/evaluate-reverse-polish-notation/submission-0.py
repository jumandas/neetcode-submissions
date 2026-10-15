class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
                    
        stk = []

        for i in tokens:
            if i in {'+' , '-' , '*' , '/'}:
                b= stk.pop()
                a= stk.pop()
                result = 0
                if i == '+':
                    result = a+b
                    stk.append(result)
                elif i == '-':
                    result = a-b
                    stk.append(result)
                elif i == '*':
                    result = a*b
                    stk.append(result)
                elif i == '/':
                    result = a/b
                    stk.append(int(result))
            else:
                stk.append(int(i))
        
        return stk[-1]
        