from setuptools import setup, Extension, find_packages

gsl_library_dirs = ["/usr/local/lib", "/usr/lib"]  # Adjust these paths if necessary
gsl_include_dirs = ["/usr/local/include", "/usr/include"]  # Adjust paths

cpp_extensions = [
    Extension(
<<<<<<< HEAD
<<<<<<< HEAD
        "dataframe_bindings",
=======
        "mytoolbox.data_frame",
>>>>>>> fef7517 (new version. TODO: include elena's code)
=======
        "dataframe_bindings",
>>>>>>> a959075 (everything is working (of dataframe))
        sources=["bindings/DataFrameBindings.cpp", "src/DataFrame.cpp"],
        include_dirs=["include"] + gsl_include_dirs,
        library_dirs=gsl_library_dirs,
        libraries=["gsl", "gslcblas", "boost_json", "boost_system", "boost_filesystem"],  # Link GSL and CBLAS
        language="c++",
    ),
    Extension(
<<<<<<< HEAD
<<<<<<< HEAD
        "interpolation_bindings",
=======
        "mytoolbox.interpolation_bindings",
>>>>>>> fef7517 (new version. TODO: include elena's code)
=======
        "interpolation_bindings",
>>>>>>> a959075 (everything is working (of dataframe))
        sources=["bindings/InterpolationBindings.cpp", "src/Interpolator.cpp"],
        include_dirs=["include"] + gsl_include_dirs,
        library_dirs=gsl_library_dirs,
        libraries=["gsl", "gslcblas", "boost_json", "boost_system", "boost_filesystem"],
        language="c++",
    ),
]

<<<<<<< HEAD
<<<<<<< HEAD
# Define the setup
setup(
    name="pytoolbox",
=======
# Read long description from README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the setup
setup(
    name="mytoolbox",
>>>>>>> fef7517 (new version. TODO: include elena's code)
=======
# Define the setup
setup(
    name="pytoolbox",
>>>>>>> a959075 (everything is working (of dataframe))
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for interpolation and data manipulation using C++ libraries",
<<<<<<< HEAD
<<<<<<< HEAD
    packages=find_packages(where="pytoolbox"),  # Look for packages in pytoolbox directory
    package_dir={"": "pytoolbox"},  # Points to the python folder as 
=======
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mytoolbox",  # Update with your repo
    packages=find_packages(),
>>>>>>> fef7517 (new version. TODO: include elena's code)
=======
    packages=find_packages(where="pytoolbox"),  # Look for packages in pytoolbox directory
    package_dir={"": "pytoolbox"},  # Points to the python folder as 
>>>>>>> a959075 (everything is working (of dataframe))
    ext_modules=cpp_extensions,
    install_requires=["numpy", "pandas", "seaborn", "matplotlib", "scipy"],
    python_requires=">=3.7",
)
