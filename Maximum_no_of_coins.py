class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        nk=len(piles)
        n=len(piles)-2
        nl=int((nk)/3) -1
        sum=0
        while(n>nl):
            sum+=piles[n]
            n-=2
        return sum 
