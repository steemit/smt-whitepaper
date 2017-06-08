#!/bin/sh

# Prereqs for building on Ubuntu LTS:  sudo apt-get install pandoc texlive-latex-base texlive-fonts-recommended texlive-latex-recommended
pandoc -o marketmaker.pdf marketmaker.md
