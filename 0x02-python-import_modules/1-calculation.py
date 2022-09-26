#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1 as c
    a = 10
    b = 5
    text = f"{a} + {b} = {c.add(a, b)}"
    text1 = f"{a} - {b} = {c.sub(a, b)}"
    text2 = f"{a} * {b} = {c.mul(a, b)}"
    text3 = f"{a} / {b} = {c.div(a, b)}"
    print(text+"\n"+text1+"\n"+text2+"\n"+text3)
