class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        processed={}
        for i,number in enumerate(nums):
            base=target-number
            if base in processed:
                return [min(i,processed[base]),max(i,processed[base])]
            processed[number]=i
            
        