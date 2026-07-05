class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        smap={}
        for c in s:
            smap[c]=smap.get(c,0)+1
        for c in t:
            smap[c]=smap.get(c,0)-1
        return not any(smap.values())

        