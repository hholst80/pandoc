#!/bin/sh
#pandoc -t json < README.md | ./pandoc_codeblock_interactive.py | pandoc -N --variable mainfont=Georgia --variable sansfont=Arial --variable monofont="Bitstream Vera Sans Mono Bold" --variable fontsize=12pt --variable version=1.10 -f json --latex-engine=xelatex --toc -o README.pdf
pandoc -t json < README.md | ./pandoc_codeblock_interactive.py | pandoc -N --variable mainfont=Georgia --variable sansfont=Arial --variable monofont="Inconsolata" --variable fontsize=12pt --variable version=1.10 -f json --latex-engine=xelatex --toc -o README.pdf
