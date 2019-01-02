install:
	pip install -r requirements.txt

setup:
	python main.py

test:
	py.test tests -v

.PHONY: install setup test