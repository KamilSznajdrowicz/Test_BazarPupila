.PHONY: deps tests
RUNTEST=python -m unittest -v -b
ALLMODULES=$(patsubst %.py, %.py, $(wildcard test_*.py))


deps:
	pip install -r requirements.txt

tests:
	${RUNTEST} ${ALLMODULES}

test_%: Tests.test_%.py
	${RUNTEST} Tests.test_%.py
