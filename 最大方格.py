import random as rd

W,H=10,8
L=[]
for i in range(H):
    lr=[]
    for j in range(W):
        lr.append(rd.randint(0,1))
        print(lr[j], end=" ")
    L.append(lr)
    print()
print("==========")

# 分解因数
def fj(num):
    r=[]
    for i in range(1,num+1):
        if num%i==0:
            r.append([i,num//i])
    return r

# 判断大小
def isBigger(list_wh):
    if list_wh[0]>W:
        return False
    if list_wh[1]>H:
        return False
    return True
    

for s in range(W*H,0,-1):
    ys=fj(s)
    for wh in ys:
        if not isBigger(wh):
            continue
        
        for h in range(0,H-wh[1]+1):
            for w in range(0,W-wh[0]+1):
                # 可能结果的左上方格索引：L[h,w]
                # 当前假设最大为宽：wh[0]，高：wh[1]，共wh[0]*wh[1]个
                #print("因式：",wh,"左上：",h,w)
                size=wh[0]*wh[1]
                for i in range(size):
                    # 有一个格子不为0
                    print("i=",i,"id=",h+i//wh[0],w+i%wh[0],"v=",L[h+i//wh[0]][w+i%wh[0]])
                    if L[h+i//wh[0]][w+i%wh[0]] != 0:
                        break
                else:
                    print("存在",size,"大小",wh,"的方格，左上索引：",h,w)
                    exit(0)
                    pass
