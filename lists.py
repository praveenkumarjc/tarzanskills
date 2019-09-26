names=['praveen','hari','nanda','salman']
print('praveen'in names)
print('praveen'not in names)
print('naresh'in names)
print(names.index('hari'))
print(names[0])
print(names[::-1])
names.append('samarth')
print(names)
names[2]='varun'
print(names)
names.remove('salman')
print(names)
del names[2]
print(names)
names.pop()
print(names)
names.insert(0,'manja')
#nested
t3=[1,2,3,4,5,[7,8,9],[1,2,4]]
print(t3[5][0])
len
print(len(t3))
#concat
t4=[3,5]
t5=[8,9]
print(t4+t5)
#in and not in


#sort

t1=[1,2,3]
t2=[6,5,6]
t1.extend(t2)
t2.sort()
print(t2)
print(t1)
