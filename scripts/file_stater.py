#!/usr/bin/python
# coding: utf-8


# listing files in /etc
import json  # for dumping
import datetime  # for converting unix time to human datetime.datetime
import os  # for os.walk and os.stat


def list_all_files(in_folder, filter=''):
    """List all files in_folder with filter"""
    result = []
    for dirpath, dirnames, filenames in os.walk(in_folder):
        for filename in filenames:
            if filename.endswith(filter):
                result.append(os.path.join(dirpath, filename))
    return result


def from_timestamp_to_human_readable(unixtime):
    """converts unixtime to datetime.datetime and then to human readable string
    unixtime is expected to be string"""
    date_obj = datetime.datetime.fromtimestamp(int(unixtime))
    return date_obj.strftime('%Y.%m.%d %H:%M:%S')


def open_file_and_grep_v(path, match='#'):
    "returns contets of a file grepped by invert match"
    result = ''
    try:
        with open(path) as iowrap:
            for line in iowrap.readlines():
                if line.startswith(match):
                    continue
                else:
                    result += "{}".format(line)
    except PermissionError:
        return False
    return result


def main(path, filter):
    "the main logic"

    conf_files_in_etc = list_all_files(path, filter)

    # use each filepath from list conf_files_in_etc to create a key in files_dict dictionary
    files_dict = {}
    for key in conf_files_in_etc:
        files_dict[key] = {}  # create new dictionary for each key

    for file_path in files_dict.keys():  # itterate through keys (in this case paths to file)
        if os.path.exists(file_path):  # check if the file exists
            stat = os.stat(file_path)  # save the stat for current file
            # get all the info from stat we want
            files_dict[file_path]['size'] = stat.st_size
            files_dict[file_path]['group'] = stat.st_gid
            files_dict[file_path]['user'] = stat.st_uid
            files_dict[file_path]['time_access'] = stat.st_atime
            files_dict[file_path]['time_access_d'] = from_timestamp_to_human_readable(
                stat.st_atime)
            files_dict[file_path]['time_modify'] = stat.st_mtime
            files_dict[file_path]['time_modify_d'] = from_timestamp_to_human_readable(
                stat.st_mtime)
            files_dict[file_path]['time_creation'] = stat.st_ctime
            files_dict[file_path]['time_creation_d'] = from_timestamp_to_human_readable(
                stat.st_ctime)
            # do whatever else you want with the files
            files_dict[file_path]['uncommented_contents'] = open_file_and_grep_v(
                file_path)

    # now save the results to json
    with open('result.json', 'x') as iowrap:
        json.dump(files_dict, iowrap)


if __name__ == '__main__':
    main('/etc', '.conf')
