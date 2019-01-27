.PHONY: all build pipenv-lock test e2etest docs apidocs clean-pyc

all: test

build: clean-pyc
	docker-compose build --no-cache --compress app

pipenv-lock: clean-pyc
	docker-compose run --rm --no-deps app pipenv lock

test: clean-pyc
	-docker-compose run --rm --no-deps app pipenv run pytest -m "not e2etest"

xtest: clean-pyc
	-docker-compose run --rm --no-deps app pipenv run pytest -m "not e2etest" -x --ff

e2etest: clean-pyc
	-docker-compose run --rm app pipenv run pytest -m e2etest

docs: clean-pyc
	docker-compose run --rm --no-deps app pipenv run make -C docs html

apidocs: clean-pyc
	docker-compose run --rm --no-deps app pipenv run sphinx-apidoc -f -o docs/source src/cerberusauth

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
