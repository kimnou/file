# f=open("read.txt","r")
# a=f.read()
# print(a)


import os
old="read.txt"
new="read1.txt"
os.rename(old,new)