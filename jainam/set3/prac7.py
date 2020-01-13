def pascal(n):
    mat=[]
    for i in range(0,n):
        row=[]
        for j in range(0,i+1):
            if j==0 or j==i:
                row.append(1)
            else:
                row.append(mat[i-1][j-1] + mat[i-1][j])
        mat.append(row)
    for i in mat:
        for j in range(n,len(i),-1):
            print(" ", end="")
        for j in i:
            print(j, end=" ")
        print()    
n = int(input("Enter rows: "))
pascal(n)