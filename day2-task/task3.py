# Question 3: Calculus with SciPy
#
# Define the function f(x) = x^3 + 2x^2 + x + 1.
# Compute the first and second derivatives of f(x) at x = 1.
# Compute the definite integral of f(x) from x = 0 to x = 2.

from scipy import integrate
from sympy import symbols, diff

# Define the function f(x) = x^3 + 2x^2 + x + 1
x = symbols('x')
f = x**3 + 2*x**2 + x + 1

# Compute the first and second derivatives of f(x) at x = 1
first_derivative = diff(f, x)
second_derivative = diff(first_derivative, x)

first_derivative_at_1 = first_derivative.subs(x, 1)
second_derivative_at_1 = second_derivative.subs(x, 1)

# Compute the definite integral of f(x) from x = 0 to x = 2
definite_integral_result, _ = integrate.quad(lambda x: f.subs('x', x), 0, 2)

print("First derivative of f(x) at x = 1:", first_derivative_at_1)
print("Second derivative of f(x) at x = 1:", second_derivative_at_1)
print("Definite integral of f(x) from x = 0 to x = 2:", definite_integral_result)
