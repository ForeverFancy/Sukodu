class sukudo(object):
    def __init__(self,list):
        self.getList_2=list
        self.count=0
        self.flag=0

    def check(self,x,y,value):                                      #检查所在行列和九宫格内有没有相同的数字

        for j in range(0,9):
            if j!=y:
                if self.getList_2[x][j] == value:
                    return False

        for i in range(0,9):
            if i!=x:
                if self.getList_2[i][y] == value:
                    return False

        row, col = int(x/3)*3, int(y/3)*3
        for i in range(row,row+3):
            for j in range(col,col+3):
                if i!=x and j!=y :
                    if self.getList_2[i][j]==value:
                        return False

        return True

    def getNext(self,x,y):

        for j in range(y+1,9):
            if self.getList_2[x][j]==0:
                return x,j

        for i in range(x+1,9):
            for j in range(0,9):
                if self.getList_2[i][j]==0:
                    return i,j
        return -1,-1

    def tryIt(self,x,y):
        if self.getList_2[x][y]==0:
            for i in range(1,10):
                if self.check(x,y,i):
                    self.getList_2[x][y]=i
                    next_x,next_y=self.getNext(x,y)
                    if next_x==-1:
                        self.count+=1
                        self.getList_2[x][y]=0
                        return False
                    else:
                        end=self.tryIt(next_x,next_y)
                        if not end:
                            self.getList_2[x][y]=0
            return False

    def start(self):
        for i in range(0,9):
            for j in range(0,9):
                if self.getList_2[i][j] ==0:
                    self.tryIt(i,j)
                    return

if __name__ =='__main__':
    List=[[7,8,9,1,2,3,4,6,5],[6,1,2,4,0,0,3,7,8],[3,4,5,8,7,6,1,9,2],[8,5,6,9,4,2,7,1,3],[2,3,1,5,6,7,8,4,9],[9,7,4,3,8,1,5,2,6],[1,6,3,7,0,0,2,8,4],[5,2,8,6,1,4,9,3,7],[4,9,7,2,3,8,6,5,1]]
    so=sukudo(List)
    so.start()