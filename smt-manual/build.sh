#!/bin/bash

set -e
set -x

./md-to-toc.py manual.md

mkdir -p img
cd img
../pie.py
dot -Tpng -o creation.png ../creation.dot
