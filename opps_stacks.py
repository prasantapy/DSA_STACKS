class stack:

    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)

    def peek(self):
        return self.stack
    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        length = len(self.stack)
        return length
obj=stack()

obj.push('A')
obj.push('B')
obj.push('C')
print(obj.peek())
print(obj.pop())
print(obj.isEmpty())