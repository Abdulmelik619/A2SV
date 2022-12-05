class Solution:
    def isValid(self, s: str) -> bool:
        match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
        g=deque()
        for x in s:
            if x=='(' or x=='{' or x=='[':
                g.append(x)
            else:
                if(len(g)==0):
                    return False 
                elif(g.pop()!=match_dict[x]):
                    return False
        return len(g)==0
