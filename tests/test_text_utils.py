import pathlib
import pytest

import lazytex.text_utils as tu


def test_get_file_lines():
    """
    Test that :func:`get_file_lines` function correctly reads the lines
    from a file and returns them as a list.
    Also test that the function correctly handles errors like
    a file not being found or not being able to open the file.
    """

    simple_file = "tests/test_data/test_file_reader.txt"
    assert tu.get_file_lines(simple_file) == ["hello\n", "world\n"]

    with pytest.raises(SystemExit) as exc_info:
        tu.get_file_lines("does_not_exist.txt")
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 1


def test_text_to_latex():
    """
    Test that :func:`convert_to_latex` correctly replaces
    the operators in a statement with their LaTeX equivalents.
    """

    tex_pairs = [
        ("t", "\\mathbf{t}"),
        ("c", "\\mathbf{c}"),
        (">", "\\to"),
        ("and", "\\ \\land \\"),
        ("or", "\\ \\lor \\"),
        ("-", "\\sim "),
        ("==", "\\ \\equiv \\"),
        ("p > q", "p \\to q"),
        ("p and q", "p \\ \\land \\ q"),
        ("p or q", "p \\ \\lor \\ q"),
        ("-p", "\\sim p"),
        ("p == q", "p \\ \\equiv \\ q"),
        ("p and -q or c > t",
            "p \\ \\land \\ \\sim q \\ \\lor \\ \\mathbf{c} \\to \\mathbf{t}"),
        ("", ""),
        ("   ", "   "),
        ("hello", "hello")
    ]
    for plaintext, expected_latex in tex_pairs:
        assert tu.convert_to_latex(plaintext) == expected_latex


def test_format_row():
    """
    Test that the format_row function correctly formats a 'statement' string
    and a 'law' string in the form:
    | $<statement>$ | <law> |\\n

    The function should distinguish between a statement that has a law and
    one that does not by checking if the law is "---".
    If the statement has a law, the statement should
    include a LaTeX equivalence symbol. If the statement does not have a law,
    the statement should be indented by 4 spaces.
    """

    test_data = [
        ("p or q", "by implication",
         "| $\\ \\equiv \\ p \\ \\lor \\ q$ | by implication |\n"),
        ("hello", "world", "| $\\ \\equiv \\ hello$ | world |\n"),
        ("", "", "| $\\ \\equiv \\ $ |  |\n"),
        ("no law", "---", "| $\\ \\ \\ \\ \\ no law$ | --- |\n"),
    ]
    for statement, law, expected_output in test_data:
        assert tu.format_row(statement, law) == expected_output


def test_generate_table():
    """
    Test that :func:`generate_table` correctly generates a markdown table of
    statements and laws. If a line contains the `# START` string, it should
    only start adding to the table after a line that contains the `# START`
    string. Otherwise, it should start adding to the table from the first line.
    It should set the 'law' variable to "---" if no law is found on the line.

    """

    valid_list = [
        "dummy line\n",
        "# START\n",
        "p > q == p or q",
        "p or q # by implication\n",
    ]

    expected_table = [
        "| Equivalence | Law |\n",
        "| :--- | :--- |\n",
        "| $\\ \\ \\ \\ \\ p \\to q \\ \\equiv \\ p \\ \\lor \\ q$ | --- |\n",
        "| $\\ \\equiv \\ p \\ \\lor \\ q$ | by implication |\n",
    ]

    assert tu.generate_table(valid_list) == expected_table

    valid_list = [
        "p > q == p or q",
        "p or q # by implication\n",
    ]

    expected_table = [
        "| Equivalence | Law |\n",
        "| :--- | :--- |\n",
        "| $\\ \\ \\ \\ \\ p \\to q \\ \\equiv \\ p \\ \\lor \\ q$ | --- |\n",
        "| $\\ \\equiv \\ p \\ \\lor \\ q$ | by implication |\n",
    ]

    assert tu.generate_table(valid_list) == expected_table


def test_check_file_exists(monkeypatch):
    """
    Test that :func:`check_file_exists` correctly checks if a file exists.
    It should return early if the output file does not exist. If it does, it
    should ask the user if they want to overwrite it in a loop until a valid
    response is given. If the user enters 'n' or 'N', the program should exit.
    """

    non_existent_file = "does_not_exist.txt"
    assert not pathlib.Path(non_existent_file).is_file()
    assert not tu.check_file_exists(non_existent_file)

    assert pathlib.Path("tests/test_data/test_file_reader.txt").is_file()

    monkeypatch.setattr("builtins.input", lambda _: "n")
    with pytest.raises(SystemExit) as exc_info:
        tu.check_file_exists("tests/test_data/test_file_reader.txt")
    assert exc_info.type == SystemExit

    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert tu.check_file_exists("tests/test_data/test_file_reader.txt")


def test_write_table_to_file():
    """
    Test that :func:`write_table_to_file` correctly writes the table to a
    markdown file. It should insert a header row at the top of the table,
    and successfully write the table to the file.

    """

    test_table = [
        "| Equivalence | Law |\n",
        "| :--- | :--- |\n",
        "| $\\ \\ \\ \\ \\ p \\to q \\ \\equiv \\ p \\ \\lor \\ q$ | --- |\n",
        "| $\\ \\equiv \\ p \\ \\lor \\ q$ | by implication |\n",
    ]

    tu.write_table_to_file(test_table, "tests/test_data/test_output.md")

    assert pathlib.Path("tests/test_data/test_output.md").is_file()

    with open("tests/test_data/test_output.md", "r") as f:
        output = f.readlines()

    assert output == test_table
    pathlib.Path("tests/test_data/test_output.md").unlink()
    assert not pathlib.Path("tests/test_data/test_output.md").is_file()
