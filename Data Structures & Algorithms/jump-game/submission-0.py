class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump=0
        for i in range(0,len(nums)):
            if i>max_jump:
                return False
            max_jump = max(max_jump, i + nums[i])
            if i > len(nums) - 1: 
                return False
        return True
nums = [1,2,0,1,0]
result=Solution().canJump(nums)
print(result)
        