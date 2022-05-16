# !/usr/bin/python3
from operator import itemgetter
import sys

'''
(token@file,pos)
-> (token@file,[pos])
'''
dict_tokenpos = {}
for line in sys.stdin:
    line = line.strip()
    s  = line.split('\t')
    # print(line)
    tokenfile, pos = s[0],s[1]
    try:
        if(dict_tokenpos.get(tokenfile,0)):
            dict_tokenpos[tokenfile]+=";"+str(pos)
        else:
            dict_tokenpos[tokenfile] = str(pos)
    except ValueError:
        continue

for tokenfile,pos_list in dict_tokenpos.items():
    print("%s\t%s"%(tokenfile,pos_list))