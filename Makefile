install:
	pip3 install --user -r requirements.txt

setup:
	python3 main.py

clean:
	python3 main.py clean

pull-cl:
	python3 main.py pull chainlink

pull-geth:
	python3 main.py pull geth

pull-parity:
	python3 main.py pull parity

restart-eth:
	python3 main.py restart-eth

stop-eth:
	python3 main.py stop-eth

logs-eth:
	python3 main.py logs-eth

start-cl:
	python3 main.py start-cl

update-cl:
	python3 main.py update-cl

stop-cl:
	python3 main.py stop-cl

logs-cl:
	python3 main.py logs-cl

logs:
	python3 main.py logs

test:
	py.test tests -v

info:
	docker version
	python3 --version
	pip3 -V

.PHONY: install setup clean pull-chainlink pull-geth pull-parity restart-eth stop-eth logs-eth start-cl update-cl stop-cl logs-cl logs test info