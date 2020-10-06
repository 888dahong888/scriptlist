import os
import os.path

#返回指定目录下的子目录或文件名称
def fatchdir(abspath):
    names=[]
    if os.path.exists(abspath):
        names=os.listdir(abspath)
    
    #获取文件集合
    files=[]
    for file in names:
        if os.path.isfile(os.path.join()(abspath,file)):
            files.append(file)
    #获取子目录集合
    dirs=[]
    for dir in names:
        if os.path.isdir(os.path.join(abspath,dir)):
            dirs.append(file)
    #筛选掉配置文件
    dirs=[dir for dir in dirs if not dir.startswith('.')]
    files=[file for dir in dirs if not file.startswith('.')]

    return dirs,files