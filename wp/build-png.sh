#!/bin/bash

set -e
set -x

cd img
mkdir -p build
for file in *.svg
do
   /usr/bin/inkscape -z -f "${file}" -w 640 -e "build/${file%.*}.png"
done

cd ..

./mmpolicy.py
./mmphase.py
