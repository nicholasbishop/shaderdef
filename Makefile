.PHONY: doc doctest lint release test

doc: doctest
	cd docs && make html
	@echo -e "\noutput:"
	@realpath docs/_build/html/index.html

doctest:
	cd docs && make doctest

lint:
	python3 -m pylint -rn shaderdef test tools *.py

typecheck:
	python3 -m mypy demo.py

test: doctest
	cd docs && make doctest
	python3 -m unittest discover -v

release:
	python3 -m tools.release
