#!/bin/bash

set -eou pipefail

result=$(find django_tqdm -name '*.py' -exec py3diatra {} \;)
if [[ $result ]]; then
    echo "$result"
    exit 1
fi
