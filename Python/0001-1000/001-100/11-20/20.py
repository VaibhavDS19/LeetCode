class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        n = -1
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stk.append(c)
                n += 1
            elif c == ')':
                if n < 0 or stk[n] != '(':
                    return False
                stk.pop()
                n -= 1
            elif c == '}':
                if n < 0 or stk[n] != '{':
                    return False
                stk.pop()
                n -= 1
            elif c == ']':
                if n < 0 or stk[n] != '[':
                    return False
                stk.pop()
                n -= 1
        return n == -1
