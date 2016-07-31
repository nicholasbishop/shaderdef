#! /usr/bin/env python

from setuptools import setup
from tools import version_util


setup(name='shaderdef',
      version=version_util.load_version_as_string(),
      description='Transform Python code into GLSL shaders',
      url='https://github.com/nicholasbishop/shaderdef',
      author='Nicholas Bishop',
      author_email='nicholasbishop@gmail.com',
      license='GNU General Public License v3 or later (GPLv3+)',
      packages=['shaderdef', 'tools'],
      test_suite='test',
      zip_safe=True)
