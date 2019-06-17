import numbers


class Calculator:
    def add(self, op1, op2):
        self._validate(op1)
        self._validate(op2)
        return op1 + op2

    def subtract(self, op1, op2):
        self._validate(op1)
        self._validate(op2)
        return op1 - op2

    def multiply(self, op1, op2):
        self._validate(op1)
        self._validate(op2)
        return op1 * op2

    def divide(self, op1, op2):
        self._validate(op1)
        self._validate(op2)
        return op1 / op2

    def _validate(self, operand):
        if not isinstance(operand, numbers.Number):
            raise ValueError(f'"{operand}" is not a number.')
