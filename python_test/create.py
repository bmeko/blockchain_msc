#! /usr/bin/python3
from asyncore import read
import os 
import sys

from matplotlib.cbook import index_of
#import inter  
filen= sys.argv

os.system("touch " + filen[-1])
file_name=""
des_path=""
check=False
for x in filen[-1]:
    if x == "/":
        check=True
        break
if check==True:
    other_path =filen[-1].split("/")
    file_name=other_path[-1]
    del other_path[-1]
    print(file_name)
    des_path="/"
    des_path=des_path.join(other_path)
    print(des_path)
else :
    file_name=filen[-1]
    des_path=""
#detail
detail=str(os.popen("ls "+ des_path + " -la |grep " +file_name).read()).split()
cleaned_details=[]

#clean the details
new=[]
for i in detail:
    new.append(i)
    if len(new)%9==0:
        cleaned_details.append(new)
        new=[]

offset=0
for x in range(1,len(cleaned_details)+1):
    y=x*-1+offset
    
    if cleaned_details[y][8]!=filen[-1]:
        del cleaned_details[y]
        offset =offset+1
#path 
if check==False:
    path_arr=(os.popen("ls -d $PWD/* |grep " +file_name).read()).split()
    #clean the path
    offset=0
    for i in range (1,len(path_arr)+1):
        y=i*-1+offset
        x= path_arr[y].split("/")
        
        if x[-1]!=filen[-1]:
            del path_arr[y]
            offset=offset+1
    path=path_arr[0]
else:
    path=des_path+"/"+file_name
print(path)
#inter.create()DD