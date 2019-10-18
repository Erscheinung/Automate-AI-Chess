from motor1 import rotatemotor as rotateY
from motor2 import rotatemotor as rotateX
from em import toggleMagnet as toggleMagnet
import time
import threading

motorcurentx = 0
motorcurenty = 0

xscale = 5
yscale = 5

half_square = 2


def moveMotor(move):
    convertMove(move)

def trackInitial(x2,y2):
	thread1=moveY(y2,0)
	thread2=moveX(x2,0)
    	thread1.start()
    	thread2.start()
    	thread1.join()
    	thread2.join()

class moveX(threading.Thread)
    x1=0
    x2=0
    def __init__(self,t1,t2):
	threading.Thread.__init__(self)
	x1=t1
	x2=t2
    def run(self):
    	dx = x2-x1
    	rotateX(dx*xscale)

class moveY(threading.Thread)
    y1=0
    y2=0
    def __init__(self,t1,t2):
	threading.Thread.__init__(self)
	    y1=t1
	    y2=t2
    def run(self):
    	dy = y2-y1
    	rotateY(-1*dy*yscale)


def moveToOldPos(x1, y1):
    thread1=moveY(0,y1)
    thread2=moveX(0,x1)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("current position "+str(x1) +" "+str(y1))
    print("picking the peice up")
    toggleMagnet(True)
    rotateX(-1*half_square)
    rotateY(1*half_square)

def moveToNewPos(x1,y1,x2,y2):
    thread1=moveY(y1,y2)
    thread2=moveX(x1,x2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("current position "+str(x2) +" "+str(y2))
    print("dropping the piece moving towards zero")
    rotateX(1*half_square)
    rotateY(-1*half_square)
    toggleMagnet(False)
    moveMotortozero(x2,y2)

def moveMotortozero(x,y):
    thread1=moveY(y,0)
    thread2=moveX(x,0)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("finally at zero")

def convertMove(move):
    print("inside the motor")
    x1 = move.oldPos[0]
    y1 = move.oldPos[1]
    x2 = move.newPos[0]
    y2 = move.newPos[1]
    x1 = abs(7-x1)
    y1 = abs(7-y1)
    x2 = abs(7-x2)
    y2 = abs(7-y2)
    print("("+str(x1)+","+str(y1)+") ("+str(x2)+","+str(y2)+")")
    print("current position 0,0")
    moveToOldPos(x1,y1)
    moveToNewPos(x1,y1,x2,y2)
