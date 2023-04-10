import sys


def get_file_lines(file_name: str) -> list:
    """
    Read a file and return a list of lines.
    """
    try:
        with open(file_name, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: file '{file_name}' not found.", file=sys.stderr)
        sys.exit(1)
    except IOError:
        print(f"Error: could not open file '{file_name}'.", file=sys.stderr)
        sys.exit(1)


def replace_operators(statement: str) -> str:
    """
    Replace the operators in a string with their LaTeX equivalents.
    Also adds boldface to the t and c variables.
    Returns the converted string.
    """
    operators = {
        "t": "\\mathbf{t}",  # the t replacement must come before >
        "c": "\\mathbf{c}",
        ">": "\\to",
        "and": "\\ \\land \\",
        "or": "\\ \\lor \\",
        "-": "\\sim ",
        "==": "\\ \\equiv \\"
    }
    for old, new in operators.items():
        statement = statement.replace(old, new)
    return statement


def format_row(statement: str, law: str) -> str:
    """
    Takes a LaTeX statement and a logical equivalence law as arguments.
    Returns a formatted markdown table row in the form:
    | $<statement>$ | <law> |
    """
    start = "| $\\ \\ \\ \\ \\ " if law == "---" else "| $\\ \\equiv \\ "
    converted_statement = replace_operators(statement)
    return start + converted_statement.rstrip() + "$ | " + law.rstrip() + " |\n"


def generate_table(lines: list, output_file: str) -> None:
    """
    Takes a list of lines from a file that contain substrings equivalent to 
    statements and logical equivalence laws formatted as:
    <statement>  # <law>

    where the statement is a formal logic statement that uses syntax like:
    [(p > q) and (q > r)] > (p > r) == t

    where brackets and parens are interchangeable, `>` is the implication,
    `and` is the conjunction, `or` is the disjunction, `-` is the negation,
    and `==` is the equivalence.

    The law is a string that describes the logical equivalence law that
    was used to convert the statement to the form on the right side of the
    `==` operator.

    The function converts the statements to LaTeX and writes a markdown
    table of the statements and laws to the output file.
    """

    start_index = lines.index("# START\n")
    table = []
    for line in lines[start_index+1:]:
        line = line.rstrip()
        row = line.split("# ")
        statement = row[0]
        law = row[1] if len(row) == 2 else "---"
        table.append(format_row(statement, law))
    return table


def write_table_to_file(table: list, output_file: str) -> None:
    """
    Takes a list of formatted markdown table rows and writes them to the
    output file.
    """
    with open(output_file, 'w') as f:
        f.write("| Equivalence | Law |\n")
        f.write("| :--- | :--- |\n")  # Add alignment for the table columns
        f.write("".join(table))


if __name__ == "__main__":
    lines = get_file_lines('tests/test_expression.txt')

    converted_table = "".join(generate_table(lines, 'output.md'))

    write_table_to_file(converted_table, 'output.md')
