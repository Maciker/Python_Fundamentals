x = 10
print(id(x))
x +=2
print(id(x))

# both names refers to the same object
# no variables -- names refered to object
r = [1,2,3]
s = r
s[1] = 2000
print(r)
print(s is r)

# passing arguments
m = [9, 15, 24]
def modify(k):
    k.append(39)
    print('k = {}'.format(k))

modify(m)

# default arguments. Be carefull with default values. Don't use mutable elements.
def banner(message, border = '-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("We are not our thoughts.We are what we do!")
banner('we are willing', '*')