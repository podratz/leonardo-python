import argparse

from . import Bronce, Gold, Silver


def parse_args():
    parser = argparse.ArgumentParser(
        prog="leonardo",
        description="generates metallic numbers",
        epilog="by N. M. Podratz",
    )
    # positional argument
    parser.add_argument(
        "scale", metavar="S", nargs="?", type=int, default=1, help="scale factor"
    )
    # options
    parser.add_argument(
        "-m",
        "--metal",
        nargs="?",
        choices=["g", "s", "b"],
        default="g",
        const="g",
        help="specify the metal",
    )
    parser.add_argument(
        "-p",
        "--prev",
        type=int,
        nargs="?",
        default=0,
        help="specify the number of preceeding numbers",
    )
    parser.add_argument(
        "-n",
        "--next",
        type=int,
        nargs="?",
        default=1,
        help="specify the number of succeeding numbers",
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    scale_factor = args.scale or 1
    start = 0 if args.prev is None else -args.prev + 1
    stop = 2 if args.next is None else args.next + 1
    match args.metal:
        case "s":
            metal = Silver
        case "b":
            metal = Bronce
        case _:
            metal = Gold
    metal_numbers = metal.sequence(scale_factor)
    metal_strings = map(str, metal_numbers[start:stop])
    output = "\n".join(metal_strings)
    print(output)


if __name__ == "__main__":
    main()
