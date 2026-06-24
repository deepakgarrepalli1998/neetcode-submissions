class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped={}
        for s in strs:
            key=tuple(sorted(s))
            if key in grouped.keys():
                grouped[key].append(s)
            else:
                grouped[key]=[s]
        return list(grouped.values())
