.DEFAULT_GOAL := help

SHELL := /bin/bash
SOURCE_CMD := source venv/bin/activate

#------------------------------------
# Help
#------------------------------------
TARGET_MAX_CHAR_NUM := 25

# COLORS
RED     := \033[0;31m
GREEN   := \033[0;32m
YELLOW  := \033[0;33m
BLUE    := \033[0;34m
MAGENTA := \033[0;35m
CYAN    := \033[0;36m
WHITE   := \033[0;37m
RESET   := \033[0;10m

.PHONY: help
## Show help | Help
help:
	@echo ''
	@echo 'Usage:'
	@printf "  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}"
	@echo ''
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
		    if (index(lastLine, "|") != 0) { \
				stage = substr(lastLine, index(lastLine, "|") + 1); \
				printf "\n ${GRAY}%s: \n", stage;  \
			} \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			if (index(lastLine, "|") != 0) { \
				helpMessage = substr(helpMessage, 0, index(helpMessage, "|")-1); \
			} \
			printf "    ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)
#------------------------------------

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
## Run pydiatra
pydiatra:
	scripts/pydiatra.sh

.PHONY: pylint
## Run pylint
pylint:
	tox -e py-pylint

.PHONY: flake8
## Run flake8
flake8:
	tox -e py-flake8

.PHONY: isort
## Run isort
isort:
	tox -e py-isort

.PHONY: bandit
## Run bandit
bandit:
	tox -e py-bandit

.PHONY: rstlint
## Run rstlint
rstlint:
	tox -e py-rstlint

.PHONY: pydocstyle
## Run pydocstyle
pydocstyle:
	tox -e py-pydocstyle

.PHONY: safety
## Run safety
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
## Format code except for json files
format:
	${SOURCE_CMD} && \
	autoflake --remove-all-unused-imports --in-place -r django_tqdm && \
	isort django_tqdm && \
	black .
	shfmt -l -w .
#------------------------------------
