class Solution:
    def trap(self, height: List[int]) -> int:
        pref=[]
        suff=[]
        prefref=0
        suffref=0
        totalwater=0
        for i in range(len(height)):
            if i==0:
                pref.append(height[i])
                prefref=height[i]
            else:                
                prefref=max(prefref,height[i])
                pref.append(prefref)
        for i in range(len(height)-1,-1,-1):
            if i==len(height)-1:
                suff.append(height[i])
                suffref=height[i]
            else:
                suffref=max(suffref,height[i])
                suff.append(suffref)
        for i in range(len(height)):
            suffindex=len(height)-1-i
            totalwater+=(min(pref[i],suff[suffindex])-height[i])
        return totalwater



