###================truncate=================
## resize file to the given no. of bytes

file=open("truncate.txt","a")
file.truncate(306)
file.close
# file=open("truncate.txt","a")
# print(file.read())
# print(file.readable())