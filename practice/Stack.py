class Stack:
    def __init__(self):
        self.iteam = []
    def is_empty(self):
        return (len(self.iteam) == 0)
    def push(self,val):
        self.iteam.append(val)
    def pop(self):
        if len(self.iteam) == 0 :
            return "empty Stack"
        else:
            x = self.iteam.pop()
            return x
    def top(self):
        if len(self.iteam) == 0 :
            return "empty Stack"
        else:
            return self.iteam[-1]
    def size(self):
        return len(self.iteam)

Stacke = Stack()  
print(Stacke)