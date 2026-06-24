class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        removedups=set(nums)
        currlen=1
        maxlen=1
        for i in removedups:
            prior=i-1
            subsq=i+1
            if prior not in removedups:
                while subsq in removedups:
                    currlen+=1
                    subsq+=1
                    if subsq not in removedups:
                        if currlen>maxlen:
                            maxlen=currlen
                        currlen=1
                        continue


        return maxlen
                
            
            
        