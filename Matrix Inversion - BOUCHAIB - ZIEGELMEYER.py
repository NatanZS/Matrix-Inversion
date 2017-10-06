############ MAP #################
a=([["Houston","nous","avons"],["un","probleme","!"]])
val=[]
print("Matrix before Map Reduce : %s"%a)

for i in range(0,len(a)):
    for j in range(0,len(a[0])):
        key = j #The key is corresponding to the line number
        value = "%d,%s"%(i, a[i][j])#The value corresponds to the columns of the data and its string value
        val.append("%d,%s" % (key,value)) #Then we add the (key,value) to the list val

############ REDUCE #################
liste=[]

myArray=[[i*j for j in range(2)] for i in range(3)]
liste=sorted(val) #We sort the list val in order to start from the first column. The sorted is stores into the list "liste"

for i in range(0,len(liste)):
    ligne,colonne,nom = liste[i].split(",")# we split the value list in order to split the key (line), columns and value
    myArray[int(ligne)][int(colonne)]=nom#We store the data in myArray according to the line and column predefined
print("Matrix after Map Reduce : %s"%myArray) # display the final result