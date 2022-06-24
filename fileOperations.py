from fileinput import close
import os
import time
def fileOperations(file_dir):
    for root, dirs, files in os.walk(file_dir):
        data = open('C:\/test.txt','a+')
        n = len(files)
        if n >= 1:
         file = root+'\/'+files[0]         
         mtime = os.path.getmtime(file)
         print(root,end='\t',file=data)  # 当前目录路径          
         print(time.ctime(mtime),file=data)  # 当前路径下所有非目录子文件
         data.close()
fileOperations('C:\posterCenter')