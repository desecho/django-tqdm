.DEFAULT_GOAL := help

include help.mk

SHELL := /bin/bash
SOURCE_CMD := source venv/bin/activate

#------------------------------------
# Installation
#------------------------------------

.PHONY: install-deps
## Install dependencies | Installation
install-deps:
	# Install Python
	sudo apt install python3.9 python3.9-venv python3.9-dev -y

.PHONY: create-venv
## Create virtual environment and install requirements
create-venv:
	python3.9 -m venv venv
	${SOURCE_CMD} && \
		pip install -r requirements-dev.txt && \
		pip install -e .

.PHONY: bootstrap
## Bootstrap project
bootstrap: install-deps create-venv
#------------------------------------


#------------------------------------
# Tox
#------------------------------------
.PHONY: test
## Run tests | Tests
test:
	tox

.PHONY: pydiatra
## Run pydiatra linter
pydiatra:
	scripts/pydiatra.sh

.PHONY: pylint
## Run pylint linter
pylint:
	tox -e py-pylint

.PHONY: flake8
## Run flake8 linter
flake8:
	tox -e py-flake8

.PHONY: isort
## Run isort linter
isort:
	tox -e py-isort

.PHONY: bandit
## Run bandit linter
bandit:
	tox -e py-bandit

.PHONY: rstlint
## Run rstlint linter
rstlint:
	tox -e py-rstlint

.PHONY: pydocstyle
## Run pydocstyle linter
pydocstyle:
	tox -e py-pydocstyle

.PHONY: safety
## Run safety linter
safety:
	tox -e py-safety

.PHONY: pytest
## Run pytest
pytest:
	tox -e py-pytest

.PHONY: black
## Run black linter
black:
	tox -e py-black

.PHONY: shfmt
## Run shfmt linter
shfmt:
	tox -e py-shfmt

.PHONY: shellcheck
## Run shellcheck linter
shellcheck:
	shellcheck scripts/*.sh

#------------------------------------

#------------------------------------
# Development
#------------------------------------
.PHONY: update-venv
## Update packages in venv and tox with current requirements | Development
update-venv:
	${SOURCE_CMD} && \
	pip install -r requirements-dev.txt && \
	pip install -e . && \
	deactivate && \
	source .tox/py/bin/activate && \
	pip install -r requirements-dev.txt && \
	pip install -e .

.PHONY: format
## Format code
format:
	${SOURCE_CMD} && \
	autoflake --remove-all-unused-imports --in-place -r django_tqdm && \
	isort django_tqdm && \
	black .
	shfmt -l -w .
#------------------------------------
