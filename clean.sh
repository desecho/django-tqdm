#!/bin/bash

# We want to remove imports before running isort.
autoflake --remove-all-unused-imports --in-place -r django_tqdm
yapf -ri django_tqdm
# We want to run isort after yapf to make sure isort lint pass.
isort -rc django_tqdm
