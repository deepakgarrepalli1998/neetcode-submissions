class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        volume=0
        while i<j:
            currvolume=(j-i)*min(heights[i],heights[j])
            if currvolume>volume:
                volume=currvolume
            if heights[i]<heights[j]:
                i+=1
            elif heights[j]<heights[i]:
                j-=1
            else:
                i+=1        
        return volume
        