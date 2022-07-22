#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import sys
import inter

comm = sys.argv






def cleanpath(comm):
    check=False	
    for x in comm[-2]:
        if x=="/":
            check=True
            break
    if check==True:
        other_path=comm[-2].split("/")
        file_name=other_path[-1]
        del other_path[-1]
        
        des_path="/"
        des_path=des_path.join(other_path)
        path=des_path
    else:
        file_name=comm[-2]
        des_path=""
        path_arr=(os.popen("ls -d $PWD/* |grep " +file_name).read()).split()
        offset=0
        for i in range(1,len(path_arr)+1):
            y=i*-1+offset
            x=path_arr[y].split("/")
            if x[-1]!=comm[-2]:
                del path_arr[y]
                offset=offset+1
        path=path_arr
    return des_path,file_name,path



def details(des_path,file_name):
    detail=str(os.popen("ls "+des_path+" -la |grep "+file_name).read()).split()
    cleaned_details=[]
    
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
    return cleaned_details


def check_format(file,path):
    z=file.split(".")
    im_exten=["jpg","jpeg","png","jfif","pjpeg","pjp","png","wav","WAV","JPG","JPEG","PNG","JFIF","PJPEG","PJP","PNG"]
    check_list=set(im_exten)
    forma=False
    for i in z:
        if i in check_list:
            forma=True
            return forma
    #check based on the binwalk return
    binw=str(os.popen("binwalk "+path).read())
    binw=binw.split(" ")
    
    #clean the binwalk result
    new=[]
    for i in binw:
        if i!="":
            new.append(i)
    binw=new
    
    for i in binw:
        
        if i in check_list:
            forma=True
            print("got it")
            return forma
    #check based on hexdump return

    hexdum=str(os.popen("hexdump -C "+path+" |head").read())
    hexdum=hexdum.split(" ")
    hexval=["FFD8FFE1","ffd8ffe1","FFD8FFE0","ffd8ffe0","89504e47","89504E47","52494646"]
    check_val=set(hexval)
    new=[]
    for i in hexdum[1:6]:
        
        if len(i)<=3 and len(i)>0:
            new.append(i)
    hexdum="".join(new)   
    if hexdum in check_val:
        print("image")
        return True
    
    return forma    

if len(comm)>=3:
    des_path,filename,path=cleanpath(comm)
    if check_format(comm[-2],path[0]):
        
        cleaned_details=details(des_path,filename)
        upda="/".join(cleaned_details[0][5:8])
        
        resul=inter.check(upda, cleaned_details[0][-1],path[0],cleaned_details[0][4])
        if resul:
            os.system("cp "+comm[-2]+" "+comm[-1])
        
            
    else:
        os.system("cp "+comm[-2]+" "+comm[-1])
else:
    print("command is not corrent")