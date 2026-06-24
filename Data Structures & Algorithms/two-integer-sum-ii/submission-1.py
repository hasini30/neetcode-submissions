class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            s=numbers[l] + numbers[r]
            if s==target:
                return [l+1,r+1]
            elif s<target:
                l=l+1
            else:
                r=r-1
        
numbers = [1,2,3,4]
target = 3
print(Solution().twoSum(numbers, target))