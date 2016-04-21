#! /usr/bin/env python

from __future__ import print_function

from json import load
from io import open

author_list = load(open("authors.json"))

with open("../authors.tex", "w") as f:
    f.write(u"\\author{%\n")
    for n, author in enumerate(author_list):
        f.write((u"%s%%\n" % author["name"]))
        f.write(u"\\thanks{%s (\\email{%s}).}\n" \
                % (author["institution"], author["email"]))
        if n < len(author_list) - 1:
            f.write(u"\\and\n")
    f.write(u"}\n")
