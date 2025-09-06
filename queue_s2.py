class queary:

    def __init__(self):
        self.new=[]

    def push(self,value):
        self.new.append(value)

        
    def peek(self):
        if self.new:
            
            return self.new[0]        

    def degueue(self):
        if self.new:
            
            return self.new.pop(0)
            
        else:
            return "empty queary"

    def isEmpty(self):
        return len(self.new)== 0
myqueue=queary()
myqueue.push(10)
myqueue.push(20)
print("Peek:", myqueue.peek())       # Peek: 10
print("Dequeue:", myqueue.degueue()) # Dequeue: 10
print("Is empty?", myqueue.isEmpty())
        
