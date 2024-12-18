import math
A=[[2,-2],[3,-5]]
B=[[-2,0],[0,2]]
C=[[-1,2,0],[2,0,3]]
E=[[2,-1],[math.pi,math.log(2,10)],[-2,3]]
F=[[1,2,3],[2,3,4],[3,5,7]]
I=[[1,0,0],[0,1,0],[0,0,1]]
X=[[1,2],[3,4]]

def Transpose(A):#轉置矩陣
    S=list(list(0 for i in range(len(A))) for i in range(len(A[0])))#建立一個合適大小的矩陣
    for i in range(0,len(A[0])):
        for j in range(0,len(A)):
            S[i][j]=A[j][i]
    return S

def Addition(A,B):#矩陣加法
    if (len(A)==len(B)):#判斷主元素數量是否相等
        if(len(A[0])==len(B[0])):#判斷次層元素數量是否相等
            S=list(list(0 for j in range(len(A[0]))) for i in range(len(A)))#將S的尺寸設為A的尺寸
            for i in range(0,len(A)):
                for j in range(0,len(A[0])):
                    S[i][j]=A[i][j]+B[i][j]
            return S
        else:
            return 'error-differant size(in)'#回傳錯誤訊息，兩者尺寸不同
    else:
        return "error-differant size(out)"#回傳錯誤訊息，兩者尺寸不同

def Subtraction(A,B):#矩陣減法
    if (len(A)==len(B)):
        if(len(A[0])==len(B[0])):
            S=list(list(0 for j in range(len(A[0]))) for i in range(len(A)))#將S的尺寸設為A的尺寸
            for i in range(0,len(A)):
                for j in range(0,len(A[0])):
                    M=list(list(0 for j in range(len(B[0]))) for i in range(len(B)))#將S的尺寸設為A的尺寸
                    M[i][j]=-B[i][j]
                    S[i][j]=A[i][j]+M[i][j]
            return S
        else:
            return "error-differant size(in)"#回傳錯誤訊息，兩者尺寸不同
    else:
        return 'error-differant size(out)'#回傳錯誤訊息，兩者尺寸不同
    

def int_multiplication(A,B):#整數乘以矩陣(A須為整數)
    import copy
    S=copy.deepcopy(B)
    '''
    Line 47、48 深度拷貝，以免資料被刪掉
    '''
    for i in range(0,len(B),1):
        for j in range(0,len(B),1):
                S[i][j]=A*B[i][j]
    return S

def matrix_multiplication(A,B):#矩陣乘以矩陣
    if len(A[0])==len(B):#確認兩者尺寸是否相同
        S=list(list(0 for i in range(len(B[0]))) for i in range(len(A)))
        for i in range(0,len(A)):
            for j in range(0,len(B[0])):
                for k in range(0,len(B)):
                    S[i][j]+=A[i][k]*B[k][j]#把算出來的結果累加進矩陣之中
        return S
    else:
        return'error-this row with that column are differant size'#回傳錯誤訊息，兩者尺寸不同

def inverse_multiplication(A):
    if (len(A)!=len(A[0])):
        return'error-The inverse matrix does not exist(this column and this row are differant size)'#沒有反矩陣(行與列的大小不同)
    else:
        if(det(A)==0):
            return'error-The inverse matrix does not exist(det==0)'#沒有反矩陣(det==0)
        elif(len(A)==1):
            S=A
        elif(len(A)==2):#特例:size==2
            Base=det(A)
            P=[[A[1][1],-A[0][1]],[-A[1][0],A[0][0]]]
            S=int_multiplication(Base**-1,P)
        else:
            Base=det(A)
            S=list(list(0 for i in range(0,len(A))) for j in range(0,len(A)))
            Q=list(list(0 for i in range(len(A))) for j in range(len(A)))
            for i in range(0,len(A)):
                for j in range(0,len(A)):
                     Q[j][i]=delate_pop_C(delate_pop_R(A,i),j)#回傳值為一個(n-1)X(n-1)的矩陣(其最後一個位置的未知數表述式為Q[n][n][n-1][n-1])
                     Q[j][i]=det(Q[j][i])#將Q[j][i]內部的矩陣用行列式算法換成數值
            S=int_multiplication(Base**-1,Q)
            S=PN(S)
            S=check(S)
        return S
            
def check(A):#防止出現-0.0
    for i in range(len(A)):
        for j in range(len(A)):
            if(A[i][j]==0)or(A[i][j]==-0):
                A[i][j]=abs(A[i][j])
    return A
            
def det(A):#運算行列式
    S=0
    if(len(A)==1):#特例：1X1矩陣
        S=A[0][0] 
    elif(len(A)==2):#特例：2X2矩陣
        S=A[0][0]*A[1][1]-A[0][1]*A[1][0]  
    else:
        for x in range(0,len(A),1):#偏移迴圈(Shift)
            EP=1#正半週
            ED=1#負半週
            for y in range(0,len(A),1):#主迴圈
                EP*=A[(y+x)%len(A)][y]
                ED*=A[(len(A)-y+x)%len(A)][y]
            S+=EP
            S-=ED
    return S

def PN(A):#正負變號的工具
    for x in range(0,len(A)):
        for y in range(0,len(A)):
            if ((x+y)%2 != 0)and(A[x][y]!=0):
                A[x][y]=-A[x][y]
    return A

def delate_pop_C(A,y):#delate a column
    R=list((i*1) for i in A)
    for j in range(0, len(A)):
       R[j].pop(y)
    return R

def delate_pop_R(A,x):#delate a row
    R=list((i*1) for i in A)
    R.pop(x)
    return R

def diagonal_matrix(A):
    if(len(A)==len(A[0])):
        flag=1#旗標，預設值為1，當結果不符合定義時就會變0，輸出false，反之當結果符合定義時會維持1，並輸出true
        for i in range(len(A)):
            for j in range(len(A)):
                if (i==j):
                    if(A[i][j]!=0):
                        flag*=1
                    else:
                        flag*=0
                else:
                    if(A[i][j]!=0):
                        flag*=0
                    else:
                        flag*=1
        if(flag==1):
            return'true'
        else:
            return'false'
            
    else:
        return'error-this row and this column are differant size'#回傳錯誤訊息，行與列尺寸不同無法比較

def symmetric_matrix(A):
    if(len(A)!=len(A[0])):
        return'error-this row and this column are differant size'#回傳錯誤訊息，行與列尺寸不同無法比較
    else:
        Flag=1#旗標，預設值為1，當結果不符合定義時就會變0，輸出false，反之當結果符合定義時會維持1，並輸出true
        for i in range(len(A)):
            for j in range(len(A)):
                if(A[i][j]==A[j][i]):
                    Flag*=1
                else:
                    Flag*=0#當結果不符合定義時就會變0
        if(Flag==1):
            return'true'
        else:
            return'false'
            
def equal(A,B):
    if(A==B):
        return 'true'
    else:
        return'false'
    
a1=Addition(A,int_multiplication(3,B))
a2=Subtraction(C,matrix_multiplication(B,Transpose(E)))
a3=Transpose(A)
M=matrix_multiplication(A,B)
N=matrix_multiplication(B,A)
b=equal(M,N)
P=matrix_multiplication(Transpose(C),Transpose(B))
Q=Transpose(matrix_multiplication(B,C))
c=equal(P,Q)
d1=inverse_multiplication(A)
d2=inverse_multiplication(F)
e1=diagonal_matrix(A)
e2=diagonal_matrix(B)
e3=diagonal_matrix(F)
e4=diagonal_matrix(I)
f1=symmetric_matrix(A)
f2=symmetric_matrix(B)
f3=symmetric_matrix(F)
f4=symmetric_matrix(I)

'''
Line 179~197 題目的測試資料
'''
print(inverse_multiplication(X))
print('(a)\na1=%s\na2=%s\na3=%s' %(a1,a2,a3))
print('(b)※答案為true時，答案相同，答案為false時，答案相異\n%s' %b)
print('(c)※答案為true時，答案相同，答案為false時，答案相異\n%s' %c)
print('(d)※答案為error-The inverse matrix does not exist時，代表反矩陣不存在\nA=%s\nF=%s' %(d1,d2))
print('(e)※答案為true時，符合條件，答案為false時，不符合條件\nA=%s\nB=%s\nF=%s\nI=%s' %(e1,e2,e3,e4))
print('(f)※答案為true時，符合條件，答案為false時，不符合條件\nA=%s\nB=%s\nF=%s\nI=%s' %(f1,f2,f3,f4))