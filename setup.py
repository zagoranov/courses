from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='courses',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(), install_requires=['django']
)
