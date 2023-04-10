import argparse
import lazytex.text_utils as tu


def main(args):
    lines = tu.get_file_lines(args.input_file)
    converted_table = "".join(tu.generate_table(lines))

    output_file = args.output_file if args.output_file else "lazytex_output.md"
    tu.write_table_to_file(converted_table, output_file)

    print(f"Table written to {output_file}")


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description='Converts logical statements in a simple format to LaTeX.'
    )

    parser.add_argument(
        'input_file',
        type=str,
        help='The file to read the logical statements from.'
    )
    parser.add_argument(
        '-o',
        '--output-file',
        type=str,
        help='The output file to write the generated LaTeX table to.'
    )

    return parser.parse_args(args)


if __name__ == '__main__':
    import sys
    args = parse_args(sys.argv[1:])
    main(args)

