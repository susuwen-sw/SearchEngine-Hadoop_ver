# !/usr/bin/python3
from operator import itemgetter
import sys
import os

dict_FileCount = {}

'''
(file,(token:[pos]))
-> (token,(file:TokenCount:[pos]))
'''
dict_TokenMap = {}
for line in sys.stdin:
    file,tokenpos = line.split('\t')
    token,pos = tokenpos.split(':')
    pos = pos.replace('\n','')
    TokenCount = len(pos.split(';'))
    if(dict_FileCount.get(file,0)):
        dict_FileCount[file]+=TokenCount
    else:
        dict_FileCount[file] = TokenCount
    if(dict_TokenMap.get(token,0)):
        dict_TokenMap[token]+='|'+file+':'+str(TokenCount)+':'+pos
    else:
        dict_TokenMap[token]=file+':'+str(TokenCount)+':'+pos

for token,tokenmap in dict_TokenMap.items():
    print("%s\t%s"%(token,tokenmap))

for file,FileCount in dict_FileCount.items():
    with open('FileTokenCount.txt','a') as f:
        f.write("%s\t%s"%(file,str(FileCount)))
        f.write('\n')

# for file,FileCount in dict_FileCount.items():
#     if(os.path.exists('/user/hduser_/FileTokenCount')):
#         pass
#     else:
#         os.mkdir('/user/hduser_/FileTokenCount')
#     print("%s\t%s"%(file,str(FileCount)))