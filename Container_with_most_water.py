class Solution:
    def maxArea(self, height: List[int]) -> int:
        m_area=0
        l=0
        r=len(height)-1
        while(l!=r):
            w=r-l
            h=min(height[l],height[r])
            area=w*h
            if(area >= m_area):
                m_area=area
            if(height[l]>=height[r]):
                r-=1
            else:
                l+=1
        return m_area
