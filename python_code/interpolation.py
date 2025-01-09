import interpolation_bindings # Importa el módulo que contiene los bindings de C++

class Interpolator: 
    #Inicializa el interpolador con los nodos de x e y.
    def __init__(self, x_nodes, y_nodes):

        self.x_nodes = x_nodes
        self.y_nodes = y_nodes
        
        # Crear las instancias de los interpoladores (usando las clases expuestas por pybind11)
        self.linear_interpolator = interpolation_bindings.LinearInterpolator(x_nodes, y_nodes)
        self.newton_interpolator = interpolation_bindings.NewtonInterpolator(x_nodes, y_nodes)
        self.gsl_polynomial_interpolator = interpolation_bindings.GslPolynomialInterpolator(x_nodes, y_nodes)
        self.cubic_spline_interpolator = interpolation_bindings.CardinalCubicSpline(x_nodes, y_nodes, 0.0, 0.0)  # Por ejemplo, los parámetros pueden variar según tu implementación

    def linear_interpolate(self, x):

        return self.linear_interpolator(x)

    def newton_interpolate(self, x):

        return self.newton_interpolator(x)
    
    def gsl_polynomial_interpolate(self, x):

        return self.gsl_polynomial_interpolator(x)

    def cubic_spline_interpolate(self, x):
        
        return self.cubic_spline_interpolator(x)