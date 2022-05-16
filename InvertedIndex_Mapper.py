# !/usr/bin/python3
from operator import itemgetter
import sys
import os

'''
(token,(file:TokenCount:[pos]))
-> (token,(file:TokenCount:tf:[pos]))
'''

# 从本地文件中获取TokenCount Mapreduce过程中获得的每个文件中token的数量
# key = filename
# value = FileTokenNum
FileTokenCount = {}
with open('FileTokenCount.txt')as f:
    for line in f.readlines():
        line = line.strip()
        filename,TokenSum = line.split('\t')
        TokenSum = int(TokenSum)
        FileTokenCount[filename] = TokenSum

# 计算tf = TokenCount/FileTokenNum
# TokenCount：token在filename中出现的次数
dict_FileTokenTfPos={}
for line in sys.stdin:
    token,M_FileTokenPos = line.split('\t')
    M_FileTokenPos = M_FileTokenPos.split('|')
    for FileTokenPos in M_FileTokenPos:
        filename,TokenCount,pos = FileTokenPos.split(':')
        pos = pos.replace('\n','')
        pos = pos.split(';')
        TokenCount = int(TokenCount)
        tf = round(TokenCount/FileTokenCount[filename],3)
        if(dict_FileTokenTfPos.get(token,0)):
            dict_FileTokenTfPos[token]+='|'+filename+':'+str(TokenCount)+':'+str(tf)+':'+(';').join(pos)
        else:
            dict_FileTokenTfPos[token]=filename+':'+str(TokenCount)+':'+str(tf)+':'+(';').join(pos)

for token,FileTokenTfPos in dict_FileTokenTfPos.items():
    print('%s\t%s'%(token,FileTokenTfPos))