#! /usr/bin/env python

from __future__ import print_function

from json import load

author_list = load(open("authors.json"))

with open("../authors.tex", "wb") as f:
    for author in author_list:
        f.write(("\\author{%s}\n" % author["name"]).encode("utf-8"))
#        f.write(("\\affil{%s}\n" % author["institution"]).encode("utf-8"))
        f.write("\n".encode("utf-8"))
