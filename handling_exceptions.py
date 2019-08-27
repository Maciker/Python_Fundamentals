"""import sys

def convert(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        # print standard error
        print('Conversion error: {}'.format(str(e)), file=sys.stderr)
        return -1

print(convert('33'))

print(convert('iker'))

print(convert('[1,2,3,4]'))

from math import log

def string_log(s):
    v = convert(s)
    return log(v)"""
def sqrt(x):
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

def main():
    print(sqrt(9))
    try:
        print(sqrt(-1))
    except ZeroDivisionError:
        print('Error: Zero Division')
    finally:
        print('Always run this')

if __name__ == '__main__':
    main()