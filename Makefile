.PHONY: test

lint:
	pylint -rn shaderdef test demo.py

test:
	python -m unittest discover -v
