#!/usr/bin/env python3

import sys
import os
import json

guserc = list()
guserd = list()


def main(argv):
    """
    read all of files in directory inputed recursively.
    rename and copy(instead move for safety) file to specific rules.
    """
    os.makedirs('./outputs', exist_ok = True)

    dir_queue = argv[1:]
    file_queue = get_all_files(dir_queue)

    process_files(file_queue)



def process_files(file_queue):
    global guserc
    global guserd
    for target in file_queue:
        filename = target.split('/')[-1]
        user = target.split('/')[-2]
        if target.split('/')[-3] == 'fitcraft_data':
            if user not in guserc:
                guserc.append(user)
            user = guserc.index(user) + 1
            user = 'C' + '{:02}'.format(user)
        elif target.split('/')[-3] == 'fitnessonly_data':
            if user not in guserd:
                guserd.append(user)
            user = guserd.index(user) + 1
            user = 'D' + '{:02}'.format(user)
        date = filename[0:4] + filename[5:7] + filename[8:10]
        data = (filename.split('_')[1]).split('.')[0]

        target_path = (data 
                     + '/' 
                     + date 
                     + '/' 
                     + user 
                     + '.json')
        target_path = './outputs/' + target_path

        os.makedirs('./outputs/' + data + '/' + date, exist_ok = True)
        with open(target, 'r') as read_filep:
            with open(target_path, 'w') as write_filep:
                try:
                    read_json = json.load(read_filep)
                except Exception as e:
                    print(target)
                    print(e)
                    sys.exit()
                json.dump(read_json, write_filep,
                          indent = 4)

        print(target_path)

    print('# Group C is fitcraft')
    print('C = ', guserc)
    print('# Group D is only fitbit')
    print('D = ', guserd)





def get_all_files(dir_queue):
    file_queue = list()

    while len(dir_queue) > 0:
        path = dir_queue.pop()
        with os.scandir(path) as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    if entry.path.split('.')[-1] != 'json':
                        continue
                    file_queue.append(entry.path)
                else:
                    dir_queue.append(entry.path)

    return file_queue
        


# is it good thing, right?
if __name__ == '__main__':
    sys.exit(main(sys.argv))
