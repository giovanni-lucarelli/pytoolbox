cmake_minimum_required(VERSION 3.10)

# Project name and language
project(PyPlusSci LANGUAGES CXX)

# Set C++ standard (C++17)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Set global compiler flags
add_compile_options(-Wall -Wextra -Wpedantic -Werror)

# Set the CMAKE_PREFIX_PATH to the directory where pybind11Config.cmake is located
set(CMAKE_PREFIX_PATH "/home/elena/miniconda3/lib/python3.12/site-packages/pybind11/share/cmake")

# Find pybind11
find_package(pybind11 REQUIRED)

# Find GSL
find_package(GSL REQUIRED)

# Find Boost with the JSON, system, and filesystem components
find_package(Boost REQUIRED COMPONENTS json system filesystem)

if (Boost_FOUND)
    message(STATUS "Boost found: ${Boost_INCLUDE_DIRS}")
else()
    message(FATAL_ERROR "Boost not found")
endif()


# Include directories
include_directories(include ${Boost_INCLUDE_DIRS} ${GSL_INCLUDE_DIRS})

# Add the core library (DataFrame.cpp) with -fPIC
add_library(core STATIC src/DataFrame.cpp)
set_target_properties(core PROPERTIES POSITION_INDEPENDENT_CODE ON)

# Link Boost and GSL to the core library
target_link_libraries(core PUBLIC Boost::boost Boost::json Boost::filesystem Boost::system GSL::gsl)

# Add the bindings target 
pybind11_add_module(data_frame bindings/DataFrameBindings.cpp)

# Link the core library to the Python module
target_link_libraries(data_frame PRIVATE core)

# Add the interpolation library
add_library(interpolation STATIC
    src/Interpolator.cpp
    src/LinearInterpolator.cpp
    src/NewtonInterpolator.cpp
    src/GslPolynomialInterpolator.cpp
    src/CardinalCubicSpline.cpp
)
set_target_properties(interpolation PROPERTIES POSITION_INDEPENDENT_CODE ON)

# Link Boost and GSL to the interpolation library
target_link_libraries(interpolation PUBLIC Boost::boost Boost::system GSL::gsl)

# Add the bindings target for interpolation
pybind11_add_module(interpolation_bindings bindings/InterpolationBindings.cpp)

# Link the interpolation library to the Python module
target_link_libraries(interpolation_bindings PRIVATE interpolation)


