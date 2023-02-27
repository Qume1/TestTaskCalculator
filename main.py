def calculator(expression):
    try:
        result = eval(expression)
        print(result)
    except (SyntaxError, TypeError):
        return "Invalid expression"


if __name__ == '__main__':
    calculator(input())


