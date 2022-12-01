class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt=0
        count=Counter(nums)
        for x in nums:
            if(count[k-x]>0 and count[x]>0):
                if(x==k-x and count[x]==1):
                    continue
                count[x]-=1
                count[k-x]-=1
                cnt+=1
        return cnt   
