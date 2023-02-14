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
