.PHONY: install upgrade flake8 coverage travis pylint bandit restructuredtext pydocstyle

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

bandit:
	bandit -r django_tqdm --exclude django_tqdm/tests

coverage:
	py.test --cov-report term-missing --cov django_tqdm --verbose

restructuredtext:
	python setup.py check --restructuredtext --metadata --strict

pydocstyle:
	pydocstyle --count

travis: install pylint flake8 isort bandit restructuredtext pydocstyle coverage
