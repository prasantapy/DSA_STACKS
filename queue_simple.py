queue=[]


queue.append('AB')
queue.append('CD')
queue.append('EF')

print('fully queue',queue)

f_ele=queue[0]
print('frist in',f_ele)

re_ele=queue.pop(0)
print('frist out',re_ele)

isEmpty=not bool(queue)
print('isEmpty',isEmpty)

print('size',len(queue))
