import jieba
import re
from utils import *
import os 

path = './DB_PreInput_film2'
FileNames = get_files(path)
# FileNames = ['PreInput_0.txt']
count = 0
for filename in FileNames:
    with open(path+'/'+filename,encoding='utf-8') as f:
        new_fn = './DB_SegInput_film2/SegInput_'+str(count)+'.txt'
        title = 1
        for line in f.readlines():
            line = line.strip()
            line = line.replace(' ','')
            line = line.replace('\n','')
            line = re.sub(r"[^\u4e00-\u9fa5]","",line)
            seg_list = []
            if(title == 1):
                l = line.split(' ')
                for ll in l:
                    ll = ll.replace(' ','')
                    seg_list+=list(jieba.cut(ll,cut_all=False))
            else:
                seg_list = jieba.cut(line,cut_all=False)
                seg_list = list(seg_list)

            with open(new_fn,'a',encoding='utf-8')as f:
                f.write((' ').join(seg_list))
                if(title == 1):
                    f.write('\n')
                    title = 0
                else:
                    f.write(' ')
        print('----',filename,'finish ----')
    count+=1