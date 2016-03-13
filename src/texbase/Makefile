# -*- Makefile -*- $Id$

ARTICLE=base

PDF=$(patsubst %,%.pdf,$(ARTICLE))

all: $(PDF)

%.pdf: %.tex
	pdflatex $<
	pdflatex $< && pdflatex $<

clean:
	rm -rf  core *~ *.log *.aux *.bbl *.dvi *.blg $(PDF)

.depend: $(ARTICLE).tex
	test -x ../texdepend.pl || chmod a+x ../texdepend.pl
	../texdepend.pl $< >$@

-include .depend
