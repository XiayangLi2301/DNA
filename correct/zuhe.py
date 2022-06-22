# 二位列表初始化
c = [[0] * 11 for _ in range(11)]
c[0][0]= 1
c[1][1] = 1
for i in range(2,11):
    for j in range(1,i+1):
        c[i][j] = (i-1)*c[i-1][j]+c[i-1][j-1]

for i in range(1,11):
    print(c[10][i]) 

