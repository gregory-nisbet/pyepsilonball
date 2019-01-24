#!/bin/bash

cd "$(dirname "${BASH_SOURCE[0]}")" || exit 20

env PYTHONPATH="$PYTHONPATH:./src/pyepsilonball" python -i ./load_modules.py
