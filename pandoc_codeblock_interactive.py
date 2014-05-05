#!/usr/bin/env python

"""
Pandc filter to convert all octave and python code blocks to interactive sessions.
"""

import subprocess, sys, os
from pandocfilters import toJSONFilter, CodeBlock
import threading
import time

def octave(key, value, format, meta):
    if key != 'CodeBlock':
      return
    options = value[0][1]
    text = value[1]
    if 'octave' in options and 'interactive' in options:
        f = file('stdin.txt','w')
        f.write(text)
        f.close()
        subprocess.call('env LD_PRELOAD=./loginteractive.so STDIN=stdin.txt STDOUT=stdout.txt octave -qi --traditional > /dev/null', shell=True, bufsize=1)
        f = open('stdout.txt','r')
        text = f.read()
        f.close()
        return CodeBlock(("",["octave", "interactive"],[]),text)
    elif 'python' in options and 'interactive' in options:
        f = file('stdin.txt','w')
        f.write(text)
        f.close()
        subprocess.call('env LD_PRELOAD=./loginteractive.so STDIN=stdin.txt STDOUT=stdout.txt python -i > /dev/null', shell=True, bufsize=1)
        f = open('stdout.txt','r')
        text = f.read()
        f.close()
        return CodeBlock(("",["python", "interactive"],[]),text)

if __name__ == "__main__":
        toJSONFilter(octave)
