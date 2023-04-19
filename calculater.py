class Calculator:
    def sum(self, a, b):
        return a + b

    def product(self, a, b):
        return a * b

    def quotient(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b

    def difference(self, a, b):
        return a - b


calc = Calculator()

print(calc.sum(14, 16))
print(calc.product(14, 16))
print(calc.quotient(12, 2))
print(calc.quotient(12, 0))
print(calc.difference(12, 6))
