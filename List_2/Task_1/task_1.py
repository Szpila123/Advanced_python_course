#!/usr/bin/python3
import csv
import argparse
import sys
import dHondt as dh

description = "Analyzing election results and print number of mandates based on d'Hondt method"


def create_arguments_parser() -> argparse.ArgumentParser:
    '''Create parser for cmd line'''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('results',
                        type=str,
                        help='CSV file name that holds election results data',
                        action='store')
    parser.add_argument('districts',
                        type=str,
                        help='CSV file name that holds election districts data',
                        action='store')
    parser.add_argument('--token',
                        required=False,
                        type=str,
                        default='KOMITET',
                        help='Word that will be used to recognize results columns',
                        action='store')
    parser.add_argument('--minority_token',
                        required=False,
                        type=str,
                        default='MNIEJSZOŚĆ',
                        help='Word that will be used to recognize minorities',
                        action='store')
    parser.add_argument('--district_token',
                        required=False,
                        type=str,
                        default='Numer okręgu',
                        help='Word that will be used to recognize district header',
                        action='store')
    parser.add_argument('--mandates_token',
                        required=False,
                        type=str,
                        default='Liczba mandatów',
                        help='Word that will be used to recognize number of mandates header',
                        action='store')
    parser.add_argument('--threshold',
                        required=False,
                        type=int,
                        default='5',
                        help='What is minimum prcentage threshold to get a mandate',
                        action='store')
    return parser


if __name__ == '__main__':
    # Parse command arguments
    args = create_arguments_parser().parse_args(sys.argv[1:])

    # Parse results file
    header, data = [], []
    with open(args.results, 'r') as file:
        results_dialect = csv.Sniffer().sniff(''.join(file.readlines(5)))
        file.seek(0)
        results_reader = csv.reader(file, dialect=results_dialect)
        header = next(results_reader)
        data = list(results_reader)
    name_idxs = [num for num, col_name in enumerate(header) if args.token in col_name]
    number_idx = header.index(args.district_token)

    # Parse districts file
    header_districts, districts = [], []
    with open(args.districts, 'r') as file:
        districts_dialect = csv.Sniffer().sniff(''.join(file.readlines(5)))
        file.seek(0)
        districts_reader = csv.reader(file, dialect=districts_dialect)
        header_districts = next(districts_reader)
        districts = list(districts_reader)
    district_number_idx = header_districts.index(args.district_token)
    district_mandates_idx = header_districts.index(args.mandates_token)

    # Count votes
    results = dict(zip([header[idx] for idx in name_idxs], [0] * len(name_idxs)))
    for row in data:
        votes, mandates = dict(), 0

        for idx in name_idxs:
            votes[header[idx]] = int(row[idx]) if row[idx] else 0

        for district_row in districts:
            if district_row[district_number_idx] == row[number_idx]:
                mandates = int(district_row[district_mandates_idx])
                break

        for key, value in dh.analyze(votes, mandates, args.minority_token).items():
            results[key] += value

    # Print results
    for key, val in sorted(results.items(), key=lambda x: x[1], reverse=True):
        print(key, ':', val)
