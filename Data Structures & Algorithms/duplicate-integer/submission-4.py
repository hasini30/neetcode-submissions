class Solution:
    def hasDuplicate(self, nums):
        h={}
        for i in nums:
            if i not in h:
                h[i]=1
            else:
                h[i]=h[i]+1
        for j in h:
            if h[j]>1:
                return True
        return False
            
        
        
         