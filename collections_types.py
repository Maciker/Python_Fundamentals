# tuple: immutable sequence or arbitrary objects
t = ['Iker', 34, 7.8]

for i in t:
    print(i)

# Can use in
print('Erkuden' in t)

# str: can use len, join, split,partition
s = 'We are in summer time'
print(len(s))
a = 'blue'
b = 'green'
c= 'red'
d = ','.join([a, b, c])
print(d)
print(s.split(' '))
# partition: part a tring in three parts arround a separator
departure, separator, arrival = 'Pamplona:Barcelona'.partition(':')
print('El vuelo sale de {} y llega a {}'.format(departure, arrival))

# range: arithmetic progression of integers
print(list(range(10)))
print(list(range(1,7)))
print(list(range(0,1001, 100)))

# don't iterate list with rage. Iterate the list directly
# some times can be usefull use enumerate
for i in enumerate(t):
    print(i)

# list: heterogeneous mutable sequence
l = s.split(' ')
print(l)
# slice: extracts part of a list seq[start:end]
print(s[::-1])
print(s[1:-1])

# copy a list. Be carefulll with shallow copies
z = l[:]
y = l.copy()
x = list(l)

# index, in, not in and count
notes = [5,5,8,4,8,10,6,5,4,7,8,9,3,1,6,10,8,9,9]
print(notes.index(1))
print(notes.count(9))
print(10 in notes)
print(2 not in notes)

# delete elements: use del for del by position and remove by value
# delete the first 10 in the list
del notes[notes.index(10)]
notes.remove(1)
print(notes)

# insert: position, value
notes.insert(0, 1000)
print(notes)

# Reverse and sortin
notes.reverse()
print(notes)
print(notes[::-1])
notes.sort()
print(notes)

# dictionaries
d = {'Iker': 'Beti Onak', 'Lebron James': 'Los Angeles Lakers', 'Carson Wentz': 'Philadelphia Eagles'}
print(d['Iker'])
# dict constructor
dd = dict(Iker=34, Erkuden=36, Asier=29)
print(dd)

# we can iterate by keys or values
for key in d:
    print(key)
for val in d.values():
    print(val)

# set: unordered collection of unique,immutable objects
p = set(notes)
print(p)
p.add(2)
p.add(1)
p.remove(1000)
print(p)
# set in algebra
blue_eyes = {'Olivia','Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Mia','Harry', 'Joshua', 'Jack', 'Amelia'}
smell_hcn = {'Harry','Amelia'}
taste_ptc = {'Lola','Harry', 'Lily', 'Amelia'}
o_blood = {'Olivia','Mia', 'Lily', 'Joshua'}
b_blood = {'Jack', 'Amelia'}
a_blood = {'Harry'}
ab_blood = {'Lola','Joshua'}
# Union method
print(blue_eyes.union(blond_hair))
# Intersection method
print(blue_eyes.intersection((blond_hair)))
# Diffrerence method
print(blue_eyes.difference((blond_hair)))
print(blue_eyes.symmetric_difference(blond_hair))