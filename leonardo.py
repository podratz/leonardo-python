#!/usr/bin/env python3
import argparse
import itertools
import math
from types import NotImplementedType


class GeometricSequence:
    def __init__(self, common_ratio: float, scale_factor: float = 1):
        self.common_ratio = common_ratio
        self.scale_factor = scale_factor

    def __call__(self, n: int = 1) -> float: 
        return self.scale_factor * (self.common_ratio ** n)

    def __getitem__(self, subscript) -> list[float]:
        if isinstance(subscript, int):
            return [self(subscript)]

        if subscript.start is None:
            raise KeyError('sequence requires pre-determined start')
        start = subscript.start

        if subscript.stop is None and subscript.step is not None:
            raise KeyError('sequence with step needs pre-determined stop')
        stop = subscript.stop

        if subscript.step == 0:
            raise ValueError('slice step cannot be zero')
        step = subscript.step or 1

        return [self(index) for index in range(start, stop, step)]

    def __iter__(self):
        for index in itertools.count():
            yield self(index)

    def __eq__(self, other: object) -> NotImplementedType | bool:
        if not isinstance(other, GeometricSequence):
            return NotImplemented
        return (self.common_ratio == other.common_ratio
            and self.scale_factor == other.scale_factor)


bronce_ratio = (3 + math.sqrt(13)) / 2
class BronceSequence(GeometricSequence):
    def __init__(self, scale_factor: int | float = 1):
        super().__init__(bronce_ratio, scale_factor=scale_factor)


silver_ratio = (2 + math.sqrt(8)) / 2
class SilverSequence(GeometricSequence):
    def __init__(self, scale_factor: int | float = 1):
        super().__init__(silver_ratio, scale_factor=scale_factor)


golden_ratio = (1 + math.sqrt(5)) / 2
class GoldenSequence(GeometricSequence):
    def __init__(self, scale_factor: int | float = 1):
        super().__init__(golden_ratio, scale_factor=scale_factor)


def parse_args():
    parser = argparse.ArgumentParser(
        prog='Leonardo',
        description='Compute metallic means.',
        epilog='by N. M. Podratz'
    )
    # positional argument
    parser.add_argument(
        'scale',
        metavar='S',
        nargs='?',
        type=int,
        default=1,
        help='The scale factor'
    )
    #options
    parser.add_argument(
        '-m',
        '--metal',
        type=int,
        help='The mean\'s metal',
        default=GoldenSequence
    )
    parser.add_argument(
        '-p',
        '--prev',
        type=int,
        nargs='?',
        default=0,
        help='number of preceding values'
    )
    parser.add_argument(
        '-n',
        '--next',
        type=int,
        nargs='?',
        default=1,
        help='number of succeeding values'
    )
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    metal = args.metal  # assume Gold
    scale_factor = args.scale or 1
    start = 0 if args.prev is None else -args.prev + 1
    stop = 2 if args.next is None else args.next + 1
    golden_numbers = GoldenSequence(scale_factor)
    golden_strings = map(str, golden_numbers[start:stop])
    output = '\n'.join(golden_strings)
    print(output)


if __name__ == '__main__':
    main()
