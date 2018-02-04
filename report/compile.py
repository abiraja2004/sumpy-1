#!/usr/bin/python

import subprocess, sys

try:
    commands = [
                ['pdflatex', sys.argv[1] + '.tex'],
                ['bibtex', sys.argv[1] + '.aux'],
                ['pdflatex', sys.argv[1] + '.tex'],
                ['pdflatex', sys.argv[1] + '.tex']
            ]
except IndexError:
    print("Provide .tex file to be compiled")
    exit(1)

for c in commands:
    subprocess.call(c)
