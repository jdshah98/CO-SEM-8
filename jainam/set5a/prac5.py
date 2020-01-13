m1,n1 = [int(i) for i in input("Enter size of matrix1(m,n): ").split(",")]
m2,n2 = [int(i) for i in input("Enter size of matrix1(m,n): ").split(",")]
if m2!=n1:
    print("Enter Dimensions of matrix properly")
else:
    mat1 = []
    temp = [int(i) for i in input("Enter comma seperated elements of matrix1 in row order: ").split(",")]
    start,end=0,n1
    for i in range(m1):
        mat1.append(temp[start:end])
        start+=n1
        end+=n1
    mat2 = []
    temp = [int(i) for i in input("Enter comma seperated elements of matrix2 in row order: ").split(",")]
    start,end=0,n2
    for i in range(m2):
        mat2.append(temp[start:end])
        start+=n2
        end+=n2
    print(mat1)
    print(mat2)
    prod = []
    for i in range(m1):
        temp=[0]*n2
        for j in range(m2):
            for k in range(n2):
                temp[j] = temp[j] + mat1[i][k]*mat2[j][k];
        prod.append(temp)
    print(prod)