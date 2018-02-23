#!/usr/bin/env python

#add
abc =['a','b','c']
abc.append('d')
abc.append('e')
print(abc)
print(type(abc))
print(type(abc[2]))

#count
abc.append('a')
print(abc.count('a'))

#extend
a =[1,2,3]
b =[4,5,6]
a.extend(b)
print(a *2)

#index
linux =['link','lina','linb','linc']
print(linux.index('lina'))
print(linux.index('linb'))

#insert
abc =[1,3,4,5,6]
abc[1]
print(abc)

abc.insert(1,2)
abc.insert(5,'6')
print(abc)

#pop
abc =[1,2,3,4]
abc.pop(0)
abc.pop()
print(abc)

abc =['hello','boy','hello','girl']
abc.remove('hello')
print(abc)

#reverse & sort
abc =[1,2,3,4,5]
abc.reverse()
print(abc)
abc.sort()
print(abc)

#slice
x =[10,20,30,40,50,60]
print(x[2:3])
print(x[2:3:1])
print(len(x))
print(max(x))
print(min(x))

# add 
lists =[[] for i in range(3)]
lists[0].append(3)
lists[1].append(5)
lists[2].append(7)
print(lists)

#replace
x =[10,20,30,40,50,60]
x[1] =22
print(x)

#slice
x[2:4] = [12]
print(x)

x =[10,20,30,40,50,60]
del x[2:4]
print(x)

#replace2
x1=[10,20,30,40,50,60]
x1[2:3:6] =[11]
print(x1)

abc =[1,11,12,32]
abc.copy()
print(abc)
abc.clear()
print(abc)


print(list('abc'))

"""
['a', 'b', 'c', 'd', 'e']
<class 'list'>
<class 'str'>
2
[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
1
2
[1, 3, 4, 5, 6]
[1, 2, 3, 4, 5, '6', 6]
[2, 3]
['boy', 'hello', 'girl']
[5, 4, 3, 2, 1]
[1, 2, 3, 4, 5]
[30]
[30]
6
60
10
[[3], [5], [7]]
[10, 22, 30, 40, 50, 60]
[10, 22, 12, 50, 60]
[10, 20, 50, 60]
[10, 20, 11, 40, 50, 60]
[1, 11, 12, 32]
[]
['a', 'b', 'c']
[Finished in 0.1s]
"""
