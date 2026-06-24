class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        for i in range(0,n+1):
            count=0
            a=i
            while a:
                a=a&(a-1)
                count=count+1
            result.append(count)
        return result

        