install:
	pip3 install --user -r requirements.txt

setup:
	python3 main.py

clean:
	python3 main.py clean

test:
	py.test tests -v

.PHONY: install clean setup test