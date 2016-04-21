#! /usr/bin/env python

from __future__ import print_function

from json import load

author_list = load(open("authors.json"))

with open("../authors.tex", "wb") as f:
    f.write("\\author{%\n")
    for n, author in enumerate(author_list):
        f.write(("%s%%\n" % author["name"]).encode("utf-8"))
        f.write(("\\thanks{%s (\\email{%s}).}\n" \
                % (author["institution"], author["email"])).encode("utf-8"))
        if n < len(author_list) - 1:
            f.write("\\and\n".encode("utf-8"))
    f.write("}\n")
