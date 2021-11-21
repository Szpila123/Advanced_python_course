"""
Zadanie 2.
Zaprogramuj system do monitorowania stron, który sprawdza, czy jakaś strona nie
zmieniła zawartości. Zakładamy, że nasz program może monitorować więcej niż
jedną stronę; zakładamy też że sprawdzanie odbywa się co jakiś czas (np. co 1
minutę).
Zakładamy w tym zadaniu, że układ strony zmienia się rzadko, jedynie zmieniają
się pojedyncze elementy tego układu, dlatego jeśli program wykryje zmianę to
niech tylko zwróci to, co się zmieniło.
"""

"""
Note: this program uses http, thus it's unsafe
"""

import urllib.request
import re
import argparse
import sys
import logging
import signal
import tempfile
import difflib
import time
URL_RE = 'http://([a-zA-Z0-9]+\.)+[a-zA-Z]+'


def create_arguments_parser() -> argparse.ArgumentParser:
    """Create parser for cmd line"""

    parser = argparse.ArgumentParser(
        description='Check for updates of sites under given urls, print any changes to stdout')

    parser.add_argument('-f', '--file',
                        required=False,
                        type=argparse.FileType('r'),
                        help='Use urls from given file, urls will be parsed with regular expression: "([a-zA-Z0-9]+.)+[a-zA-Z]+"',
                        action='store')
    parser.add_argument('-u', '--url',
                        required=False,
                        nargs='*',
                        type=str,
                        help='Explicitly adds given urls to checking list',
                        action='store')
    parser.add_argument('-p', '--period',
                        required=False,
                        type=int,
                        default=1,
                        help='Period in seconds between the end of one requests batch and the start of a next one',
                        action='store')
    parser.add_argument('-v', '--verbose',
                        help='Print additional information',
                        action='store_true')
    parser.add_argument('-n', '--noprint',
                        help='Do not print any information about content (new content, content diff)',
                        action='store_false')
    return parser


class ProgramStopped(Exception):
    pass


def signal_handler(signum, frame):
    logging.warning(f'Received signal {signum}, exiting...')
    raise ProgramStopped


def observe(urls: list[str], period: int, print_content: bool):
    """Periodicly send get requests to urls and watch for any changes"""
    if not urls or period < 1:
        return

    cache = dict(zip(urls, [{'file': tempfile.TemporaryFile(), 'hash': None} for _ in urls]))
    try:
        while(True):
            for url in urls:
                print(f'Requesting: {url}')
                with urllib.request.urlopen(url) as f:
                    if f.status == 200:
                        data = f.read().decode('utf-8')
                        data_hash = hash(data)

                        if not cache[url]['hash']:
                            """First successful request"""
                            cache[url]['hash'] = data_hash
                            if print_content:
                                print(f'Content of {url}:\n' + data)
                            cache[url]['file'].write(bytes(data, 'utf-8'))
                            cache[url]['file'].seek(0)

                        elif cache[url]['hash'] != data_hash:
                            """Data changed"""
                            file = cache[url]['file']
                            diff = difflib.unified_diff(file.read().decode('utf-8').split(),
                                                        data.split(), fromfile='Old', tofile='New')
                            """Update content and hash"""
                            file.truncate(0)
                            file.write(bytes(data, 'utf-8'))
                            file.seek(0)
                            cache[url]['hash'] = data_hash
                            """Print diff"""
                            print(f'Content of {url} changed')
                            if print_content:
                                for line in diff:
                                    print(line)
                        else:
                            """Data is the same"""
                            print(f'Contect of {url} is the same')

                    else:
                        print(f'{url} responeded with {f.status}, no diff created')
            time.sleep(period)

    except ProgramStopped:
        print('Program was stopped, exiting...')
    except Exception as err:
        logging.error(f'Error occured: {err.args}, exiting...')
        logging.error(f'{err.with_traceback()}')

    finally:
        for file in [entry['file'] for entry in cache.values()]:
            file.close()


if __name__ == "__main__":
    """Set signal handlers"""
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    """Parse command arguments"""
    args = create_arguments_parser().parse_args(sys.argv[1:])

    """Set logging"""
    if args.verbose:
        log_level = logging.WARNING
    else:
        log_level = logging.ERROR
    logging.basicConfig(format='%(levelname)s: %(message)s', level=log_level)
    logging.warning('Verbose flag set')

    """Gather URLs"""
    urls = []
    url_regex = re.compile(URL_RE)

    if args.file:
        logging.warning('URL File: ' + str(args.file.name))
        with args.file as input_file:
            urls += [url.group() for url in url_regex.finditer(input_file.read())]

    if args.url:
        urls += [url for url in args.url if url_regex.match(url)]

    if urls:
        print('Valid URLs:\n\t' + '\n\t'.join(urls))
    else:
        logging.error('No valid url found, exiting...')
        exit(1)

    """Observe urls for changes"""
    observe(urls, args.period, args.noprint)
