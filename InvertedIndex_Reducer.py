# !/usr/bin/python3
from operator import itemgetter
import sys
import os
import math


'''
(token,(file:TokenCount:tf:[pos]))
-> (token,(file:TokenCount:tf*idf:[pos]))
'''
# 文件总数
N = 9545+8077

# 从map中读取的内容再计算idf = log2（N/FileCount）
# N：文件总数
# FileCount：统计出来token在所有文件中出现了多少次
dict_FileTokenTfPos={}
for line in sys.stdin:
    token,M_FileTokenPos = line.split('\t')
    M_FileTokenPos = M_FileTokenPos.split('|')
    FileCount=len(M_FileTokenPos)
    idf = math.log2(N/FileCount)
    for FileTokenPos in M_FileTokenPos:
        filename,TokenCount,tf,pos = FileTokenPos.split(':')
        pos = pos.replace('\n','')
        tf = float(tf)
        tfidf = round(tf*idf,5)
        if(dict_FileTokenTfPos.get(token,0)):
            dict_FileTokenTfPos[token]+='|'+filename+':'+TokenCount+':'+str(tfidf)+':'+pos
        else:
            dict_FileTokenTfPos[token] = filename+':'+TokenCount+':'+str(tfidf)+':'+pos

for token,FileTCTfidfPos in dict_FileTokenTfPos.items():
    print("%s\t%s"%(token,FileTCTfidfPos))