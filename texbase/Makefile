# -*- Makefile -*- $Id$

ARTICLE=base

PDF=$(patsubst %,%.pdf,$(ARTICLE))

all: $(PDF)

%.pdf: %.tex
	pdflatex $<
	pdflatex $< && pdflatex $<

clean:
	rm -rf  core *~ *.log *.aux *.bbl *.dvi *.blg $(PDF)

