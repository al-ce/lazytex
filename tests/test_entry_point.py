import pytest
from pathlib import Path
from lazytex.__main__ import main, parse_args


def test_cli_file_args(monkeypatch, tmp_path):
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
    main(test_args)
    assert output_file.is_file()
    # Delete the output file so that it does not interfere with other tests
    output_file.unlink()
    assert not output_file.is_file()

    # Test that the program exits when the user does not want to overwrite
    # an existing file
    output_file = Path("tests/test_data/test_dummy_out.txt")
    monkeypatch.setattr("builtins.input", lambda _: "n")
    test_args = parse_args([str(input_file), "-o", str(output_file)])
    with pytest.raises(SystemExit) as exc_info:
        main(test_args)
    assert exc_info.type == SystemExit

    # Test that the program exits when given an invalid input file
    invalid_input_file = Path("tests/test_data/invalid_input_file.txt")
    output_file = tmp_path / "test_lazytex_output.md"
    test_args = parse_args([str(invalid_input_file), "-o", str(output_file)])
    with pytest.raises(SystemExit):
        main(test_args)
    assert not output_file.is_file()

    # Test that default output filename is used if no output filename is given
    output_file = None
    test_args = parse_args([str(input_file)])
    main(test_args)
    assert Path("lazytex_output.md").is_file()
    Path("lazytex_output.md").unlink()
    assert not Path("lazytex_output.md").is_file()
