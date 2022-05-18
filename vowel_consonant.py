f=open("vowel_consonant.txt")
f1=f.read()
f2=f1.split()
i=0
vowel=0
consonant=0
while i<len(f2):
    j=0
    while j<len(f2[i]):
        if f2[i][j]=="a" or "e" or "i" or "o" or "u":
            vowel+=1
        else:
            consonant+=1
        j+=1
    i+=1
print(vowel)
print(consonant)

# f=open("vowel_consonant.txt","r")
# a=f.read()
# print(a)
# upper=0
# lower=0
# vowel=0
# consonant=0
# i=0
# while i<len(a):
#     if a[i]. isupper():
#         upper+=1
#     if a[i]. islower():
#         lower+=1
#     if a[i] in ("a","e","i","o","u","A","E","I","O","U"):
#         vowel+=1
#     else:
#         consonant+=1
#     i+=1
# print(upper)
# print(lower)
# print(vowel)
# print(consonant)