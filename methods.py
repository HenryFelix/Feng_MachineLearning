#!/usr/bin/env python3

# make letters upper.
a = "i Love python!"
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.casefold())
print("ABCD1234abcd".swapcase())
print("ABCD1234abcd".title())
print("ABCD1234abcd".upper())

# str plus str.
a1 ="I love python2 !"
a2 ="I love ruby !"
print(a1 + a2)
print(a1[0:5] + a2[-5:-1])

# make full left and right.
print(a1.center(20,"*"))

# calcuate
print(a1.count('o',1,15))

#starwith and endwith
print(a1.startswith("I"))
print(a1.endswith("!"))

#make \t into blank
a3 = "tab\ttab!" 
print(a3.expandtabs(10))
print("****abc".lstrip('*')) #delete balank or str.

#find str
a4 = "I love python very much!"
print(a4.find('y',2,10))
print(a4.index('o'))

#check str whether number or str.
a5 = "abcdef1233"
print(a5.isalnum()) #str and number
print(a5.isalpha()) #str
print(a5.isdecimal()) #number
print(a5.isdigit()) # number
print(a5.isnumeric())
print(a5.isprintable())

#check variable is true or false
print("a8".isidentifier()) 

#check the letter upper.
a6 = "I love python3 very much!"
print(a6.islower())
print(a6.istitle())
print(a6.isupper())

#check space
print("  ".isspace())

#join and slice
a7 = ['a','b','c','d']
print(" python ".join(a7))

# make left
print('abc'.ljust(10,'*'))
print('abc'.rjust(10,'*'))
print('aaa'.zfill(10))

#replace
a8 = "aeious"
a9 = "123456"
print("my cat is a cute cat".translate(str.maketrans(a8,a9)))
print("my cat is a cute cat".translate(str.maketrans({'a':'2','e':'1'})))
print("aaaa".replace('a','1'))
print("aaaa".replace('a','1',3))
print("aaaaa".replace('aa','22',1))
print("ababa1212".translate({97:"F"}))

#slice
print("ABCD1234abcd".partition("B"))
print("ABCD1234abcd".rpartition("B"))

#find
print('ABCD1234abcd'.rfind('C'))
print('ABCD1234abcd'.rindex('C'))

#split
print("AB CD 12 34 ab cd".rsplit(maxsplit=3))
print("AB CD 12 34 ab cd".split(maxsplit=3))
print("A,C,1,3,a,123".split(',',4))

#delete
print('***aeious'.rstrip('us')) #right
print("    Aaaa  ".strip())
print("***aaa***".strip('*'))

#split again
a101 = "abcd1\n12324\nkagcnajk\n"
print(a101.splitlines())
print(a101.splitlines(keepends=True))

#start
print("ABCD1234abcd".startswith('A',0,3))
print("ABCD1234abcd".startswith('bbb'))

"""
I love python!
I LOVE PYTHON!
i love python!
i love python!
abcd1234ABCD
Abcd1234Abcd
ABCD1234ABCD
I love python2 !I love ruby !
I lovuby 
**I love python2 !**
2
True
True
tab       tab!
abc
8
3
True
False
False
False
False
True
True
False
False
False
True
a python b python c python d
abc*******
*******abc
0000000aaa
my c1t 36 1 c5t2 c1t
my c2t is 2 cut1 c2t
1111
111a
22aaa
FbFbF1212
('A', 'B', 'CD1234abcd')
('A', 'B', 'CD1234abcd')
2
2
['AB CD 12', '34', 'ab', 'cd']
['AB', 'CD', '12', '34 ab cd']
['A', 'C', '1', '3', 'a,123']
***aeio
Aaaa
aaa
['abcd1', '12324', 'kagcnajk']
['abcd1\n', '12324\n', 'kagcnajk\n']
True
False
[Finished in 0.1s]
"""


















