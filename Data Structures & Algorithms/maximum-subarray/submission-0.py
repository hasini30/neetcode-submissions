class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        s=0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                s=sum(nums[i:j+1])
                maxi=max(maxi,s)
        return maxi
nums = [2,-3,4,-2,2,1,-1,4]   
result=Solution().maxSubArray(nums)
print(result)