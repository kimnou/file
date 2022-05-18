# f = open("all.txt", "a")
# f.writelines(["See you soon!", "Over and out."])
# f.close()
# f = open("all.txt")
# print(f.read())


##=======using line breaks====================
f=open("all.txt", "a")
f.writelines(["\nSee you soon!", "\nOver and out."])
f.close()
f=open("all.txt")
print(f.read())