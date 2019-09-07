""" Ejemplos
f = open('iker.txt', mode='wt', encoding='utf-8')

f.write('Esta es la primera linea')

f.write('oooh no tenia salto de linea \n')

f.write('fin de fichero')

f.close()

f = open('iker.txt', mode='rt', encoding='utf-8')

print(f.read(24))

print(f.readline())

# Ir al inicio del fichero
f.seek(0)
print(f.readline())

f.seek(0)
print(f.readlines())

f.seek(0)
lines = f.readlines()
for line in lines:
    print(line)

f.close()

f = open('iker.txt', mode='at', encoding='utf-8')

f.writelines(['Estas son ls lineas nuevas, \n',
              'escribiendo mas lineas'])

f.close()

f = open('iker.txt', mode='rt', encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line)

f.close()


import sys

def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        print(line)
    f.close()

main('iker.txt')
"""