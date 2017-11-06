"""
List

l = []
l = list()

"""

l = ['a','b','c']

l.append('d')
print (l)
l.insert(0 , '1')
print(l)
l.pop(0)
print (l)

print(l.index('b'))
l = 'abcdfghi'
l = list(l)
print(l)

#Strings

s = 'abc:cde'
parts= s.split(':')
print(parts)

new_strint= '.'.join(parts)
print(new_strint)

s = 'hello world'
print(len(s))

s= '    abc      '
print(s.strip())

"""
#Tuples

t =()
t = tuple()

"""
t = tuple(l)
print(t)

t = ('Othello', 'Iago')

hero , villain = t

print(hero , villain)

l = 'abcdf'
l= list(l)

for i , letter in enumerate(l):
    print(i, letter)


"""
{}
dict()

"""

d = {'name':'ivan', 'subname1' : 'pedro', 'subname2' : 'arteaga'}
print(d)

d = dict(name='ivan', subname1 = 'pedro', subname2 = 'arteaga')

print(d)

for i in d:
    print (i, d[i])

print(d.items())

for a , b in d.items():
    print(a , b)

d.iteritems