#https://www.codewars.com/kata/591748b3f014a2593d0000d9/train/python
class Datamining:
    def __init__(self, train_set, degree=5):
        self.coefficients = self.train(train_set, degree)

    def train(self, train_set, degree):
        x_values = [point[0] for point in train_set]
        y_values = [point[1] for point in train_set]
        coefficients = self.polyfit(x_values, y_values, degree)

        return coefficients

    def polyfit(self, x, y, degree):
        n = len(x)
        X = [sum(x_i ** j for x_i in x) for j in range(2 * degree + 1)]
        Y = [sum(y_i * x_i ** j for x_i, y_i in zip(x, y)) for j in range(degree + 1)]

        A = [[X[i + j] for j in range(degree + 1)] for i in range(degree + 1)]

        # Gaussian elimination
        for i in range(degree + 1):
            max_row = max(range(i, degree + 1), key=lambda j: abs(A[j][i]))
            A[i], A[max_row] = A[max_row], A[i]
            Y[i], Y[max_row] = Y[max_row], Y[i]

            for j in range(i + 1, degree + 1):
                factor = A[j][i] / A[i][i]
                Y[j] -= factor * Y[i]
                for k in range(i, degree + 1):
                    A[j][k] -= factor * A[i][k]

        coefficients = [0] * (degree + 1)
        for i in range(degree, -1, -1):
            coefficients[i] = Y[i] / A[i][i]
            for j in range(i - 1, -1, -1):
                Y[j] -= A[j][i] * coefficients[i]
        return coefficients

    def predict(self, x):
        return sum(c * x ** i for i, c in enumerate(self.coefficients))