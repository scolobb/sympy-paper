#! /bin/bash

set -e

python -m json.tool authors.json > authors.json.tmp
mv authors.json.tmp authors.json
