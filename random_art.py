import random
from math import pi, sin, cos

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.

class Expression:
    def __init__(self):
        self.commands = []

    def evaluate(self, x, y):
        value = 1
        for (command, coord) in self.commands:
            if command == "sin" and coord == "x":
                value *= sin(pi * x)
            elif command == "sin" and coord == "y":
                value *= sin(pi * y)
            elif command == "cos" and coord == "x":
                value *= cos(pi * x)
            elif command == "cos" and coord == "y":
                value *= cos(pi * y)

        return value

    def __str__(self):
        return str(self.commands)


def avg(a, b):
    return (a + b) / 2


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    # expr = lambda x, y: (random.random() * 2) - 1
    # return expr

    expr = Expression()
    for _ in range(3):
        if random.random() > 0.5:
            x_or_y = "x"
        else:
            x_or_y = "y"

        if random.random() > 0.5:
            sin_or_cos = "sin"
        else:
            sin_or_cos = "cos"

        expr.commands.append([sin_or_cos, x_or_y])

    return expr

def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr.evaluate(x, y)
