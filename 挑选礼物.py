'''
方法一：没用背包问题解法
'''
N,V=3,5
#(价格,喜爱值)
D=[(1,2),(2,4),(3,3)]
# 计算价格的所有子集
ZJ=[[]]
for i in D:
    for j in ZJ[:]:
        t=j+[i]
        ZJ.append(t)
#print(ZJ)
# 计算每个子集的总价和总喜爱值并排序
Res=[]
for i in ZJ:
    sp=0
    sl=0
    for j in i:
        sp+=j[0]
        sl+=j[1]
    if sp>V:
        continue
    Res.append((sp,sl))
Res=sorted(Res,key=lambda x:x[1])
print(Res[-1])

'''
方法二：01背包
'''
# 物品重量
w1=[2,2,6,5,4]
# 物品价值
v1=[6,3,5,4,6]
# 物品重量
w=[1,2,3]
# 物品价值
v=[2,4,3]
# 共5个物品，背包承重7
N=3
W=5
# 生成N*W二维数组
result=[[0 for j in range(1+W)] for i in range(1+N)]

for i in range(1,N+1):
    for j in range(1,W+1):
        if i==0:
            continue
        if w[i-1]>j:
            result[i][j]=result[i-1][j]
        else:
            result[i][j]=max(result[i-1][j],result[i-1][j-w[i-1]]+v[i-1])

print(result[N][W])
