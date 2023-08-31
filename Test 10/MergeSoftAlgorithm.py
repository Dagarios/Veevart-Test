MatrizOriginal = [14,33,27,10,35,19,42,44]
MatrizA = []
MatrizB = []
Matriz1 = []
Matriz2 = []
Matriz3 = []
Matriz4 = []
MatrizFinal = [0,0,0,0]

def SortedArray():
    for i in range(4):
        MatrizA.append(MatrizOriginal[i])
        MatrizB.append(MatrizOriginal[i+4])
    print("\n-> SortedArray")
    print(MatrizA,"     ",MatrizB)

def MergeSortDivision():
    for i in range(2):
        Matriz1.append(MatrizA[i])
        Matriz2.append(MatrizA[i+2])
        Matriz3.append(MatrizB[i])
        Matriz4.append(MatrizB[i+2])
    print("\n-> MergeSortDivision")
    print(Matriz1,"     ",Matriz2,"     ",Matriz3,"     ",Matriz4)
    a1 = Matriz1[0]
    a2 = Matriz1[1]
    a3 = Matriz2[0]
    a4 = Matriz2[1]
    b1 = Matriz3[0]
    b2 = Matriz3[1]
    b3 = Matriz4[0]
    b4 = Matriz4[1]
    print("\n-> MergeSortDivision 2")
    print(a1,"  ",a2,"  " ,a3,"  " ,a4,"  " , b1,"  ", b2,"  ", b3,"  ", b4)
    return a1,a2,a3,a4,b1,b2,b3,b4

def MergeSortConbine():
    if(a1>a2):
        Matriz1[1] = a1
        Matriz1[0] = a2
    else:
        Matriz1[0] = a1
        Matriz1[1] = a2
        print(Matriz1)

    if(a3>a4):
        Matriz2[1] = a3
        Matriz2[0] = a4
    else:
        Matriz2[0] = a3
        Matriz2[1] = a4

    if(b1>b2):
        Matriz3[1] = b1
        Matriz3[0] = b2
    else:
        Matriz3[0] = b1
        Matriz3[1] = b2

    if(b3>b4):
        Matriz4[1] = b3
        Matriz4[0] = b4
    else:
        Matriz4[0] = b3
        Matriz4[1] = b4
    print("\n-> MergeSortConbine")
    print(Matriz1,"     ",Matriz2,"     ",Matriz3,"     ",Matriz4)

    if (Matriz1[0]>=Matriz2[0] & Matriz1[0]>=Matriz2[1]):
        MatrizA[0] = Matriz2[0]
        MatrizA[1] = Matriz2[1]
        MatrizA[2] = Matriz1[0]
        MatrizA[3] = Matriz1[1]
    elif(Matriz1[0]>=Matriz2[0] & Matriz1[1]<=Matriz2[1]):
        MatrizA[0] = Matriz2[0]
        MatrizA[1] = Matriz1[0]
        if(Matriz1[1]<=Matriz2[1]):
            MatrizA[2] = Matriz1[1]
            MatrizA[3] = Matriz2[1]
        else:
            MatrizA[2] = Matriz2[1]
            MatrizA[3] = Matriz1[1]
    elif(Matriz3[0]<=Matriz4[0] & Matriz3[1]<=Matriz4[1]):
        MatrizA[0] = Matriz1[0]
        MatrizA[1] = Matriz1[1]
        MatrizA[2] = Matriz2[0]
        MatrizA[3] = Matriz2[1]

    if (Matriz3[0]>=Matriz4[0] & Matriz3[1]>=Matriz4[1]):
        MatrizB[0] = Matriz4[0]
        MatrizB[1] = Matriz4[1]
        MatrizB[2] = Matriz3[0]
        MatrizB[3] = Matriz3[1]
    elif(Matriz3[0]>=Matriz4[0] & Matriz3[1]<=Matriz4[1]):
        MatrizB[0] = Matriz3[0]
        MatrizB[1] = Matriz4[0]
        if(Matriz3[1]<=Matriz4[1]):
            MatrizB[2] = Matriz3[1]
            MatrizB[3] = Matriz4[1]
        else:
            MatrizB[2] = Matriz4[1]
            MatrizB[3] = Matriz3[1]
    elif(Matriz3[0]<=Matriz4[0] & Matriz3[1]<=Matriz4[1]):
        MatrizB[0] = Matriz3[0]
        MatrizB[1] = Matriz3[1]
        MatrizB[2] = Matriz4[0]
        MatrizB[3] = Matriz4[1]

    print("\n-> MergeSortConbine 2")
    print(MatrizA,"     ",MatrizB)
    MatrizFinal[0] = MatrizA[0]
    MatrizFinal[1] = MatrizA[1]
    MatrizFinal[2] = MatrizA[2]
    MatrizFinal[3] = MatrizA[3]
    for i in range(4):
        for j in range(4):
            if (MatrizB[i] <= MatrizFinal[j]):
                MatrizFinal.insert(j, MatrizB[i])
                x = True
                break
            else:
                x = False
        if(x==False):
            MatrizFinal.append(MatrizB[i])
    print("\n-> MergeSortConbine 3")
    print(MatrizFinal)

SortedArray()
a1,a2,a3,a4,b1,b2,b3,b4 = MergeSortDivision()
MergeSortConbine()