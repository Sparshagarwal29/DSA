class Queue :
    def __init__(self):
        self.iteam = []
    def is_empty(self):
        return len(self.iteam) == 0
    def enqueue(self,val):
        self.iteam.append(val)
    def dequeue(self):
        if len(self.iteam) == 0:
            return "empty Queue"
        else:
            x = self.iteam.pop(0)
            return x 
    def front(self):
        if len(self.iteam) == 0 :
            return "empty Queue"
        return self.iteam[0]
    def rear(self):
        if len(self.iteam) == 0 :
            return "empty Queue"
        return self.iteam[-1]
    def size(self):
        return len(self.iteam)
    
