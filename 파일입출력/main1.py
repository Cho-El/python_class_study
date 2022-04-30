if __name__ == '__main__':
    from calculator.add import add_and_multiply
else:
    from .calculator.add import add_and_multiply

if __name__ == '__main__':
    print(add_and_multiply(1,2))