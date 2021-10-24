import argparse
import sys
import simplify

def create_arguments_parser() -> argparse.ArgumentParser:
    '''Create parser for cmd line'''
    parser = argparse.ArgumentParser(description='Program for simplifing text')
    parser.add_argument('file',
                        type=str,
                        help='File which will be simplified',
                        action='store')
    parser.add_argument('--words',
                        required=False,
                        type=int,
                        default='100',
                        help='Maximal word count of text after simplifing',
                        action='store')
    parser.add_argument('--len',
                        required=False,
                        type=int,
                        default='8',
                        help='Maximal word length',
                        action='store')
    return parser

if __name__ == '__main__':
    # Parse command arguments
    args = create_arguments_parser().parse_args(sys.argv[1:])

    # Read file content
    content = ''
    with open(args.file, 'r') as file:
        content = file.readlines()
    
    print(simplify.simplify(' '.join(content), args.len, args.words))