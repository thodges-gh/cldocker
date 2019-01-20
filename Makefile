install:
	pip3 install --user -r requirements.txt

setup:
	python3 main.py

clean:
	python3 main.py clean

pull-chainlink:
	python3 main.py pull chainlink

pull-geth:
	python3 main.py pull geth

pull-parity:
	python3 main.py pull parity

test:
	py.test tests -v

.PHONY: install setup clean pull-chainlink pull-geth pull-parity test