#!/usr/bin/python3

import json
import argparse
import os


def main(source: str, target: str, output: str, number: int) -> None:
    with open(source, "r", encoding='utf-8') as file1:
        source_sentences = file1.readlines()
    with open(target, "r", encoding='utf-8') as file2:
        target_sentences = file2.readlines()

    with open(output, "w", encoding='utf-8') as file:
        data_array = []
        ids, source, text = "", "", ""

        for i, (source_sen, target_sen) in \
                enumerate(zip(source_sentences, target_sentences)):
            ids += target + "_" + str(i + 1) + "\n"
            source += source_sen.strip() + "\n"
            text += target_sen.strip() + "\n"

            if i % number == number - 1 or i == len(source_sentences) - 1:
                data_array.append({
                    "data":
                        {"ids": ids[:-1],
                         "source": source[:-1],
                         "text": text[:-1]}
                })
                ids, source, text = "", "", ""

        file.write(json.dumps(data_array, indent=1))


def init_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-s', '--source', nargs='?', required=True,
                        help='Source txt, file with source sentences')
    parser.add_argument('-t', '--target', nargs='?', required=True,
                        help='Target txt, file with target sentences')
    parser.add_argument('-o', '--output', nargs='?', required=True,
                        help='Name of the output file to be imported')
    parser.add_argument('-n', '--number', nargs='?', default=10, type=int,
                        help='Number of lines on one page')

    args = parser.parse_args()

    if not os.path.isfile(args.source) or not os.path.isfile(args.source):
        raise Exception("Input doesn't exist or is a path")

    return args


if __name__ == "__main__":
    args = init_args()
    main(args.source, args.target, args.output, args.number)
