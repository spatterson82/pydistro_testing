#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='pydistro_testing',
      version='1.0',
      description='Testing open-source publishing',
      author='Stephen Patterson',
      author_email='spatterson82@hotmail.com',
      url='https://github.com/spatterson82/pydistro_testing',
      packages=find_packages(include=['pydistro_testing', 'pydistro_testing.*']),
     )