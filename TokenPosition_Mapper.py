# !/usr/bin/python3
import sys
import os
# from utils import *

'''
file
-> (token@file,pos)
'''
dict_file = {}
for line in sys.stdin:
    token_list = line.split(' ')
    # print(token_list)
    # with open('local.txt','a') as f:
    #     f.write(os.environ['HOME'])
    filename = os.environ["map_input_file"]
    filename = filename.split('/')[-1][:-4]
    # filename='1'
    title  = 0
    if(dict_file.get(filename,0)):
        pass
    else:
        title = 1
        dict_file[filename] = 1
    # filename = '1'
    for i in range(len(token_list)):
        key = token_list[i].replace('\n','')+'@'+filename
        if(key[0]!='@'):
            position = str(title)+'%'+str(i)
            print("%s\t%s" % (key,position))
            # with open('rlt_map.txt','a')as f:
            #     f.write("%s\t%s" % (key,position))
            #     f.write('\n')