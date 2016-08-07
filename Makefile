.PHONY: build test

all: build

test:
	@python3 -m pip install -q -r requirements-dev.txt
	@python3 -m pytest

build: test
	@python setup.py build
	@python -m pytest
