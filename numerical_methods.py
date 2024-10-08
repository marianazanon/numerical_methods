import math

def round_to_two_decimals(value):
    return round(round(value), 2)

class FalsePositionMethod:
    def __init__(self, f, lower_bound, upper_bound, max_iterations, epsilon=1e-6):
        self.f = f
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.max_iterations = max_iterations
        self.epsilon = epsilon

    def solve(self):
        if self.f(self.lower_bound) * self.f(self.upper_bound) > 0:
            raise ValueError("False position method failed. Choose another interval.")

        lower_bound, upper_bound = self.lower_bound, self.upper_bound

        for iteration in range(self.max_iterations):
            root_approx = (lower_bound * self.f(upper_bound) - upper_bound * self.f(lower_bound)) / (self.f(upper_bound) - self.f(lower_bound))
            f_approx = self.f(root_approx)

            if self._check_convergence(f_approx):
                return round_to_two_decimals(root_approx), iteration + 1

            if self.f(lower_bound) * f_approx < 0:
                upper_bound = root_approx
            elif self.f(upper_bound) * f_approx < 0:
                lower_bound = root_approx
            else:
                raise ValueError("False position method failed")

        return round_to_two_decimals(root_approx), self.max_iterations

    def _check_convergence(self, f_approx):
        return abs(f_approx) < self.epsilon

class BisectionMethod:
    def __init__(self, f, lower_bound, upper_bound, max_iterations, epsilon=1e-6):
        self.f = f
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.max_iterations = max_iterations
        self.epsilon = epsilon

    def solve(self):
        if self.f(self.lower_bound) * self.f(self.upper_bound) > 0:
            raise ValueError("Bisection method failed. Choose another interval.")

        lower_bound, upper_bound = self.lower_bound, self.upper_bound

        for iteration in range(self.max_iterations):
            midpoint = (lower_bound + upper_bound) / 2
            f_midpoint = self.f(midpoint)

            if self._check_convergence(f_midpoint):
                return round_to_two_decimals(midpoint), iteration + 1

            if self.f(lower_bound) * f_midpoint < 0:
                upper_bound = midpoint
            elif self.f(upper_bound) * f_midpoint < 0:
                lower_bound = midpoint
            else:
                raise ValueError("Bisection method failed")

        return round_to_two_decimals(midpoint), self.max_iterations

    def _check_convergence(self, f_midpoint):
        return abs(f_midpoint) < self.epsilon

class NewtonRaphsonMethod:
    def __init__(self, f, df, initial_guess, epsilon=1e-6, max_iterations=50):
        self.f = f
        self.df = df
        self.initial_guess = initial_guess
        self.epsilon = epsilon
        self.max_iterations = max_iterations

    def solve(self):
        current_approximation = self.initial_guess

        for iteration in range(self.max_iterations):
            f_current_approx = self.f(current_approximation)
            if abs(f_current_approx) < self.epsilon:
                return round_to_two_decimals(current_approximation), iteration + 1

            df_current_approx = self.df(current_approximation)
            if df_current_approx == 0:
                raise ValueError("Derivada igual a zero. Nenhuma solução encontrada")

            current_approximation = current_approximation - f_current_approx / df_current_approx

        return round_to_two_decimals(current_approximation), self.max_iterations
