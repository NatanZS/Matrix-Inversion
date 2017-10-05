############ MAP #################
a=([["Houston","nous","avons"],["un","probleme","!"]])
val=[]
print("Matrix before Map Reduce : %s"%a)

for i in range(0,len(a)):
    for j in range(0,len(a[0])):
        key = j
        value = "%d,%s"%(i, a[i][j])
        val.append("%d,%s" % (key,value))

############ REDUCE #################
liste=[]

myArray=[[i*j for j in range(2)] for i in range(3)]
liste=sorted(val)

for i in range(0,len(liste)):
    ligne,colonne,nom = liste[i].split(",")
    myArray[int(ligne)][int(colonne)]=nom
print("Matrix after Map Reduce : %s"%myArray)