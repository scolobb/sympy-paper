#! /usr/bin/env python

from __future__ import print_function

from json import load

author_list = load(open("authors.json"))

print("List of authors:")
print()

for author in author_list:
    print("Author:", author["name"])
    print("Affiliation:", author["institution"])
    print("Address:", author["institution_address"])
    print("GitHub profile: https://github.com/%s" % author["github_id"])
    print("Article commits: https://github.com/sympy/sympy-paper/commits?author=%s" % author["github_id"])
    print("Article comments on issues and PRs: https://github.com/sympy/sympy-paper/search?q=%s&type=Issues" % author["github_id"])
    print()
