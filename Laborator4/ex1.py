class Stack:
    def __init__(self) :
        self.items=[]
    def push(self,number):
        self.items.append(number)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    def is_empty(self):
        return len(self.items) == 0

st1=Stack()
st1.push(2)
st1.push(4)
st1.push(5)
st1.push(26)
print("Peek:", st1.peek())
print("Pop:", st1.pop())
print("Pop:", st1.pop())

