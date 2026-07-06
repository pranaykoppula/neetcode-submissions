class Solution:
    def isValid(self, s: str) -> bool:
        p_stack = []
        close = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for i in range(len(s)):
            c=s[i]
            if c in close:
                p_stack.append(c)
            elif len(p_stack):
                if c!=close[p_stack.pop()]:
                    return False
            else: 
                return False
        return (len(p_stack)==0)