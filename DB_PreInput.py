import re
import os
from zhon.hanzi import punctuation

def get_files(path):
    FileNames = []
    for filepath,dirnames,filenames in os.walk(path):
        FileNames = filenames
    return FileNames

path = './DB_RawData_film2'
FileNames = get_files(path)
# FileNames = ['RawInput_234.txt']
count = 0
for filename in FileNames:
    with open('./DB_RawData_film2/'+filename,'r',encoding='utf-8')as f:
        FileName = './DB_PreInput_film2/PreInput_'+str(count)+'.txt'
        title = 1
        for line in f.readlines():
            line = line.replace(' ','')
            line = re.sub('[a-zA-Z]','',line)
            line = re.sub('[0-9]','',line)
            punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}'
            line = re.sub(r"[%s]+" %punc, " ",line)
            line = re.sub(r'[%s]+'%punctuation," ",line)
            # print(line)
            for bd in ['」','「','[',']','［','］','】','【','”','“','＞','＜','５','８','｛','｝','～','`','·']:
                line = line.replace(bd,' ')
            # line = re.sub(r"[^\u4e00-\u9fa5]","",line)
            line = line.strip()
            line = line.split(' ')
            line[-1] = line[-1].replace('\n','')
            # print(line)
            if(title == 1):
                with open(FileName,'a',encoding='utf-8')as f:
                    f.write((' ').join(line))
                    f.write('\n')
                title = 0
            else:
                for l in line:
                    l = l.replace(' ','')
                    if(len(l)!=0):
                        with open(FileName,'a',encoding='utf-8')as f:
                            f.write(l)
                            f.write('\n')
    print('----',filename,'finish processing','----')
    count+=1
print('all the works have been Done')