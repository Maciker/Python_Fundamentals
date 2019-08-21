# strings and collections
# single or double quote 'str' = "str"
# \n new line
p = 'this string\nspans multiple\nlines'
print(p)
# raw string don't need \ for scaping characters
path = r'C:\Users\My_User\Data\scripts'
print(path)
# sequence type
print(path[0:10])
# str have a lot ofmethods
print(p.capitalize())

# list mutable sequence of objetcs
numbers = [1,2,3,4,5,6,7,8,9, 0]
colors = ['red', 'blue', 'green', 'white', 'black']
# Print all the list without last element
print(numbers[:-1])
# Print firt element
print(colors[0])
numbers[-1] = 10
print(numbers)

# dictionaries mutable mappings of keys to values
dict = {'iker': '123456789P', 'erku': 'P987654321'}
print(dict['erku'])

# for loop
for color in colors:
    print(color)

# In a dictionary we get the key values
for name in dict:
    print(name, dict[name])

#example putting all together
from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)

print(story_words)