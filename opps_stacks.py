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
#-----------------------------------------------------------------------------------------#
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

obj1=Node(1)
obj2=Node(2)
obj3=Node(3)

obj1.next=obj2
obj2.next=obj3
cur=obj1
while cur:
    print(cur.data,end='')
    cur=cur.next
print('nul')