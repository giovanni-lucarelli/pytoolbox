import numpy as np
import time
from scipy.interpolate import CubicSpline

# ------------------------- If building through CMake ------------------------ #

# import sys
# sys.path.append('../build')
# import interpolation_bindings # Importa el módulo que contiene los bindings de C++

# ---------------------------------------------------------------------------- #

try:
    import interpolation_bindings
except ImportError as e:
    raise ImportError(
        "Failed to import 'interpolation_bindings'. Ensure it is built and installed."
    ) from e

class Interpolator: 
    def __init__(self, x_nodes, y_nodes):

        self.x_nodes = x_nodes 
        self.y_nodes = y_nodes
        
        # Create the instances of the interpolators (using the classes exposed by pybind11)
        self.linear_interpolator = interpolation_bindings.LinearInterpolator(x_nodes, y_nodes)
        self.newton_interpolator = interpolation_bindings.NewtonInterpolator(x_nodes, y_nodes)
        self.gsl_polynomial_interpolator = interpolation_bindings.GslPolynomialInterpolator(x_nodes, y_nodes)
        self.cubic_spline_interpolator = interpolation_bindings.CardinalCubicSpline(x_nodes, y_nodes, x_nodes[0], x_nodes[1]-x_nodes[0] )  # Por ejemplo, los parámetros pueden variar según tu implementación

    def linear_interpolate(self, x):

        return self.linear_interpolator(x)

    def newton_interpolate(self, x):

        return self.newton_interpolator(x)
    
    def gsl_polynomial_interpolate(self, x):

        return self.gsl_polynomial_interpolator(x)

    def cubic_spline_interpolate(self, x):
        
        return self.cubic_spline_interpolator(x)
    
def calculate_errors(real_values, interpolated_values):
    absolute_errors = np.abs(real_values-interpolated_values)
    relative_errors = np.abs(absolute_errors/real_values)
    mae = np.mean(absolute_errors)
    return absolute_errors, relative_errors, mae

def generate_data(func, x_range, num_points, exclude_extremes = False):
    if exclude_extremes:
        epsilon = 1e-5
        x = np.linspace(x_range[0] + epsilon, x_range[1] - epsilon, num_points)
    else:
        x = x = np.linspace(x_range[0], x_range[1], num_points)
    y = func(x)
    return x, y

def measure_execution_time(func, *args, **kwargs):
    """
    Measures the execution time of the function passed as an argument.

    Parameters:
    - func: the function to be executed.
    - *args: positional arguments that the function may require.
    - **kwargs: keyword arguments that the function may require.

    Returns:
    - The execution time in seconds.
    """
    start_time = time.time() 
    func(*args, **kwargs) 
    end_time = time.time() 
    
    return end_time - start_time  

# Implementing interpolations in pure Python (I think it is unnecessary)
def linear_interpolation(x_nodes, y_nodes, x):
    """
    Realiza la interpolación lineal para un valor x dado, usando nodos x_nodes y valores y_nodes.
    """
    n = len(x_nodes)
    for i in range(n - 1):
        if x_nodes[i] <= x <= x_nodes[i + 1]:
            return y_nodes[i] + (x - x_nodes[i]) * (y_nodes[i + 1] - y_nodes[i]) / (x_nodes[i + 1] - x_nodes[i])
    return None
def newton_interpolation(x_nodes, y_nodes, x):
    """
    Realiza la interpolación de Newton para un valor x dado.
    """
    n = len(x_nodes)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_nodes

    # Construir la tabla de diferencias divididas
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i, j] = (diff_table[i + 1, j - 1] - diff_table[i, j - 1]) / (x_nodes[i + j] - x_nodes[i])

    # Evaluar el polinomio de Newton
    result = diff_table[0, 0]
    for j in range(1, n):
        term = diff_table[0, j]
        for i in range(j):
            term *= (x - x_nodes[i])
        result += term
    return result
def lagrange_interpolation(x_nodes, y_nodes, x):
    """
    Realiza la interpolación de Lagrange para un valor x dado.
    """
    n = len(x_nodes)
    result = 0
    for i in range(n):
        term = y_nodes[i]
        for j in range(n):
            if j != i:
                term *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term
    return result
def cubic_spline_interpolation(x_nodes, y_nodes, x):
    """
    Realiza la interpolación de splines cúbicos para un valor x dado.
    """
    cs = CubicSpline(x_nodes, y_nodes)
    return cs(x)
