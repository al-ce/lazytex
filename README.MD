# lazytex

`lazytex` is a command line tool that allows you to easily convert logical
statements from a readable syntax to LaTeX format. It's main use is to create
a Markdown table with two columns, one for a logical statement in LaTeX format
and one for a plain text comment about which logical equivalence law was used
to transform the statement.

https://user-images.githubusercontent.com/23170004/231308098-c4fed725-cc8a-41c4-987f-dd21858639e6.mov

The intention behind this program is to let a user type out a long sequence of
statements so they can remain in a readable format while working on the
problem, and then doing all the conversion to LaTeX and a Markdown table in one
command.

# Dependencies

- Python 3.8+

`pip` will also install the following dependencies:

- `pyperclip` for copying to clipboard

# Installation

Clone this repository and run `pip install .` from the root directory.

After install, you can run `lazytex` from the command line in any directory.
Test it with `lazytex -h` to see the help message or `lazytex -v` to see the version.

# Conversion syntax

| Plain syntax | LaTeX syntax        | Visual example        |
| ------------ | ------------------- | --------------------- |
| -p           | \sim p              | $\sim p$              |
| p > q        | p \to q             | $p \to q$             |
| p and q      | p \land q           | $p \land q$           |
| p or q       | p \lor q            | $p \lor q$            |
| p <-> q      | p \leftrightarrow q | $p \leftrightarrow q$ |
| p == q       | p \equiv q          | $p \equiv q$          |

For a more complex example:

```
== [p > (-q and c) or (-p or (t <-> r))]
```

would become

```latex
\ \equiv \ [p \to (\sim q \ \land \ \mathbf{c}) \ \lor \ (\sim p \ \lor \ t \leftrightarrow r))]
```

Across multiple lines this can be a nice time saver.

In the future, I'd like to add more features to this syntax, like quantifiers,
text, text styling, etc, and maybe even actual LaTeX headers, footers, etc.
Currently, this program is mainly intended for use in embedded LaTeX in a
markdown file when taking notes.

# Usage

From your terminal, `lazytex` can be run with the following arguments/options:

- `-h` or `--help` to see the help message
- `-v` or `--version` to see the version
- `path/to/some_file` to convert the contents of a file to LaTeX
- `-s` or `--statement` + a logical statement to convert to LaTeX
- `-w` or `--write` + `path/to/output_file` to write the converted LaTeX to a file
- `-a` or `--append` + `path/to/output_file` to append the converted LaTeX to a file

## Input

You can either pass a single statement string enclosed in quotes as an argument
to `lazytex` with the `-s` flag, or you can pass a relative or absolute
filepath to a file to read from.

For example, if you pass a statement, `lazytex` will convert it to LaTeX as a single line,
like so:

```bash
lazytex -s "== [p > (-q and c) or (-p or (t <-> r))]"
```

`lazytex` will convert this to:

```
\ \equiv \ [p \to (\sim q \ \land \ \mathbf{c}) \ \lor \ (\sim p \ \lor \ t \leftrightarrow r))]
```

If you pass a path to an input file, for example, one that contains the following:

https://github.com/al-ce/lazytex/blob/ecdaf82ab6be6789b76313e5f1d568ea7f0a4455/tests/test_data/hammack_example.txt#L1-L12

(this example is taken from _Book of Proof_, edition 3.3, by Richard Hammack.
Creative Commons Attribution-NonCommercial-NoDerivative 4.0 International License)

```bash
lazytex path/to/hammack_example.txt
```

`lazytex` will convert this to:

```markdown
| Equivalence                                                          | Law                                    |
| :------------------------------------------------------------------- | :------------------------------------- |
| $\ \equiv \ \sim (p \ \land \ \sim q) \ \lor \ (q \ \land \ \sim q)$ | by implication                         |
| $\ \equiv \ (\sim p \ \lor \ q) \ \lor \ (q \ \land \ \sim q)$       | by De Morgan's law and double negation |
| $\ \equiv \ (\sim p) \ \lor \ [q \ \lor \ (q \ \land \ \sim q)]$     | by associative law                     |
| $\ \equiv \ (\sim p) \ \lor \ [q \ \lor \ \mathbf{c}]$               | by negation law                        |
| $\ \equiv \ \sim p \ \lor \ q$                                       | by identity law                        |
| $\ \equiv \ p \to q$                                                 | by implication                         |
```

Notice how `lazytex` ignores everything up to the `# START` line so you can
include comments and other information in your input file.
In a Markdown app that can embed LaTeX or MathJax, it would look like this:

<img width="643" alt="md_table_example" src="https://user-images.githubusercontent.com/23170004/231308070-b1be01e3-4f18-4069-80cd-ca7326d1fe42.png">

## Output

If you don't pass any additional arguments, as in the examples above, `lazytex` will send the converted LaTeX (either the single line or the entire Markdown table) to your system clipboard.

### Write/overwrite to output file with `-w` flag

If you pass the `-w` flag, `lazytex` will write the converted LaTeX to the file you pass with the `-w` flag.

If the file you specified already exists, `lazytex` will confirm with you that you want to overwrite it.

```bash
lazytex path/to/input.txt -w path/to/output.txt
```

```stdout
Converted tests/test_data/hammack_example.txt to LaTeX table.

Warning: file 'tests/test_data/test_dummy_out.txt' already exists.
Continue and overwrite? [y/n] y
Table written to tests/test_data/test_dummy_out.txt
```

This also works for single line statements:

```bash
lazytex -s "== [p > (-q and c) or (-p or (t <-> r))]" -w path/to/output.txt
```

### Append to output file with `-a` flag

If you pass the `-a` flag, `lazytex` will append the converted LaTeX to the file you pass with the `-a` flag without overwriting it.

```bash
lazytex -s "p > q" -a path/to/output.txt
```

```stdout
Converted statement to LaTeX:

p \to q

Statement appended to path/to/output.txt
```

This also works for input files:

```bash
lazytex path/to/input.txt -a path/to/output.txt
```

```stdout
Converted path/to/input.txt to LaTeX table.

Table appended to path/to/output.txt
```

# Tests

See the [tests/](https://github.com/al-ce/lazytex/tree/main/tests) directory. Most of this project ended up being practice for writing unit tests as I made this clearly overly-engineered CLI tool (just use regex!).

```bash
❯ coverage report -m
Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
lazytex/__main__.py            46      2    96%   49, 88
lazytex/text_utils.py          52      3    94%   15-17
tests/test_entry_point.py      82      0   100%
tests/test_text_utils.py       45      0   100%
---------------------------------------------------------
TOTAL                         225      5    98%
```
