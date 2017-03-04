.PHONY: build test

all: test

test:
	@python -m pip install -q -r requirements.txt -r requirements-dev.txt
	@python -m pytest

build: test
	@python setup.py build
