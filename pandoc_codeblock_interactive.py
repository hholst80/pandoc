#!/usr/bin/env python

"""
Pandc filter to convert all octave and python code blocks to interactive sessions.
"""

import subprocess, sys, os
from pandocfilters import toJSONFilter, CodeBlock

def codeblock_interactive(key, value, format, meta):
    if key != 'CodeBlock':
      return
    options = value[0][1]
    text = value[1]
    prg = None
    cmd = None
    if 'octave' in options and 'interactive' in options:
        prg = 'octave'
        cmd = 'env LD_PRELOAD=./loginteractive.so STDIN=stdin.txt STDOUT=stdout.txt octave -qi --traditional > /dev/null'
    elif 'python' in options and 'interactive' in options:
        prg = 'python'
        cmd = 'env LD_PRELOAD=./loginteractive.so STDIN=stdin.txt STDOUT=stdout.txt python -i > /dev/null'
    if prg and cmd:
        f = file('stdin.txt','w')
        f.write(text)
        f.close()
        subprocess.call(cmd, shell=True, bufsize=1)
        f = open('stdout.txt','r')
        text = "\n".join(f.read().split("\n")[0:-1])
        f.close()
        return CodeBlock(("",[prg, "interactive"],[]),text)

if __name__ == "__main__":
        toJSONFilter(codeblock_interactive)
