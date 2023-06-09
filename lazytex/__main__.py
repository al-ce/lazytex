import argparse
import pyperclip
import lazytex.text_utils as tu


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description='Converts logical statements in a simple format to LaTeX. If an output file is specified with the -w flag, will write the converted LaTeX statements to the output file, or with the -a flag, append to it. Otherwise, they will be copied to the user\'s clipboard')

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
        '-w',
        '--write_to',
        type=str,
        help='The file to write the LaTeX table to. Overwrites the file if it already exists.'
    )

    parser.add_argument(
        '-a',
        '--append_to',
        type=str,
        help='The file to append a LaTeX table or a single statement to. The file must already exist.'
    )

    parser.add_argument('-v', '--version', action='version', version='0.1.0')

    args = parser.parse_args(args)

    return args


def main(args=None):

    # args is passed to main for testing purposes
    if not args:
        args = parse_args()

    if not (args.input_file or args.statement):
        print("Either an input file or a statement must be provided, but not both.")
        return 1

    if args.statement:
        output_latex = tu.convert_to_latex(args.statement)
        output_type = "Statement"
        print("Converted statement to LaTeX:\n")
        print(output_latex)
        print()

    elif args.input_file:
        lines = tu.get_file_lines(args.input_file)
        output_latex = "".join(tu.generate_table(lines))
        output_type = "Table"
        print(f"\nConverted {args.input_file} to LaTeX table.\n")

    if args.write_to:
        write_to = args.write_to
        tu.write_table_to_file(output_latex, write_to)
        print(f"{output_type} written to {write_to}")
        return 0
    elif args.append_to:
        write_to = args.append_to
        tu.append_latex_to_existing_file(output_latex, write_to)
        print(f"{output_type} appended to {write_to}")
        return 0

    pyperclip.copy(output_latex)
    if pyperclip.paste() == output_latex:
        print(f"{output_type} copied to clipboard.")
    else:
        print("Failed to copy statement to clipboard.")
    return 0


if __name__ == '__main__':
    main()
