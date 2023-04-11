import argparse
import pyperclip
import lazytex.text_utils as tu


def main(args):

    if args.statement:
        latex_statement = tu.convert_to_latex(args.statement)
        print(latex_statement)
        pyperclip.copy(latex_statement)
        if pyperclip.paste() == latex_statement:
            print("Statement copied to clipboard.")
        else:
            print("Failed to copy statement to clipboard.")
        return

    if args.input_file:
        lines = tu.get_file_lines(args.input_file)
        converted_table = "".join(tu.generate_table(lines))

        output_file = args.output_file if args.output_file else "lazytex_output.md"
        tu.write_table_to_file(converted_table, output_file)

        print(f"Table written to {output_file}")
        return

    print("Either an input file or a statement, must be provided, but not both.")
    return 1


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description='Converts logical statements in a simple format to LaTeX.')

    parser.add_argument(
        'input_file',
        type=str,
        nargs='?',
        help='The file to read the logical statements from.'
    )

    parser.add_argument(
        '-s',
        '--statement',
        type=str,
        help='A logical statement to convert to LaTeX and save to system clipboard. Cannot be used with input_file.'
    )

    parser.add_argument(
        '-o',
        '--output_file',
        type=str,
        help='The file to write the LaTeX table to. Defaults to "lazytex_output.md".'
    )

    args = parser.parse_args(args)

    return args


if __name__ == '__main__':
    import sys
    args = parse_args(sys.argv[1:])
    main(args)
