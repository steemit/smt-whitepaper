#!/bin/bash

set -e
set -x

# Dependencies:
# Python 3
# Matplotlib
# Graphviz
# ImageMagick

mkdir -p img
cd img
../pie.py
convert \
   rc-linear-cc-linear.png \
   rc-linear-cc-sqrt.png \
   rc-linear-cc-bounded.png \
   +append rc-cc-linear.png

convert \
   rc-quadratic-cc-linear.png \
   rc-quadratic-cc-sqrt.png \
   rc-quadratic-cc-bounded.png \
   +append rc-cc-quadratic.png

convert \
   rc-cc-linear.png \
   rc-cc-quadratic.png \
   -append rc-cc.png

dot -Tpng -o creation.png ../creation.dot
dot -Tpng -o timeline.png ../timeline.dot

cd ..
pandoc manual.md --latex-engine=xelatex -o smt-whitepaper.pdf
