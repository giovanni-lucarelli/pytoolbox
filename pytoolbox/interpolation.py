import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt 


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

