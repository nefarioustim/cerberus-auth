.PHONY: all test docs clean-pyc

all: test

build: clean-pyc
	docker-compose build --no-cache --compress app

lock: clean-pyc
	docker-compose run --rm --no-deps app pipenv lock

test: clean-pyc
	docker-compose run --rm --no-deps app pipenv run pytest

docs: clean-pyc
	docker-compose run --rm --no-deps app pipenv run make -C docs html

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +