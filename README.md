# Smart Media Tokens

(c) 2017 Steemit, Inc.  All rights reserved

# SMT Whitepaper

This repository contains the LaTeX source code for the SMT Whitepaper. The
instructions to clone the repository and build the PDF using pandoc are
described below.

# Fast Build

## OSX

* `brew install docker docker-machine`
* `brew tap caskroom/cask`
* `brew cask install virtualbox`
* `docker-machine create --driver virtualbox default`
* `eval $(docker-machine env default)`
* `make`

## Docker Already Installed, Linux

(This is already in the `Makefile`.  Just type `make`.)

* `docker build -t steemit/smt-whitepaper .`
* `docker run steemit/smt-whitepaper > smt-whitepaper.pdf`

# Manual Build

Currently the manual build instructions are for Ubuntu 16.04 or higher but
may successfully build on other distributions. Pull requests to update the
whitepaper will be gladly accepted and reviewed.

## Install Packages

```bash
sudo apt-get update
sudo apt install -y texlive-xetex pandoc python3-pip graphviz imagemagick
pip3 install matplotlib
```

## Compile Images

There are several image files in the `/img/` directory that are generated using the build file. The first time the build is done, and whenever the figures are updated, the images will need to be compiled.

```bash
./build.sh
```

## Build PDF

Compile using pandoc
```bash
cd ~/smt-whitepaper/smt-manual/
pandoc manual.md --latex-engine=xelatex -o smt-whitepaper.pdf
```

After building, the pdf file will be output to `smt-whitepaper.pdf`.
