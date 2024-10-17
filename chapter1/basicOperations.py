import math

if __name__ == '__main__':
    a, b = input().split(' ')
    a, b = int(a), int(b)
    print(f'{a + b}\n{a - b}\n{a * b}\n{math.floor(a / b)}\n{a % b}')
