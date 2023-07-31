'''
测试输入：
3
1,4,6
2,3,4,8
3,6,9
1,2
'''
N=int(input())
data=[]
for i in range(N):
    data.append(list(map(int,input().split(','))))
start,target=eval(input())

# 邻接矩阵
rooms=[[0 for i in range(N)] for j in range(N)]

for i in range(N-1):
    for d in data[i]:
        for j in range(i+1,N):
            if d in data[j]:
                rooms[i][j]=1
print(rooms)

# 递归函数
def move(room)->int:
    if room==target:
        # 结束
        return 0
    c=[1000 for i in range(N)]
    # 选择
    for i in range(N):
        if rooms[room][i]:
            c[i]=move(i)+1
    r=min(c)
    if r!=1000:
        return r
    return -1
print(move(start))
