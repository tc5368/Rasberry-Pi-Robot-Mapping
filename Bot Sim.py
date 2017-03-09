xHeight = 0
yHeight = 0

Wall = chr(9608)
import random

class robotSim():
    def __init__(self,startx,starty):
        self.curx = startx
        self.cury = starty

class board():
    def __init__(self,xsize,ysize):
        self.grid = []
        self.ysize = ysize
        self.xsize = xsize
        for iy in range(ysize):
            self.grid.append([])
            for ix in range(xsize):
                self.grid[iy].append(' ')

    def display(self):
        for i in range(self.ysize):
            print(self.grid[i])

    def boardSize(self):
        return (xsize,ysize)

    def genBarrier(self):
        count = 0
        for i in range(self.xsize):
            self.grid[0][i] = Wall
            self.grid[self.ysize-1][i] = Wall
        for i in range(self.ysize):
            self.grid[i][0] = Wall
            self.grid[i][self.xsize-1] = Wall
        total = int(self.xsize * self.ysize)
        obstactleNum = random.randint(int(total/50),int(total/30))
        count = obstactleNum
        print(count)
        while count != 0:
            try:
                tempx = random.randint(0,self.xsize-1)
                tempy = random.randint(0,self.ysize-1)
                for iy in range(-1,2):
                    for ix in range(-1,2):
                        self.grid[tempy+iy][tempx+ix] = Wall
                count -= 1
            except:
                count -= 1

class robotSim():
    def __init__(self,starty,startx,symbol):
        self.currenty = starty
        self.currentx = startx
        self.symbol = symbol

        for iy in range(-1,2):
            for ix in range(-1,2):
                if room[self.currenty+iy][self.currentx+ix] == Wall:
                    room[self.currenty+iy][self.currentx+ix] = ' '

    def refresh(self):
        room[self.currenty][self.currentx] = self.symbol
        #see every iteration of Map uncomment next line
        #printRoom()
        #n = input('')

    def move(self,direction):
        tempx = self.currentx
        tempy = self.currenty
        room[self.currenty][self.currentx] = ' '
        if direction.lower() == 'u':
            if room[bot.currenty - 1][bot.currentx] != Wall:
                self.currenty -= 1
        elif direction.lower() == 'd':
            if room[bot.currenty + 1][bot.currentx] != Wall:
                self.currenty += 1
        elif direction.lower() == 'l':
            if room[bot.currenty][bot.currentx - 1] != Wall:
                self.currentx -= 1
        elif direction.lower() == 'r':
            if room[bot.currenty][bot.currentx + 1] != Wall:
                self.currentx += 1
        self.refresh()

    def senseDis(self,direction):
        xsize = xHeight
        ysize = yHeight
        if direction.lower() == 'u':
            for i in range(ysize - (ysize - self.currenty)+1):
                if room[self.currenty-i][self.currentx] == Wall:
                    return i-1
        elif direction.lower() == 'd':
            for i in range(ysize - self.currenty+1):
                if room[self.currenty+i][self.currentx] == Wall:
                    return i-1
        elif direction.lower() == 'l':
            for i in range(xsize - (xsize - self.currentx)+1):
                if room[self.currenty][self.currentx-i] == Wall:
                    return i-1
        elif direction.lower() == 'r':
            for i in range(xsize - self.currentx+1):
                if room[self.currenty][self.currentx+i] == Wall:
                    return i-1

    def startMap(self):
        Map[self.currenty][self.currentx] = self.symbol
        self.check()
        count = 1
        for i in range(100000):
            move = random.randint(0,3)
            if move == 0:
                bot.runFor()
            elif move == 1:
                bot.runBack()
            elif move == 2:
                bot.runRight()
            elif move == 3:
                bot.runLeft()

    def runFor(self):
        while True:
            if Map[self.currenty-1][self.currentx] == ' ' and Map[self.currenty-1][self.currentx] != Wall:
                #print('Clear Infront going forwards')
                self.check()
                self.move('u')
            else:
                #print('No longer clear infront')
                break

    def runRight(self):
        while True:
            if Map[self.currenty][self.currentx+1] == ' ' and Map[self.currenty][self.currentx+1] != Wall :
                #print('Clear to the right going right')
                self.check()
                self.move('r')
            else:
                #print('No longer clear to the right')
                break

    def runBack(self):
        while True:
            if Map[self.currenty+1][self.currentx] == ' ' and Map[self.currenty+1][self.currentx] != Wall:
                #print('Clear Behind going backwards')
                self.check()
                self.move('d')
            else:
                #print('No longer clear behind')
                break

    def runLeft(self):
        while True:
            if Map[self.currenty][self.currentx-1] == ' ' and Map[self.currenty][self.currentx-1] != Wall:
                #print('Clear to the left going left')
                self.check()
                self.move('l')
            else:
                #print('No longer clear to the left')
                break

    def check(self):
        tempu,tempd,templ,tempr = self.getAll()
        distances = [tempu,tempd,templ,tempr]
        Map[self.currenty-tempu][self.currentx] = Wall
        Map[self.currenty+tempd][self.currentx] = Wall
        Map[self.currenty][self.currentx+tempr] = Wall
        Map[self.currenty][self.currentx-templ] = Wall

    def getAll(self):
        u = int(self.senseDis('u'))+1
        d = int(self.senseDis('d'))+1
        l = int(self.senseDis('l'))+1
        r = int(self.senseDis('r'))+1
        return(u,d,l,r)


def main(xinput,yinput):
    global xHeight, yHeight
    xHeight = xinput
    yHeight = yinput
    generatingRoom = board(xinput,yinput)
    generatingRoom.genBarrier()
    return generatingRoom.grid

def printRoom():
    for i in range(len(room)):
	       print(room[i])

def genBlankMap():
    generatingBlankRoom = board(xHeight,yHeight)
    blank = generatingBlankRoom.grid
    return blank

def showMap():
    for i in range(yHeight):
        print(Map[i])

room = main(28,28)
bot = robotSim(14,14,'X')
bot.refresh()
Map = genBlankMap()
bot.startMap()
showMap()
print('\n','\n')
printRoom()
