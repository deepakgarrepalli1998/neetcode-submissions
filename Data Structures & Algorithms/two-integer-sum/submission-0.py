class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checked={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in checked:
                return [checked[complement],i]
            checked[num]=i
        