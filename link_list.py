 #link_list
class Node:

    def __init__(self,value):
        self.value=value
        self.next=None


class Stack:
    def __init__(self):
        self.head=None
        self.size=0

    def push(self,value):
        current=Node(value)
        if self.head:
            current.next=self.head

        self.head=current
        self.size+=1

    def pop(self):
        if self.isempty():
            return "empty stack"
        else:
            poped=self.head

            
            self.head=self.head.next
            self.size-=1
            return poped.value


    def peek(self):
        if self.isempty():
            return "empty stack"
        else:
            
            return self.head.value

    def isempty(self):
        return self.size ==0

    def Stack_size(self):
        return self.size


    def Display(self):
        current=self.head

        while current:
            print(current.value,end="--->")
            current=current.next

        print()
mystack=Stack()
mystack.push(10)
mystack.push(20)
mystack.push(30)
mystack.push(40)


mystack.Display()


print('pop',mystack.pop())

print('peek',mystack.peek())

print('is Empty',mystack.isempty())

print('Stack_size',mystack.Stack_size())


            
            
            

        
