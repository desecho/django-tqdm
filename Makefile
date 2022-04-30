.DEFAULT_GOAL := help

include help.mk

SHELL := /bin/bash
SOURCE_CMD := source venv/bin/activate
PYTHON := python3.10

#------------------------------------
# Installation
#------------------------------------
SHFMT_VERSION := 3.4.3
SHFMT_PATH := /usr/local/bin/shfmt

.PHONY: install-shfmt
## Install shfmt | Installation
install-shfmt:
	sudo curl https://github.com/mvdan/sh/releases/download/v${SHFMT_VERSION}/shfmt_v${SHFMT_VERSION}_linux_amd64 -Lo ${SHFMT_PATH}
	sudo chmod +x ${SHFMT_PATH}

.PHONY: install-twine
## Install twine
install-twine:
	sudo pip3 install twine

.PHONY: install-test-deps
## Install test dependencies
install-test-deps: install-shfmt
	sudo apt install shellcheck -y
	sudo pip3 install tox
	sudo npm install -g markdownlint-cli

.PHONY: install-deps
## Install dependencies
install-deps:
	# Install Python
	sudo apt install ${PYTHON} ${PYTHON}-venv ${PYTHON}-dev -y

.PHONY: create-venv
## Create virtual environment and install requirements
create-venv:
	${PYTHON} -m venv venv
	${SOURCE_CMD} && \
		pip install -r requirements-dev.txt && \
		pip install -e .

.PHONY: bootstrap
## Bootstrap project
bootstrap: install-deps install-test-deps create-venv
#------------------------------------

#------------------------------------
# Scripts
#------------------------------------
.PHONY: pydiatra-script
pydiatra-script:
	scripts/pydiatra.sh
#------------------------------------

#------------------------------------
# Tests
#------------------------------------
.PHONY: test
## Run tests | Tests
test: shfmt shellcheck markdownlint tox

.PHONY: tox
## Run tox
tox:
	tox

.PHONY: pydiatra
## Run pydiatra linter
pydiatra:
	tox -e py-pydiatra

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

.PHONY: yamllint
## Run yamllint linter
yamllint:
	tox -e py-yamllint

.PHONY: mypy
## Run mypy linter
mypy:
	tox -e py-mypy

.PHONY: shfmt
## Run shfmt linter
shfmt:
	shfmt -l -d .

.PHONY: shellcheck
## Run shellcheck linter
shellcheck:
	shellcheck scripts/*.sh

.PHONY: markdownlint
## Run markdownlint linter
markdownlint:
	markdownlint CHANGELOG.md developer_doc.md
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
	isort django_tqdm demos tests && \
	black .
	shfmt -l -w .
	markdownlint CHANGELOG.md developer_doc.md --fix
#------------------------------------

#------------------------------------
# Commands
#------------------------------------
.PHONY: build-wheel
## Build wheel | Commands
build-wheel:
	python3 setup.py bdist_wheel
#------------------------------------
