#!/usr/bin/python
# coding: utf-8

import datetime  # for getting current time and timedelta
import time  # for converting to unixtime, for some reason (maybe there is a better way?)
import sys  # for printing to stdout


def convert_datetime_to_unixtime(datetime):
    """convert datetime.datetime to unix time int"""
    return time.mktime(datetime.timetuple())


def calculate_percentage(total, remaining):
    one_unit = total / 100
    prct = remaining / one_unit
    return(prct)


def main(remaining_time=120, stdout=True):
    """takes time in minutes, default is 90"""
    now = datetime.datetime.now()
    end = now + datetime.timedelta(minutes=remaining_time)
    total_class_time = convert_datetime_to_unixtime(end) - convert_datetime_to_unixtime(now)
    remaining_class_time = total_class_time
    if stdout:
        sys.stdout.write('\n')
    while remaining_class_time > 0:
        now = datetime.datetime.now()
        remaining_class_time -= 1
        thing_to_print = ('{:4.2f}% that is {:4.3f} minutes'.format(
                calculate_percentage(total_class_time, remaining_class_time),  # 0
                remaining_class_time / 60)) # 1
        if stdout:
            sys.stdout.write(thing_to_print + '\n')  # TODO do overwrite
        else:
            print(thing_to_print)
        time.sleep(1)  # not super precises


if __name__ == '__main__':
    main()
