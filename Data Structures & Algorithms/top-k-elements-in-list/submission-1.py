class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        maxi=0
        second=0
        for i in nums:
            if i not in h:
                h[i]=1
            else:
                h[i]=h[i]+1
        sorted_items = sorted(h.items(), key=lambda x: x[1], reverse=True)
        result=[]
        for i in range(0,k):
            result.append(sorted_items[i][0])
        return result