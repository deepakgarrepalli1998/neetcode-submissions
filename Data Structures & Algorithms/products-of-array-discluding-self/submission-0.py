class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results=[]
        output=[]
        for i in range(len(nums)):
            j=i+1
            if i==0:
                results.append(1)
                suffix=1
                for number in range(j,len(nums)):
                    suffix*=nums[number]
                results.append(suffix)
                i+=1
            elif i!=0:
                prefix=1
                for k in range(0,i):
                    prefix*=nums[k]
                results.append(prefix)
                suffix=1
                for i in range(j,len(nums)):
                    suffix*=nums[i]
                results.append(suffix)
        for x in range(1,(len(results)//2)+1):
            start=2*x-2
            end=2*x-1
            product=results[start]*results[end]
            output.append(product)
        return output


            
            
        