class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer=[]
        for x in range(len(r)):
            numsn=nums[l[x]:r[x]+1]
            numsn.sort()
            ans=True
            for i in range(len(numsn)-1):
                e=numsn[1]-numsn[0]
                if(numsn[i+1]-numsn[i]!= e):
                    ans=False
                    break
                ans=True
            answer.append(ans)   
        return answer 
