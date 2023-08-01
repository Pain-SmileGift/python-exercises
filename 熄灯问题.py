"""
输入灯的第1组测试数据
0 1 1 0 1 0
1 0 0 1 1 1
0 0 1 0 0 1
1 0 0 1 0 1
0 1 1 1 0 0
 
输出按灯的方案
 1 0 1 0 0 1
 1 1 0 1 0 1
 0 0 1 0 1 1
 1 0 0 1 0 0
 0 1 0 0 0 0
 
输入灯的第2组测试数据
0 0 1 0 1 0
1 0 1 0 1 1
0 0 1 0 1 1
1 0 1 1 0 0
0 1 0 1 0 0
 
输出按灯的方案：
 1 0 0 1 1 1
 1 1 0 0 0 0
 0 0 0 1 0 0
 1 1 0 1 0 1
 1 0 1 1 0 1
"""


Lights=[[0,0,1,0,1,0],
        [1,0,1,0,1,1],
        [0,0,1,0,1,1],
        [1,0,1,1,0,0],
        [0,1,0,1,0,0]
        ]
b=[[0 for c in range(8)] for r in range(6)]

def bin_to_press(num):
    for i in range(6):
        for j in range(8):
            b[i][j]=0
            
    for i in range(1,7):
        b[1][7-i]=num%2
        num//=2
    

def guess():
    for i in range(1,5):
        for j in range(1,7):
            b[i+1][j]=(Lights[i-1][j-1]+b[i][j]+b[i][j-1]+b[i][j+1]+b[i-1][j]+b[i+1][j])%2
    for c in range(6):
        if (Lights[4][c]+b[4+1][c+1]+b[4+1][c]+b[4+1][c+2]+b[4][c+1])%2==1:
            return False
    return True
    
def show():
    print("按钮：")
    for i in range(1,6):
        for j in range(1,7):
            print(b[i][j],end=" ")
        print()
    print("灯：")
    for i in range(0,5):
        for j in range(0,6):
            print(Lights[i][j],end=" ")
        print()
    print('-------------')


n=0
while n<64:
    bin_to_press(n)
    if(guess()):
        print("ans:",n)
        show()
    n=n+1

