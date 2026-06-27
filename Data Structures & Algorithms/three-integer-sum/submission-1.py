class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            target=-nums[i]

            while j<k:
                if j>i+1 and nums[j]==nums[j-1]:
                    j+=1
                    continue
                sumpair=nums[j]+nums[k]
                append=[nums[i],nums[j],nums[k]]
                if sumpair==target and append not in result:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif sumpair<target:
                    j+=1
                elif sumpair>target:
                    k-=1                
        return result


        