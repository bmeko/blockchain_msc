#! /usr/bin/python3

import os 
import sys
import inter

comm = sys.argv
print(comm)
check=False
for x in comm[-2]:
    if x == "/":
        check=True
        break

if check==True:
    other_path =comm[-2].split("/")
    file_name=other_path[-1]
    del other_path[-1]
    
    des_path="/"
    des_path=des_path.join(other_path)
    path=des_path
    
else :
    file_name=comm[-2]
    des_path=""
    path_arr=(os.popen("ls -d $PWD/* |grep " +file_name).read()).split()
    print(path_arr)
    offset=0
    for i in range (1,len(path_arr)+1):
        y=i*-1+offset
        x= path_arr[y].split("/")
        print(x)
        if x[-1]!=comm[-2]:
            del path_arr[y]
            offset=offset+1
    path=path_arr



#details
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
    if cleaned_details[y][8]!=file_name:
        del cleaned_details[y]
        offset =offset+1
upda="/".join(cleaned_details[0][5:8])
print(cleaned_details)
resul=inter.check(upda, cleaned_details[0][-1],path,cleaned_details[0][4])
os.system("cp "+comm[-2]+" "+comm[-1])
