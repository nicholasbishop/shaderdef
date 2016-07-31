#! /usr/bin/env python

from setuptools import setup

setup(name='shaderdef',
      version='0.5.2',
      description='Transform Python code into GLSL shaders',
      url='https://github.com/nicholasbishop/shaderdef',
      author='Nicholas Bishop',
      author_email='nicholasbishop@gmail.com',
      license='GNU General Public License v3 or later (GPLv3+)',
      packages=['shaderdef'],
      test_suite='test',
      zip_safe=True)
