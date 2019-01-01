.PHONY: all test docs clean-pyc

all: test

build: clean-pyc
	docker-compose build --no-cache --compress app

lock: clean-pyc
	docker-compose run --rm --no-deps app pipenv lock

test: clean-pyc
	-docker-compose run --rm --no-deps app pipenv run pytest

e2etest: clean-pyc
	-docker-compose run --rm --no-deps app pipenv run pytest e2etests/

docs: clean-pyc
	docker-compose run --rm --no-deps app pipenv run make -C docs html

apidocs: clean-pyc
	docker-compose run --rm --no-deps app pipenv run sphinx-apidoc -f -o docs/source src/cerberusauth

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
