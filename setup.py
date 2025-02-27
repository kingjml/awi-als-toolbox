# -*- coding: utf-8 -*-

from Cython.Build import cythonize
from Cython.Distutils import build_ext

from setuptools.extension import Extension
from setuptools import setup, find_packages

import numpy
import os

# Get the readme
with open('README.rst') as f:
    readme = f.read()

# Get the licence
with open('LICENSE') as f:
    license = f.read()

# Get the version
mypackage_root_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(mypackage_root_dir, "awi_als_toolbox", 'VERSION')) as version_file:
    version = version_file.read().strip()

# Package requirements
with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name='awi-als-toolbox',
    version=version,
    description='python sea ice radar altimetry processing library',
    long_description=readme,
    author='Stefan Hendricks',
    author_email='stefan.hendricks@awi.de',
    url='https://github.com/shendric/pysiral',
    license=license,
    install_requires=requirements,
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True
)