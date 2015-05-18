import random
from math import pi, sin, cos, tan, exp


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    expressions = [
        'pi*(x**2 + y**2)', # circle
        'sin(x)', # gradient horizontal
        'cos(x)', # gradient horizontal center-hollow
        'cos(x)+sin(x)',
        'abs(x)',
        '2*x**2*y**2', # corner circles
        'x**5*y**2+3*x*3+2*x**2+x**4', # thick gradient
        'exp(pi*sin(x))', # lighter gradient than sin(x)
        'sin(pi*x)*cos(x)*pi*(y**2 + y**2)', # reflecting half circles
        'sin(2*x**2*y**2)',
    ]

    return random.choice(expressions)
    

def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return eval(expr)
