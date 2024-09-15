from numerical_methods import FalsePositionMethod, BisectionMethod, NewtonRaphsonMethod
import math

g = 9.81
c = 12.5
v_target = 45
t = 10

def f(m):
    return (m * g / c) * (1 - math.exp(-c * t / m)) - v_target

def df(m):
    return g / c * (1 - math.exp(-c * t / m)) + (g * t * math.exp(-c * t / m)) / m

if __name__ == "__main__":
    lower_bound = 50
    upper_bound = 200
    max_iterations = 50

    fp_method = FalsePositionMethod(f, lower_bound, upper_bound, max_iterations)
    root_fp = fp_method.solve()
    print(f"Parachutist mass found using False Position Method: {root_fp:.2f} kg")

    bisection_method = BisectionMethod(f, lower_bound, upper_bound, max_iterations)
    root_bis = bisection_method.solve()
    print(f"Parachutist mass found using Bisection Method: {root_bis:.2f} kg")

    initial_guess = 100
    newton_method = NewtonRaphsonMethod(f, df, initial_guess)
    root_newton = newton_method.solve()
    print(f"Parachutist mass found using Newton-Raphson Method: {root_newton:.2f} kg")
