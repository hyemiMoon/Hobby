#!/usr/bin/env python3

import sys
import os
import logging
import json

FORMAT = '%(created)s:%(levelno)s:%(message)s'
logging.basicConfig(stream = sys.stdout,
                    format = FORMAT,
                    level = logging.DEBUG)

def main(argv):
    if len(argv) < 2:
        logging.debug('We need argument for path')
        return
    dir_queue = list()

    for arg in argv:
        if os.path.isdir(arg) == True:
            dir_queue.append(arg)

    for file_path in get_file_list(dir_queue):
        print(get_data(file_path))
        # we can access all of data
        break



def get_file_list(dir_queue):
    file_queue = list()

    while len(dir_queue) > 0:
        path = dir_queue.pop()
        with os.scandir(path) as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    #file_queue.append(entry.path)
                    yield entry.path
                else:
                    dir_queue.append(entry.path)

    return file_queue



def get_data(file_path):
    with open(file_path, 'r') as rfile:
        data = json.load(rfile)
        return data



# is it good thing, right?
if __name__ == '__main__':
    sys.exit(main(sys.argv))