#!/usr/bin/python3

if __name__ == '__main__':
    import calculator_1 as calc
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    op = sys.argv[2]

    if op not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = "{} {} {} = {}"
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == '+':
        print(result.format(a, op, b, calc.sum(a, b)))
    elif op == '-':
        print(result.format(a, op, b, calc.sub(a, b)))
    elif op == '*':
        print(result.format(a, op, b, calc.mul(a, b)))
    else:
        print(result.format(a, '/', b, calc.div(a, b)))
