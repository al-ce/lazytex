import pytest
from pathlib import Path
import pyperclip
from lazytex.__main__ import main, parse_args


def test_cli_file_args(monkeypatch, tmp_path, capsys):
    """
    Test that the main function creates the output file when given a valid
    input file. Also test that the main function exits when given
    an invalid input file. Also test that it exits when the user does not want
    to overwrite an existing file.
    """
    input_file = Path("tests/test_data/test_expression.txt")
    output_file = tmp_path / "test_lazytex_output.md"

    monkeypatch.setattr("builtins.input", lambda _: "y")
    test_args = parse_args([str(input_file), "-o", str(output_file)])
    exit_code = main(test_args)
    assert output_file.is_file()
    assert exit_code == 0
    # Delete the output file so that it does not interfere with other tests
    output_file.unlink()
    assert not output_file.is_file()

    # Test that the program exits when the user does not want to overwrite
    # an existing file
    output_file = Path("tests/test_data/test_dummy_out.txt")
    monkeypatch.setattr("builtins.input", lambda _: "n")
    test_args = parse_args([str(input_file), "-o", str(output_file)])
    with pytest.raises(SystemExit) as exc_info:
        exit_code = main(test_args)
    assert exc_info.type == SystemExit
    assert exit_code == 0

    # Test that the program exits when given an invalid input file
    invalid_input_file = Path("tests/test_data/invalid_input_file.txt")
    output_file = tmp_path / "test_lazytex_output.md"
    test_args = parse_args([str(invalid_input_file), "-o", str(output_file)])
    with pytest.raises(SystemExit):
        main(test_args)
    assert not output_file.is_file()

    # Test that the program exits when neither an input file nor a statement
    # arg is given
    test_args = parse_args([])
    exit_code = main(test_args)
    assert exit_code == 1

    # # Test that if the user does not specify an output file, the program
    # # copies the converted table to the clipboard
    input_file = Path("tests/test_data/test_simple_expr.txt")
    test_args = parse_args([str(input_file)])
    exit_code = main(test_args)
    assert exit_code == 0
    expected_table = "" \
        "| Equivalence | Law |\n" \
        "| :--- | :--- |\n" \
        "| $\\ \\ \\ \\ \\ (p \\to q) \\leftrightarrow (p \\ \\land \\ q)$ | --- |\n"

    assert pyperclip.paste() == expected_table


def test_cli_statement_conversion(monkeypatch, capsys):
    """
    Test that the main function prints a LaTeX statement to stdout and copies
    it to the clipboard when given a string arg with the -s flag.
    """

    statement = "(p > q) and [c or (t <-> r)]"
    test_args = parse_args(["-s", statement])

    # Test a successul clipboard copy
    main(test_args)
    captured = capsys.readouterr()
    expected_latex = "(p \\to q) \\ \\land \\ [\\mathbf{c} \\ \\lor \\ (\\mathbf{t} \\leftrightarrow r)]"
    assert captured.out.rstrip() == expected_latex + \
        "\nStatement copied to clipboard."
    assert pyperclip.paste() == expected_latex

    # Test a failed clipboard copy
    monkeypatch.setattr(pyperclip, "paste", lambda: None)
    main(test_args)
    captured = capsys.readouterr()
    assert captured.out.rstrip() == expected_latex + \
        "\nFailed to copy statement to clipboard."
