import argparse

from .bronce import Bronce
from .gold import Gold
from .silver import Silver

__all__ = ["Bronce", "Silver", "Gold"]


def parse_args():
    parser = argparse.ArgumentParser(
        prog="Leonardo",
        description="Compute metallic means.",
        epilog="by N. M. Podratz",
    )
    # positional argument
    parser.add_argument(
        "scale", metavar="S", nargs="?", type=int, default=1, help="The scale factor"
    )
    # options
    # parser.add_argument(
    #     "-m", "--metal", type=int, help="The mean's metal", default=GoldenSequence
    # )
    parser.add_argument(
        "-p",
        "--prev",
        type=int,
        nargs="?",
        default=0,
        help="number of preceding values",
    )
    parser.add_argument(
        "-n",
        "--next",
        type=int,
        nargs="?",
        default=1,
        help="number of succeeding values",
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    metal = args.metal  # assume Gold
    scale_factor = args.scale or 1
    start = 0 if args.prev is None else -args.prev + 1
    stop = 2 if args.next is None else args.next + 1
    golden_numbers = Gold.sequence(scale_factor)
    golden_strings = map(str, golden_numbers[start:stop])
    output = "\n".join(golden_strings)
    print(output)


if __name__ == "__main__":
    main()
