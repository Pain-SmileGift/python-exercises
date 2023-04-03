class Maze():
    def __init__(self):
        self.map=[
            [1,1,1,1,1,1,1,1,1,1],
            [1,0,1,0,0,1,0,1,0,1],
            [1,0,0,1,0,1,0,1,0,1],
            [1,1,0,1,0,1,0,0,0,1],
            [1,1,0,0,0,0,1,1,0,1],
            [1,0,1,1,1,0,1,1,0,1],
            [1,0,1,0,0,0,1,0,0,1],
            [1,0,1,0,1,1,1,0,1,1],
            [1,0,0,0,0,0,0,0,1,1],
            [1,1,1,1,1,1,1,1,1,1]
            ]
        # 记录哪些位置走过
        self.trace=[[False for h in w] for w in self.map]
        # 起点
        self.start=(1,1)
        # 终点
        self.end=(1,8)
        # 记录走法
        self.ans=[[self.start[0],self.start[1]]]
        
    def moveTo(self, x,y):
        self.trace[x][y]=True
        self.ans.append([x,y])
        
    def move(self,x,y):
        #print(x,y, self.map[x][y])
        # 终点
        if (x,y)==self.end:
            print("走法：",self.ans)
            return
        # up
        if self.map[x-1][y]==0 and self.trace[x-1][y]==False:
            self.moveTo(x-1,y)
            return self.move(x-1,y)
        # down
        elif self.map[x+1][y]==0 and self.trace[x+1][y]==False:
            self.moveTo(x+1,y)
            return self.move(x+1,y)
        # left
        elif self.map[x][y-1]==0 and self.trace[x][y-1]==False:
            self.moveTo(x,y-1)
            return self.move(x,y-1)
        # right
        elif self.map[x][y+1]==0 and self.trace[x][y+1]==False:
            self.moveTo(x,y+1)
            return self.move(x,y+1)
        # 死路
        else:
            self.ans.pop()
            return self.move(self.ans[-1][0],self.ans[-1][1])

m=Maze()
m.move(m.start[0],m.start[1])
    
