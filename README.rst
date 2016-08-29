=========
shaderdef
=========

Transform Python code into GLSL shaders.

See demo.py for a quick example of how to use the library.

This module does not currently provide any sort of shader execution
(although that would be a fun addition). It just outputs GLSL code.

License
=======

GNU GPLv3+

Documentation
=============

https://shaderdef.readthedocs.io

Implementation
==============

The builtin `ast` module is used to parse Python functions and
transform them into GLSL code.

An alternative implementation that actually evaluated the functions
and kept track of the assignment tree was dropped because regular
Python control structures can't be used.
