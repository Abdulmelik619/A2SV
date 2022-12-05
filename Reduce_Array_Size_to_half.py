class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count=Counter(arr)
        lst=[]
        for x in count.values():
            lst.append(x)
        lst.sort(reverse=True)
        if(lst[0] > len(arr)//2):
            return 1
        else:
            sum=0
            for i in range(len(lst)):
                sum+=lst[i]
                if(sum>=len(arr)//2):
                    return i+1
