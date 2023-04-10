import texsanity.text_utils as tu


def test_replace_operators():
    test_pairs = [
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
    for statement, expected_output in test_pairs:
        assert tu.replace_operators(statement) == expected_output
