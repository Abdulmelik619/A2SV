class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=Stack()
        for x in tokens:
            if x=='+' or x=='-' or x=="*" or x=='/':
                a=str(stack.pop())
                b=str(stack.pop())
                c=b+x+a
                print(c)
                e=eval(c)
                e = math.trunc(e)
                print(e)
                stack.push(e)
            else:
                stack.push(x)
        a=stack.pop()
        print(a)
        return int(a)
