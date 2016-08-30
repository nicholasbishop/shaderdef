.PHONY: doc lint release test

doc:
	cd docs && make html
	@echo -e "\noutput:"
	@realpath docs/_build/html/index.html

lint:
	python3 -m pylint -rn shaderdef test tools *.py

typecheck:
	python3 -m mypy demo.py

test:
	python3 -m unittest discover -v

release:
	python3 -m tools.release
