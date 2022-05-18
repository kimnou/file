# with open("with.txt") as file:
#     data=file.read()
#     print(data)
    

with open("new.txt","w") as file:
    data=file.writelines(["hello world!","\n","hello python!","\n","python world!"])