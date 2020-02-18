#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-18 17:13:10
# @Author  : Newone (wenlong_cheng@dajingtcm.com)
# @Link    : www.dajingtcm.com
# @About   : This is a test
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


def write2csv():
    curpath = os.getcwd()
    lrcfiles = curpath + "//*.lrc"
    logging.info(lrcfiles)
    flist = glob.glob(lrcfiles)
    logging.info(flist)
    # writer = csv.writer(file(output, 'wb+'))
    # pattern1 = re.compile(r'00]([\s\S]*) \t')
    # pattern2 = re.compile(r'\t([\s\S]*)')


# def rAndw():
#     curpath = os.getcwd()
#     lrcfiles = curpath + "//*.lrc"
#     flist = glob.glob(lrcfiles)
#     writer = csv.writer(file(output, 'wb+'))
#     pattern1 = re.compile(r'00]([\s\S]*) \t')
#     pattern2 = re.compile(r'\t([\s\S]*)')
#     i = 0
#     for f in flist:
#         i = i + 1
#         fh = file(f, 'r')
#         content = fh.read()
#         english = pattern1.findall(content)
#         chinese = pattern2.findall(content)

#         print(content)

#         print(english)
#         print(chinese)
#         mp3file = f[:-3] + "mp3"
#         newname = str(time.time()) + str(i) + ".mp3"
#         print(mp3file)
#         print(newname)
#         os.rename(mp3file, newname)
#         question = "[sound:" + newname + "]"

#         if not english:
#             answer = content[10:]
#         else:
#             answer = english[0] + "   " + question
#         writer.writerow([question, answer])
#         fh.close()
#     del writer

if __name__ == "__main__":
    write2csv()
