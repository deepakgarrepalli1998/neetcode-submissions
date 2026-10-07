class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        charSet=set()
        maxlength=0
        for r in range(len(s)):    
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            maxlength=max(r-l+1,maxlength)
        return maxlength


        