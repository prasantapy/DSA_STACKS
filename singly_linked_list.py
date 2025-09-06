class Node:

    def __init__(self,val):
        self.val=val
        self.next=None

class stack:

    def __init__(self):
        self.head=None

Node1=Node(10)
Node2=Node(20)
Node3=Node(30)

Node1.next=Node2
Node2.next=Node3

st1=stack()
st1.head=Node1
current=st1.head
while current is not None:
    print(current.val,end='-->')
    current=current.next
print("None")
    
