import sys

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup, find_packages, Extension

__version__ = "0.0.1"

ext_modules = [
    
    Pybind11Extension("pypolymer.util.topo_tools_cpp",
        ["pypolymer/util/topoTools.cpp"],
        define_macros = [('VERSION_INFO', __version__)], 
        include_dirs = ["/usr/include/eigen3"],
        ),   
     
    Pybind11Extension("pypolymer.util.geometry_approximation_cpp",
        ["pypolymer/util/geometry_approximate.cpp"],
        define_macros = [('VERSION_INFO', __version__)],
        include_dirs = ["/usr/include/eigen3"],
        ),
]

setup(
    name="PyPolymer",
    version=__version__,
    author="Even Wong",
    author_email="evenwong@stu.cdut.edu.cn",
    url="https://github.com/???",
    description="A tookit for polymer construction & analysis.",
    long_description="",
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    cmdclass={"build_ext": build_ext},
    packages = find_packages(),
    zip_safe=False,
    python_requires=">=3.6",
        install_requires = [
        'matplotlib',
        'numpy',
        'scipy',
        'numba',
        'gsd',
        'seaborn',
        'pybind11[global]',
        ],
)
