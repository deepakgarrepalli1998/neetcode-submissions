class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            target=-nums[i]
            while j<k:
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
                else:
                    j+=1
                    k-=1                    

        return result


        