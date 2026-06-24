class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ssort="".join(sorted(s))
        tsort="".join(sorted(t))
        for j in range(len(ssort)):
            if ssort[j]!=tsort[j]:
                return False
        return True