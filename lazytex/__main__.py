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
        return 0

    if not args.input_file:
        print("Either an input file or a statement, must be provided, but not both.")
        return 1

    lines = tu.get_file_lines(args.input_file)
    converted_table = "".join(tu.generate_table(lines))
    print(f"\nConverted {args.input_file} to LaTeX table.\n")

    if args.output_file:
        output_file = args.output_file
        tu.write_table_to_file(converted_table, output_file)
        print(f"Table written to {output_file}")
        return 0
    else:
        pyperclip.copy(converted_table)
        print("No output file specified, table copied to clipboard.")
        print("Table copied to clipboard.")
        return 0


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description='Converts logical statements in a simple format to LaTeX. If an output file is specified with the -o flag, will write the converted LaTeX statements to the output file, otherwise, they will be copied to the user\'s clipboard')

    parser.add_argument(
        'input_file',
        type=str,
        nargs='?',
        help='The file to read the logical statements from to be converted.'
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
