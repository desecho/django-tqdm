.DEFAULT_GOAL := help

include makefiles/colors.mk
include makefiles/help.mk
include makefiles/macros.mk

SHELL := /bin/bash
SOURCE_CMD := source venv/bin/activate
PYTHON := python3.10

#------------------------------------
# Installation
#------------------------------------
BIN_DIR := /usr/local/bin

SHFMT_VERSION := 3.4.3
SHFMT_PATH    := ${BIN_DIR}/shfmt

.PHONY: install-shfmt
## Install shfmt | Installation
install-shfmt:
	$(call print,Installing shfmt)
	@sudo curl https://github.com/mvdan/sh/releases/download/v${SHFMT_VERSION}/shfmt_v${SHFMT_VERSION}_linux_amd64 -Lo ${SHFMT_PATH}
	@sudo chmod +x ${SHFMT_PATH}

ACTIONLINT_VERSION := 1.6.13
ACTIONLINT_PATH    := ${BIN_DIR}/actionlint
ACTIONLINT_URL     := https://github.com/rhysd/actionlint/releases/download/v${ACTIONLINT_VERSION}/actionlint_${ACTIONLINT_VERSION}_linux_amd64.tar.gz
ACTIONLINT_TMP_DIR := $(shell mktemp -d)
ACTIONLINT_ARCHIVE := actionlint.tar.gz

.PHONY: install-actionlint
## Install actionlint
install-actionlint:
	$(call print,Installing actionlint)
	@cd ${ACTIONLINT_TMP_DIR} && \
	curl ${ACTIONLINT_URL} -Lo ${ACTIONLINT_ARCHIVE} && \
	tar -xvf ${ACTIONLINT_ARCHIVE} && \
	sudo mv actionlint ${ACTIONLINT_PATH}

.PHONY: install-twine
## Install twine
install-twine:
	$(call print,Installing twine)
	@sudo pip3 install twine

.PHONY: install-test-deps
## Install test dependencies
install-test-deps: install-shfmt install-actionlint
	$(call print,Installing shellcheck)
	@sudo apt install shellcheck -y
	$(call print,Installing tox)
	@sudo pip3 install tox
	$(call print,Installing markdownlint-cli)
	@sudo npm install -g markdownlint-cli

.PHONY: install-deps
## Install dependencies
install-deps:
	$(call print,Installing Python)
	@sudo apt install ${PYTHON} ${PYTHON}-venv ${PYTHON}-dev -y

.PHONY: create-venv
## Create virtual environment and install requirements
create-venv:
	$(call print,Creating venv)
	${PYTHON} -m venv venv
	${SOURCE_CMD} && \
		pip install -r requirements-dev.txt && \
		pip install -e .

.PHONY: create-tox-venv
create-tox-venv:
	$(call print,Creating tox venv and installing requirements)
	@tox -e py-requirements

.PHONY: create-venvs
create-venvs: create-venv create-tox-venv

.PHONY: bootstrap
## Bootstrap project
bootstrap: create-venvs
#------------------------------------

#------------------------------------
# Scripts
#------------------------------------
.PHONY: pydiatra-script
pydiatra-script:
	$(call print,Running pydiatra script)
	scripts/pydiatra.sh
#------------------------------------

#------------------------------------
# Tests
#------------------------------------
.PHONY: test
## Run tests | Tests
test: shfmt shellcheck markdownlint actionlint tox

.PHONY: tox
## Run tox
tox:
	$(call print,Running tox)
	@tox

.PHONY: pydiatra
## Run pydiatra linter
pydiatra:
	$(call print,Running pydiatra)
	@tox -e py-pydiatra

.PHONY: pylint
## Run pylint linter
pylint:
	$(call print,Running pylint)
	@tox -e py-pylint

.PHONY: flake8
## Run flake8 linter
flake8:
	$(call print,Running flake8)
	@tox -e py-flake8

.PHONY: isort
## Run isort linter
isort:
	$(call print,Running isort linter)
	@tox -e py-isort

.PHONY: bandit
## Run bandit linter
bandit:
	$(call print,Running bandit)
	@tox -e py-bandit

.PHONY: rstlint
## Run rstlint linter
rstlint:
	$(call print,Running rstlint)
	@tox -e py-rstlint

.PHONY: pydocstyle
## Run pydocstyle linter
pydocstyle:
	$(call print,Running pydocstyle)
	@tox -e py-pydocstyle

.PHONY: safety
## Run safety linter
safety:
	$(call print,Running safety)
	@tox -e py-safety

.PHONY: pytest
## Run pytest
pytest:
	$(call print,Running pytest)
	@tox -e py-pytest

.PHONY: black
## Run black linter
black:
	$(call print,Running black linter)
	@tox -e py-black

.PHONY: mypy
## Run mypy linter
mypy:
	$(call print,Running mypy)
	@tox -e py-mypy

.PHONY: shfmt
## Run shfmt linter
shfmt:
	$(call print,Running shfmt linter)
	@shfmt -l -d .

.PHONY: shellcheck
## Run shellcheck linter
shellcheck:
	$(call print,Running shellcheck)
	@shellcheck scripts/*.sh

.PHONY: markdownlint
## Run markdownlint linter
markdownlint:
	$(call print,Running markdownlint)
	@markdownlint CHANGELOG.md developer_doc.md

.PHONY: actionlint
## Run actionlint linter
actionlint:
	$(call print,Running actionlint)
	@actionlint

.PHONY: prettier-yaml-lint
## Run yaml linter
prettier-yaml-lint:
	$(call print,Running prettier check for yaml)
	@yarn run prettier --check ./.github/**/*.yaml
#------------------------------------

#------------------------------------
# Development
#------------------------------------
.PHONY: update-venvs
## Update packages in venv and tox with current requirements | Development
update-venvs:
	$(call print,Updating venvs)
	@${SOURCE_CMD} && \
	pip install -r requirements-dev.txt && \
	pip install -e . && \
	deactivate && \
	source .tox/py/bin/activate && \
	pip install -r requirements-dev.txt && \
	pip install -e .

.PHONY: format
## Format code
format:
	$(call print,Formatting code)
	@${SOURCE_CMD} && \
	autoflake --remove-all-unused-imports --in-place -r django_tqdm && \
	isort django_tqdm demos tests && \
	black .
	@shfmt -l -w .
	@markdownlint CHANGELOG.md developer_doc.md --fix
	@prettier --write ./.github/**/*.yaml

.PHONY: delete-venvs
delete-venvs:
	$(call print,Deleting venvs)
	@rm -rf venv
	@rm -rf .tox

.PHONY: recreate-venvs
## Recreate venvs
recreate-venvs: delete-venvs create-venvs
#------------------------------------

#------------------------------------
# Commands
#------------------------------------
.PHONY: build-wheel
## Build wheel | Commands
build-wheel:
	$(call print,Building wheel)
	@python3 setup.py bdist_wheel
#------------------------------------
