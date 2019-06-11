import yaml
import sched
import time
import datetime
import threading
import sys
import subprocess
import os

no_list = [1,
           2,
           4,
           6,
           7,
           8,
           10,
           11,
           12,
           13,
           14,
           15,
           16,
           17,
           19,
           20,
           23,
           25,
           26,
           27,
           28,
           29,
           30,
           31,
           32,
           33,
           34,
           36,
           38,
           39,
           40,
           41,
           42,
           43,
           44,
           45,
           46,
           47,
           48,
           49,
           50,
           51,
           52,
           54,
           55,
           56,
           57,
           58,
           59,
           60,
           61,
           62,
           63,
           64,
           66,
           67,
           69,
           71,
           72,
           73,
           74,
           77,
           78,
           79,
           80]
no_list.sort()

def processing(i):
    res = subprocess.call(['python', 'execute_spider.py', str(i)])
    #print(res)


#for i in range(0, 100000):  #request const.RequestNum

try:
    os.remove("request.log")
except OSError:
    pass

for i in no_list:  # request const.RequestNum
    processing(i)
