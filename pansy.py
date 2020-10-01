#!/usr/bin/env python3

from lib.interpreter import run


def run_pansy_file(filepath):
    _ret, _exc = run('<stdin>', 'run("{}")'.format(filepath))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    action = parser.add_argument(dest="file")

    argument, _ = parser.parse_known_args()
    run_pansy_file(filepath=argument.file)
