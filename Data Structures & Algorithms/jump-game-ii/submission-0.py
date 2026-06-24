class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        farest=0
        curr=0
        n=len(nums)
        for i in range(0,n-1):
            farest=max(farest,i+nums[i])
            if i==curr:
                count=count+1
                curr=farest
        return count
nums = [2,3,1,1,4]
result=Solution().jump(nums)
print(result)
            