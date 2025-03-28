# ***************************************************************************************************************************************************
#  *Author           : Ananthan.A - 286739
#  *File             : setup.py
#  *Title            : Python String Operations Module Development
#  *Description      : This file is used for packaging the module
#  ****************************************************************************************************************************************************

from setuptools import setup, find_packages

setup(
    name='strops',
    version='0.1',
    description='A Python module for various string operations',
    author='Ananthan.A',
    author_email='ananthan.a@ust.com',
    packages=find_packages(),
    install_requires=[],  
    classifiers=['Programming Language :: Python :: 3', 'License :: OSI Approved :: MIT License', 'Operating System :: OS Independent',],
    python_requires='>=3.6',
)
