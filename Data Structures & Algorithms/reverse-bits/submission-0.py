class Solution:
    def reverseBits(self, n: int) -> int:
        rev=0
        for i in range(32):
            last=n&1
            rev=rev<<1|last
            n=n>>1
        return rev


        