#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1 as c
    a = 10
    b = 5
    print(f"{a} + {b} = {c.add(a, b)}")
    print(f"{a} - {b} = {c.sub(a, b)}")
    print(f"{a} * {b} = {c.mul(a, b)}")
    print(f"{a} / {b} = {c.div(a, b)}")

