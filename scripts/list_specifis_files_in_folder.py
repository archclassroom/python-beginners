#!/usr/bin/env python
import os
import sys
"""
prints all the files in the folder X
"""


def main():
    print('you launched', sys.argv)
    if len(sys.argv) == 2:
        output = listing_files_in_directory(sys.argv[1])
    elif len(sys.argv) == 3:
        output = listing_files_in_directory(sys.argv[1], sys.argv[2])
    else:
        print('at least dir is required')
        sys.exit(1)
    if not output:
        sys.exit(2)
    else:
        sys.exit(0)


def listing_files_in_directory(dir, filter='.cpp'):
    """
    does os.walk in the specific directory
    filter has to start with .`
    """
    if not filter.startswith('.'):
        print('please input filter filter starting with .')
        return False
    if os.path.isdir(dir):
        for dirpath, dirnames, filenames in os.walk(dir):
            for file in filenames:
                if file.endswith(filter):
                    print('{2} files in Directory:{0}\n{1}'.format(dirpath, filenames, filter))
    else:
        print(dir, 'is not a directory')
        return False
    return True


if __name__ == '__main__':
    main()
