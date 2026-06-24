class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_in=float('inf')
        max_in=0
        for i in prices:
            if i<min_in:
                min_in=i
            else:
                profit=i-min_in
                if profit>max_in:
                    max_in=profit
        return max_in
                    

