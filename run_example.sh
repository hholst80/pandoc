#!/bin/sh
pandoc -t json < README.md | ./pandoc_codeblock_interactive.py | pandoc -f json -o README.pdf
