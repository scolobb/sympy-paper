import doctest

files = ["introduction.tex",
         "architecture.tex",
         "numerics.tex",
         "features.tex",
         "simplification.tex",
         "calculus.tex",
         "printers.tex",
         "solvers.tex",
         "matrices.tex",
         "domain_specific.tex"
        ]

full_text = ""

output_file = "test-paper.txt"

for file in files:
    with open(file, 'r') as f:
        full_text += "\n" + f.read()

with open(output_file, "w") as f:
    f.write(full_text)

doctest.testfile(output_file)
