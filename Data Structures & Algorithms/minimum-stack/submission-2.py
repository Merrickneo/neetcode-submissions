class MinStack:
    '''
    
    '''

    def __init__(self):
        self.arr = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        
        self.arr.append(val)
        
        

    def pop(self) -> None:
        top = self.arr.pop()
        if top == self.minStack[-1]:
            self.minStack.pop()
        return top
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
