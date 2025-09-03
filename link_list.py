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
 #link_list
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        current_stack = Node(value)
        current_stack.next = self.head
        self.head = current_stack

    def pop(self):
        if self.head == None:
            return "empty stack"
        temp = self.head
        self.head = self.head.next

        return temp.value

    def display(self):
        curr = self.head

        while curr:
            print(curr.value)
            curr = curr.next
        print()


obj = Stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.display()
print('*' * 4)
obj.pop()
obj.display()