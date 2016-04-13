all:
	pdflatex -shell-escape paper.tex
	bibtex paper.aux
	pdflatex -shell-escape paper.tex
	pdflatex -shell-escape paper.tex
travis:
	pdflatex -shell-escape --halt-on-error paper.tex
	bibtex paper.aux
	pdflatex -shell-escape --halt-on-error paper.tex
	pdflatex -shell-escape --halt-on-error paper.tex
