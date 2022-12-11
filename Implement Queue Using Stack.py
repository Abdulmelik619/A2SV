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
class MyQueue:

    def __init__(self):
        self.S1=Stack()
        self.S2=Stack()

    def push(self, x: int) -> None:
        while(self.S1.size()!=0):
            self.S2.push(self.S1.peek())
            self.S1.pop()
        self.S1.push(x)
        while(self.S2.size()!=0):
            self.S1.push(self.S2.peek())
            self.S2.pop()
    def pop(self) -> int:
        return self.S1.pop()
    def peek(self) -> int:
        return self.S1.peek()
    def empty(self) -> bool:
        return self.S1.is_empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
