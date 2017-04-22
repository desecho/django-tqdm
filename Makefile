.PHONY: install upgrade flake8 coverage travis

install:
	pip install -r requirements-dev.txt
	pip install -e .

upgrade:
	pip install -r requirements-dev.txt -U
	pip install -e . -U

flake8:
	flake8

isort:
	isort --check-only --recursive --diff django_tqdm

coverage:
	py.test --cov-report term-missing --cov django_tqdm

travis: install flake8 isort coverage
