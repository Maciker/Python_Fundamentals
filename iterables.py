# List, set, dictionaries comprehension
words = 'You are not your thoughts, you are what you do'.split()
print(words)
print([len(word) for word in words])

from math import factorial, sqrt
# list
print([len(str(factorial(x))) for x in range(20)])
# set
print({len(str(factorial(x))) for x in range(20)})

from pprint import pprint as pp
country_to_capital = {'Spain': 'Madrid', 'France': 'Paris', 'UK': 'London', 'Italy': 'Rome'}
# reverse dictionary
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        return True

print([x for x in range(1000) if is_prime(x)])

# itarable and iterator
iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# generators
def gen123():
    yield 1
    yield 2
    yield 3

g = gen123()
print(g)
print(next(g))
print(next(g))
print(next(g))

for v in gen123():
    print(v)

# generators can only use one time. list use >>>>>>>>>>>>>>>>>>>>> memory than generators
n = sum(x*x for x in range(1, 10000001))
print(n)