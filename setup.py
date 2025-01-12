from setuptools import setup, Extension, find_packages

gsl_library_dirs = ["/usr/local/lib", "/usr/lib"]  # Adjust these paths if necessary
gsl_include_dirs = ["/usr/local/include", "/usr/include"]  # Adjust paths

cpp_extensions = [
    Extension(
        "mytoolbox.data_frame",
        sources=["bindings/DataFrameBindings.cpp", "src/DataFrame.cpp"],
        include_dirs=["include"] + gsl_include_dirs,
        library_dirs=gsl_library_dirs,
        libraries=["gsl", "gslcblas", "boost_json", "boost_system", "boost_filesystem"],  # Link GSL and CBLAS
        language="c++",
    ),
    Extension(
        "mytoolbox.interpolation_bindings",
        sources=["bindings/InterpolationBindings.cpp", "src/Interpolator.cpp"],
        include_dirs=["include"] + gsl_include_dirs,
        library_dirs=gsl_library_dirs,
        libraries=["gsl", "gslcblas", "boost_json", "boost_system", "boost_filesystem"],
        language="c++",
    ),
]

# Read long description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the setup
setup(
    name="mytoolbox",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for interpolation and data manipulation using C++ libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mytoolbox",  # Update with your repo
    packages=find_packages(),
    ext_modules=cpp_extensions,
    install_requires=["numpy", "pandas", "seaborn", "matplotlib", "scipy"],
    python_requires=">=3.7",
)
