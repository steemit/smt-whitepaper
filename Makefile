default: openpdf

.PHONY: default openpdf clean

clean:
	rm -f *.pdf smt-manual/img/creation.png smt-manual/img/timeline.png \
		smt-manual/img/rc-cc-quadratic.png \
		smt-manual/img/rc-cc-linear.png \
		smt-manual/img/rc-cc.png

openpdf: smt-whitepaper.pdf
	open smt-whitepaper.pdf

smt-whitepaper.pdf:
	docker build -t steemit/smt-whitepaper .
	docker run steemit/smt-whitepaper > $@
