class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        read={}
        for i in nums:
            if i in read:
                return True
            else:
                read[i]=1
        return False
