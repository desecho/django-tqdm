#!/bin/bash

autoflake --remove-all-unused-imports --in-place -r django_tqdm
yapf -ri django_tqdm
isort -rc django_tqdm
