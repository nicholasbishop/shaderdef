.PHONY: test

lint:
	python3 -m pylint -rn shaderdef test tools *.py

test:
	python3 -m unittest discover -v
