class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            total1,total2 = 0,0
            total1 = sum(nums[:i])
            total2 = sum(nums[i+1:])
            if total1 == total2:
                return i
        return -1
