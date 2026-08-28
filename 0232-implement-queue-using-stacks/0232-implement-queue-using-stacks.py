class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        pop_val = 0
        while True:
            popped = self.stack1.pop()
            if self.stack1 == []:
                pop_val = popped
                break
            self.stack2.append(popped)
            
        while self.stack2 != []:
            self.stack1.append(self.stack2.pop())
        
        return pop_val

    def peek(self) -> int:
        pop_val = 0
        while True:
            popped = self.stack1.pop()
            if self.stack1 == []:
                pop_val = popped
                break
            self.stack2.append(popped)  
        self.stack2.append(pop_val)
        while self.stack2 != []:
            self.stack1.append(self.stack2.pop())
        return pop_val

    def empty(self) -> bool:
        return self.stack1 == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()