class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash1={}
        for i in range (0,len(nums)):
            if nums[i] not in hash1:
                hash1[nums[i]]=1
                
            else:
                hash1[nums[i]]+=1
        for x in hash1:
            if hash1[x]>1:
                return True
        return False
