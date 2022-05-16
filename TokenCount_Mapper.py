# !/usr/bin/python3
import sys
import os

'''
(token@file,[pos])
-> (file,(token:[pos]))
'''
for line in sys.stdin:
    tokenfile,pos = line.split('\t')
    pos = pos.replace('\n','')
    token,file = tokenfile.split('@')
    print("%s\t%s"%(file,token+':'+pos))
