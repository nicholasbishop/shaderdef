.PHONY: gen_glsl_types lint release test

lint:
	python3 -m pylint -rn shaderdef test tools *.py

test:
	python3 -m unittest discover -v

release:
	python3 -m tools.release

gen_glsl_types:
	python3 -m tools.generate_glsl_types > glsl_types.py
	python3 -m pylint -rn glsl_types -d invalid-name,too-many-lines,too-many-public-methods
	mypy glsl_types.py
