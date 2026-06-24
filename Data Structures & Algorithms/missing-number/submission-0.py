class Solution:
    def missingNumber(self, nums: List[int]) ->int :
        n=len(nums)
        exp=n*(n+1)//2
        tot=sum(nums)
        res=exp-tot
        return res



        
        