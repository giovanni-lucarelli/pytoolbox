from setuptools import setup, Extension, find_packages

gsl_library_dirs = ["/usr/local/lib", "/usr/lib"]  # Adjust these paths if necessary
gsl_include_dirs = ["/usr/local/include", "/usr/include"]  # Adjust paths

cpp_extensions = [
    Extension(
        "dataframe_bindings",
        sources=["bindings/DataFrameBindings.cpp", "src/DataFrame.cpp"],
        include_dirs=["include"] + gsl_include_dirs,
        library_dirs=gsl_library_dirs,
        libraries=["gsl", "gslcblas", "boost_json", "boost_system", "boost_filesystem"],  # Link GSL and CBLAS
        language="c++",
        extra_compile_args=["-std=c++17"],
    ),
    Extension(
        "interpolation_bindings",
        sources=[
            "bindings/InterpolationBindings.cpp", 
            "src/Interpolator.cpp",
            "src/LinearInterpolator.cpp",
            "src/NewtonInterpolator.cpp",
            "src/GslPolynomialInterpolator.cpp",
            "src/CardinalCubicSpline.cpp"],
        include_dirs=["include"] + gsl_include_dirs,
        library_dirs=gsl_library_dirs,
        libraries=["gsl", "gslcblas", "boost_json", "boost_system", "boost_filesystem"],
        language="c++",
        extra_compile_args=["-std=c++17"],
    ),
]

# Define the setup
setup(
    name="pytoolbox",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for interpolation and data manipulation using C++ libraries",
    packages=find_packages(),  # Look for packages in pytoolbox directory
    package_dir={"": "."},  # Points to the python folder as 
    ext_modules=cpp_extensions,
    install_requires=["numpy", "pandas", "seaborn", "matplotlib", "scipy"],
    python_requires=">=3.7",
)
