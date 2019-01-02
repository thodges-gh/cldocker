install:
	pip3 install --user -r requirements.txt

setup:
	python3 main.py

test:
	py.test tests -v

.PHONY: install setup test