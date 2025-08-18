import numpy as np


def bit_not(n):
    return (1 << 8) - 1 - n


a = 5
print(f'~{a} = ~0b{a:08b} = 0b{bit_not(a):08b} = {bit_not(a)}')
b = np.uint8(5)
print(f'~{b} = ~0b{b:08b} = 0b{~b:08b} = {~b}')

a = 5
b = 3
c = 2
print(f'{a} & {b} = 0b{a:08b} & 0b{b:08b} = 0b{a & b:08b} = {a & b}')
print(f'{a} | {b} = 0b{a:08b} | 0b{b:08b} = 0b{a | b:08b} = {a | b}')
print(f'{a} ^ {b} = 0b{a:08b} ^ 0b{b:08b} = 0b{a ^ b:08b} = {a ^ b}')
print(f'{a} << {c} = 0b{a:08b} << {c} = 0b{a << c:08b} = {a << c}')
print(f'{a} >> {c} = 0b{a:08b} >> {c} = 0b{a >> c:08b} = {a >> c}')
