#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "Interpolator.hpp"
#include "LinearInterpolator.hpp"
#include "NewtonInterpolator.hpp"
#include "GslPolynomialInterpolator.hpp"
#include "CardinalCubicSpline.hpp"

namespace py = pybind11;

PYBIND11_MODULE(interpolation_bindings, m) {

    // Exponer la clase Interpolator (abstracta)
    py::class_<Interpolator>(m, "Interpolator")
        .def("set_data", &Interpolator::setData,
            R"(Set the interpolation data points
            
            Parameters:
                x (list of float): the x-coordinates of the data points
                y (list of float): the y-coordinates of the data points
            )")  
        .def("check_range", &Interpolator::checkRange,
            R"(Check if a value is whithin the interpolation range
            
            Parameters:
                x (float): the value to check
            
            Raises:
                ValueError: if the value is outside the interpolation range
            )");

    // Exponer la clase LinearInterpolator (derivada)
    py::class_<LinearInterpolator, Interpolator>(m, "LinearInterpolator")
        .def(py::init<const std::vector<double>&, const std::vector<double>&>(),
           R"(Constructor for the LinearInterpolator class

            Parameters:
                x (list of float): the x-coordinates of the data points
                y (list of float): the y-coordinates of the data points
            )")
        .def("__call__", &LinearInterpolator::operator(),
            R"(Perform linear interpolation
            
            Parameters:
                x(float): the x-coordinate to interpolate
            
            Returns:
                float: the interpolated y-value at x
            )");

    // Exponer la clase NewtonInterpolator (derivada)
    py::class_<NewtonInterpolator, Interpolator>(m, "NewtonInterpolator")
        .def(py::init<const std::vector<double>&, const std::vector<double>&>(),
            R"(Constructor for the NewtonInterpolator class
            
                Parameters:
                    x (list of float): the x-coordinates of the data points
                    y (list of float): the y-coordinates of the data points
            )")
        .def("__call__", &NewtonInterpolator::operator(),
            R"(Perform Newton interpolation
            
            Parameters:
                x(float): the x-coordinate to interpolate
            
            Returns:
                float: the interpolated y-value at x
            )");       

    // Exponer la clase GslPolynomialInterpolator (derivada)
    py::class_<GslPolynomialInterpolator, Interpolator>(m, "GslPolynomialInterpolator")
        .def(py::init<const std::vector<double>&, const std::vector<double>&>(),
            R"(Constructor for the GslPolynomialInterpolator class
            
                Parameters:
                    x (list of float): the x-coordinates of the data points
                    y (list of float): the y-coordinates of the data points
            )")
        .def("__call__", &GslPolynomialInterpolator::operator(),
            R"(Perform polynomial interpolation using GSL
            
            Parameters:
                x(float): the x-coordinate to interpolate
            
            Returns:
                float: the interpolated y-value at x
            )");       

    // Exponer la clase CardinalCubicSpline (derivada)
    py::class_<CardinalCubicSpline, Interpolator>(m, "CardinalCubicSpline")
        .def(py::init<const std::vector<double>&, const std::vector<double>&, double, double>(),
            R"(Constructor for the CardinalCubicSpline class

            Parameters:
                x (list of float): The x-coordinates of the data points
                y (list of float): The y-coordinates of the data points
                start (float): The start point for the spline
                step (float): The step size between x points
            )")
        .def("__call__", &CardinalCubicSpline::operator(),
            R"(Perform cubic spline interpolation

            Parameters:
                x (float): The x-coordinate to interpolate

            Returns:
                float: The interpolated y-value at x
            )");
}