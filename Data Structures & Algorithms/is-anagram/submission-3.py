class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ssort="".join(sorted(s))
        tsort="".join(sorted(t))
        return ssort==tsort
        