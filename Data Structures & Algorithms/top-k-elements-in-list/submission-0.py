class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i in count.keys():
                count[i]+=1
            else:
                count[i]=1
        sorted_dict_desc = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        sorted_keys = list(sorted_dict_desc.keys())
        return sorted_keys[:k]