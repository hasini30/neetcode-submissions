class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long=0
        numset=set(nums)
        for num in numset:
            if (num-1) not in numset:
                l=1
                while(num+l) in numset:
                    l=l+1
                long=max(l,long)
        return long
                