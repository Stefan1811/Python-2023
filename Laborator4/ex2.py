class Queue:
    def __init__(self) :
        self.items=[]
    def push(self,number):
        self.items.append(number)
    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None
    def is_empty(self):
        return len(self.items) == 0

q1=Queue()
q1.push(2)
q1.push(4)
q1.push(5)
q1.push(26)
print("Peek:", q1.peek())
print("Pop:", q1.pop())
print("Pop:", q1.pop())