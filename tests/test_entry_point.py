from pathlib import Path
from lazytex.__main__ import main, parse_args


def test_lazytex(monkeypatch, tmp_path):
    input_file = Path("tests/test_data/test_expression.txt")
    output_file = tmp_path / "test_lazytex_output.md"

    monkeypatch.setattr("builtins.input", lambda _: "y")
    test_args = parse_args([str(input_file), "-o", str(output_file)])
    main(test_args)

    assert output_file.is_file()
