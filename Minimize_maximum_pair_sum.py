class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        l=len(nums)-1
        a=[]
        for i in range(int(len(nums)/2)):
            a.append(nums[i]+nums[l])
            i+=1
            l-=1
        return max(a)   
