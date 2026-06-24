class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                maxi=max(maxi,sum(nums[i:j+1]))
        return maxi
nums = [2,-3,4,-2,2,1,-1,4]
print(Solution().maxSubArray(nums))

