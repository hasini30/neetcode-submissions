class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=0
        for i in digits:
            a=a*10+i
            b=a+1
        return [int(d) for d in str(b)]