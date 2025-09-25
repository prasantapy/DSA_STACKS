stack=[]
#push
stack.append('A')
stack.append('B')
stack.append('C') 
print(stack)
#peek
topstacks=stack[-1]

print(topstacks)
stack.pop()
print(stack)

isempty= not bool(stack)
print(isempty)

size = len(stack)
print(size)
