s = input()

Word = s.split()

TypeM = ["lios","etr","initis"]
TypeN = ["liala","etra","inites"]
Type =["A","N","V"]
TypeUse = []

#Chon Gioi Tinh
kt = False
for i in range(0,len(TypeM)):
    if (Word[0].endswith(TypeM[i]) ==True):
        TypeUse = TypeM
        #print("Nam")
        kt = True
        break

for i in range(0,len(TypeN)):
     if (Word[0].endswith(TypeN[i]) == True):
        TypeUse = TypeN
        #print("Nu")
        kt = True
        break
  
if (kt == False):
    print("NO")
    exit(0)

if (kt ==True and len(Word)==1):
    print("YES")
    exit(0)

#Xuly 
result = ""
for i in range(0,len(Word)):
    kt = False
    for j in range(0,len(TypeUse)):
        if (Word[i].endswith(TypeUse[j]) == True):
            result = result + Type[j]
            kt = True
    if (kt == False):
        print("NO")
        exit(0)

#in ket qua
#print(result)
count = 0
vt = 0
for i in range(0,len(result)):
    if (result[i] == "N"):
        vt = i
        count = count + 1 

if (count != 1):
    print("NO")
    exit(0)

for i in range(0,len(result)):
    if (result[i] == "A" and i > vt) or (result[i] == "V" and i < vt ):
        print("NO")
        exit(0)

print("YES")





