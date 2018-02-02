.PHONY: install upgrade flake8 coverage travis pylint

install:
	pip install -r requirements-dev.txt
	pip install -e .

upgrade:
	pip install -r requirements-dev.txt -U
	pip install -e . -U

flake8:
	flake8

pylint:
	pylint django_tqdm

isort:
	isort --check-only --recursive --diff django_tqdm

coverage:
	py.test --cov-report term-missing --cov django_tqdm --verbose

travis: install pylint flake8 isort coverage
