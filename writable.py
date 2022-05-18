## a file is writable if it is opened using "a" or "w" modedetach()	 

#=============not writable, returns False===========
# file=open("all.txt")
# print(file.writable())


#=============writable, returns True=================
# file=open("all.txt","a")
file=open("all.txt","w")
print(file.writable())