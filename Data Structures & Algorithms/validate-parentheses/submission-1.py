class Solution:
    def isValid(self, s: str) -> bool:
        p_stack = []
        close = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for i in range(len(s)):
            if s[i] in close:
                p_stack.append(s[i])
            elif len(p_stack):
                if s[i]!=close[p_stack.pop()]:
                    return False
            else: 
                return False
        return (len(p_stack)==0)