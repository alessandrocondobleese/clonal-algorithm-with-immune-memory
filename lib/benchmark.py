import numpy

from numpy.typing import NDArray


def sphere(X: NDArray[numpy.float64]) -> numpy.floating:
    """
    Sphere function.
    f(x) = sum(x_i^2)
    """
    return numpy.sum(X**2)


def griewank(X: NDArray[numpy.float64]) -> numpy.floating:
    """
    Griewank function.
    f(x) = 1 + sum(x_i^2 / 4000) - prod(cos(x_i / sqrt(i+1)))
    """
    term_1 = numpy.sum(X**2) / 4000
    term_2 = numpy.prod(numpy.cos(X / numpy.sqrt(numpy.arange(1, X.size + 1))))
    return term_1 - term_2 + 1


def rastrigin(X: NDArray[numpy.float64]) -> numpy.floating:
    """
    Rastrigin function.
    f(x) = 10 * n + sum(x_i^2 - 10 * cos(2 * pi * x_i))
    """
    D = X.size
    return 10 * D + numpy.sum(X**2 - 10 * numpy.cos(2 * numpy.pi * X))


def rosenbrock(X: NDArray[numpy.float64]) -> numpy.floating:
    """
    Rosenbrock function.
    f(x) = sum(100 * (x_i+1 - x_i^2)^2 + (x_i - 1)^2)
    """
    return numpy.sum(100 * (X[1:] - X[:-1] ** 2) ** 2 + (X[:-1] - 1) ** 2)


def ackley(X: NDArray[numpy.float64]) -> numpy.floating:
    """
    Ackley function.
    f(x) = -20 * exp(-0.2 * sqrt(sum(x_i^2) / n))
           - exp(sum(cos(2 * pi * x_i)) / n)
           + 20 + e
    """
    D = X.size
    term_1 = -1 * 20 * numpy.exp(-1 * 0.2 * numpy.sqrt(numpy.sum(X**2) / D))
    term_2 = -1 * numpy.exp(numpy.sum(numpy.cos(2 * numpy.pi * X)) / D)
    return term_1 + term_2 + 20 + numpy.e
