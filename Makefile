.PHONY: all build pip-lock pip-outdated pip-update test e2etest docs apidocs clean-pyc

all: test

build: clean-pyc
	docker-compose build --no-cache --compress app

pip-lock: clean-pyc
	docker-compose run --rm --no-deps app pipenv lock

pip-outdated: clean-pyc
	docker-compose run --rm --no-deps app pipenv update --outdated

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
