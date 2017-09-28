FROM ubuntu:16.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt -y install texlive-xetex pandoc python3-pip graphviz imagemagick && \
    pip3 install matplotlib

ADD ./smt-manual /smt

WORKDIR /smt

RUN bash build.sh && \
    pandoc manual.md --latex-engine=xelatex -o smt-whitepaper.pdf

ENTRYPOINT [ "/bin/cat" , "/smt/smt-whitepaper.pdf" ]
