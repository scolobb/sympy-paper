#! /usr/bin/env python

from __future__ import print_function

from json import load

author_list = load(open("authors.json"))

print("List of authors:")
print()

for author in author_list:
    print(r"\author{%s}" % author["name"])
    # TODO: Print more info in Latex format here
    print()
