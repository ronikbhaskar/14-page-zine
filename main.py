"""
I'm almost positive someone has thought of this exact 14-panel zine format 
before. Regardless, I hope this makes the process of formatting them
just a tad easier. If this helps people make more zines, then my work is 
done. Well, it's not *done* done, but it's a start. Please, go forth and
make zines, because I know I won't.

hbd

Author: Ronik
"""

import argparse
from formatter import create_pdf_grid

ZINE_14_PM = [12, 11, 10, 9, 13, None, 7, 8, 0, None, 6, 5, 1, 2, 3, 4]
ZINE_14_RF = ([True] * 4 + [False] * 4) * 2

def main(args):
    """
    This is so excessive.
    But it's for the zines.
    """

    create_pdf_grid(
        args.input,
        args.output,
        page_map=ZINE_14_PM,
        rotate_flags=ZINE_14_RF
    )

    print(f"saving output to: {args.output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a single-sheet zine from a 14 page pdf.")
    parser.add_argument("--input", "-i", help="path to the input pdf with 14 pages", required=True)
    parser.add_argument("--output", "-o", help="path for saving output pdf", default="output.pdf")
    args = parser.parse_args()
    main(args)