try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(name='whatis',
      version='0.0',
      packages=find_packages(), #fix
      description='Sequential model-based optimization toolbox.')