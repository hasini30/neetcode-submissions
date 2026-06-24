class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(0,i):
                add=nums[i]+nums[j]
                if add==target:
                    return [j,i]
        