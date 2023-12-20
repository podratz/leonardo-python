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
        "scale", metavar="S", default=1, type=int, nargs="?", help="scale factor (int)"
    )
    # options
    parser.add_argument(
        "-m",
        "--metal",
        metavar="M",
        choices=["g", "s", "b", "gold", "silver", "bronce"],
        default="g",
        const="g",
        nargs="?",
        help="metal (choose from {g[old], s[ilver], b[ronce]})",
    )
    parser.add_argument(
        "-p",
        "--prev",
        metavar="P",
        default=0,
        type=int,
        nargs="?",
        help="number of preceeding numbers (int)",
    )
    parser.add_argument(
        "-n",
        "--next",
        metavar="N",
        default=1,
        type=int,
        nargs="?",
        help="number of succeeding numbers (int)",
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    scale_factor = args.scale or 1
    match args.metal:
        case "s" | "silver":
            metal = Silver
        case "b" | "silver":
            metal = Bronce
        case "g" | "gold":
            metal = Gold
        case arg:
            raise ValueError(f"{arg} is not a valid metal")
    metal_numbers = metal.sequence(scale_factor)
    start = 0 if args.prev is None else -args.prev + 1
    stop = 2 if args.next is None else args.next + 1
    metal_strings = map(str, metal_numbers[start:stop])
    output = "\n".join(metal_strings)
    print(output)


if __name__ == "__main__":
    main()
