class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        count=sorted(count.items(), key=lambda x:x[1],reverse=True)
        lst=[]
        if(len(count)==1):
            lst.append(count[0][0])
            return lst
        for x in range(len(count)):
            if(x==k):
                return lst
            lst.append(count[x][0])
        return lst    
