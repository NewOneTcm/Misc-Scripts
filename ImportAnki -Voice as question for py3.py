#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-18 17:13:10
# @Author  : Newone
# @Link    : www.dajingtcm.com
# @About   : from https://github.com/emmaping/Misc-Scripts/blob/master/ImportAnki%20-Voice%20as%20question.py
# @Version : $Id$


import logging
logging.basicConfig(level=logging.INFO)

import re
import os
import sys
import csv
#from sys import argv
import glob
import time


output = "Tobeimport.csv"

###################################
# writing test
# ######################################


def write_test():
    headers = ['class', 'name', 'sex', 'height', 'year']

    rows = [
        [1, 'xiaoming', 'male', 168, 23],
        [1, 'xiaohong', 'female', 162, 22],
        [2, 'xiaozhang', 'female', 163, 21],
        [2, 'xiaoli', 'male', 158, 21]
    ]

    with open(output, 'w', newline='')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

######################################
# read test
# ####################################


def read_test():
    with open('test.csv')as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            print(row)


def change_filename(rq):

    logging.info("start to change_filename")
    i = 1

    for file in glob.glob(r'*.mp3'):
        newname = rq + '_' + str(i) + ".mp3"
        os.rename(file, newname)
        i = i + 1

    logging.info("end to change_filename")


def write2csv():
    # curpath = os.getcwd()
    # lrcfiles = curpath + "//*.lrc"

    # logging.info(lrcfiles)
    flist = glob.glob(r'*.lrc')

    logging.info(flist)

    pattern1 = re.compile(r'00]([\S\s]*)\t+')  # () is the right thing
    pattern3 = re.compile(r'00]([\S\s]*)\t?')
    pattern2 = re.compile(r'\t\t([\S\s]*)\n')

    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))

    # change_filename(rq)

    i = 0
    for file in flist:
        i = i + 1
        with open(file) as fh:
            logging.info("reading file....")
            content = fh.readline()
            logging.info(file)
            logging.info(content)

            english = pattern1.findall(content)
            if not english:
                english = pattern3.findall(content)
            chinese = pattern2.findall(content)

            logging.info('english is:%r' % english)
            logging.info('chinese is:%r' % chinese)

            mp3file = file[:-3] + "mp3"  # add a mp3 at the end of the file.
            newname = rq + '_' + str(i) + ".mp3"
            if len(english) != 0:
                os.rename(mp3file, newname)
            else:
                print('the len of english is zero!!!1')

            logging.info(mp3file)
            logging.info(newname)

            question = "[sound:" + newname + "]"
            if not chinese:
                answer = english[0]
            else:
                answer = english[0] + '\n' + chinese[0]
            logging.info(answer)

            #####################################
            # write to file
            # ###################################
            with open(output, 'a', newline='', encoding='utf-8')as fw:
                f_csv = csv.writer(fw)
                f_csv.writerow([question, answer])


if __name__ == "__main__":
    write2csv()
