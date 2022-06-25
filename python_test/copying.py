#! /usr/bin/python3

import os 
import sys

comm = sys.argv
print(comm)

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
    
else :
    file_name=comm[-2]
    des_path=""

print(des_path)

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
    
    if cleaned_details[y][8]!=filen[-1]:
        del cleaned_details[y]
        offset =offset+1

print(cleaned_details)
os.system("cp "+comm[-2]+" "+comm[-1])

