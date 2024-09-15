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

            self._print_iteration(iteration, lower_bound, upper_bound, root_approx, self.f(lower_bound), self.f(upper_bound), f_approx)

            if self._check_convergence(f_approx):
                print(f"Valor aproximado de f(x) = 0 é {f_approx:.6f}")
                return round_to_two_decimals(root_approx)

            if self.f(lower_bound) * f_approx < 0:
                upper_bound = root_approx
            elif self.f(upper_bound) * f_approx < 0:
                lower_bound = root_approx
            else:
                raise ValueError("False position method failed")

        print(f"Valor aproximado de f(x) = 0 é {f_approx:.6f}")
        return round_to_two_decimals(root_approx)

    def _print_iteration(self, iteration, lower_bound, upper_bound, root_approx, f_lower_bound, f_upper_bound, f_approx):
        print(f"Iteração: {iteration}")
        print(f"a = {lower_bound}, f(a) = {f_lower_bound:.6f}")
        print(f"b = {upper_bound}, f(b) = {f_upper_bound:.6f}")
        print(f"xm = {root_approx:.6f}, f(x) = {f_approx:.6f}")

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

            self._print_iteration(iteration, lower_bound, upper_bound, midpoint, self.f(lower_bound), self.f(upper_bound), f_midpoint)

            if self._check_convergence(f_midpoint):
                print(f"Valor aproximado de f(x) = 0 é {f_midpoint:.6f}")
                return round_to_two_decimals(midpoint)

            if self.f(lower_bound) * f_midpoint < 0:
                upper_bound = midpoint
            elif self.f(upper_bound) * f_midpoint < 0:
                lower_bound = midpoint
            else:
                raise ValueError("Bisection method failed")

        print(f"Valor aproximado de f(x) = 0 é {f_midpoint:.6f}")
        return round_to_two_decimals(midpoint)

    def _print_iteration(self, iteration, lower_bound, upper_bound, midpoint, f_lower_bound, f_upper_bound, f_midpoint):
        print(f"Iteração: {iteration}")
        print(f"a = {lower_bound}, f(a) = {f_lower_bound:.6f}")
        print(f"b = {upper_bound}, f(b) = {f_upper_bound:.6f}")
        print(f"xm = {midpoint:.6f}, f(x) = {f_midpoint:.6f}")

    def _check_convergence(self, f_midpoint):
        return abs(f_midpoint) < self.epsilon