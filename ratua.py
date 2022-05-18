# f=open("tell.txt","r")
# a=len(f.readlines())
# print(a)


# f=open("tell.txt","r")
# a=len(f.read().split())
# print(a)


# banks_list= ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# i=0
# f=open("file-question3.txt","w")
# while i<len(banks_list):
#     j=f.write(banks_list[i]+"\n")
#     i+=1
# f.close

f=open("file-question3.txt","r")
a=f.readlines()
print(a)
for i in a:
    c=0
    b=list(i)
    for j in b:
        if j>="a" or j<="z":
            c=c+1
        if j>="A"or j<="Z":
            c+=1
        else:
            pass
print(c)  
#    print(b)
f.close

# f=open("file-question3.txt","r")
# a=f.readlines()
# print(a)
# i=0
# while i<len(a):
#     if a[i] in "a"
#     for j in b:
#         if j>="a" or j<="z":
#             c=c+1
#         if j>="A"or j<="Z":
#             c+=1
#         else:
#             pass
# print(c)  
#    print(b)
f.close