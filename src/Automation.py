import PIL.Image
import os
import time
import win32api
import win32con
import PIL.ImageOps
import datetime
import winsound
import keyboard
from random import *
from numpy import *
from PIL import *
from PIL import ImageGrab, ImageOps
from pynput.keyboard import Key, Controller






def ready():
    while trainColorGrab((110,381,1010,419)) in range(35064,37064):
        time.sleep(1)

    for i in range(3):
        winsound.Beep(600,200)
        time.sleep(1)

def 별난보석(x):
    if keyboard.is_pressed('l') == True:
        print("Time")
        print("Time")
        print("Time")
        print("Time")
        time.sleep(10)
    screen=ImageGrab.grab()
    while screen.getpixel((1536,981))[0]==0:
        time.sleep(1)
        screen=ImageGrab.grab()
    print (screen.getpixel((1536,981))[0])
    # print(answer)
    # time.sleep(3)
    gemType=["W","Y","R","G","B","P"]

    # White=3708
    # Yellow=3822
    # Red=970
    # Green=3009
    # Blue=5284
    # Purple=1860

    White=169
    Yellow=180
    Red=87
    Green=7
    Blue=112
    Purple=219
    # (169, 170, 169)
    # (180, 40, 10)
    # (87, 137, 134)
    # (7, 159, 156)
    # (112, 18, 121)
    # (219, 210, 184)



    Row1=[]
    Row2=[]
    Row3=[]
    Row4=[]
    Row5=[]
    Row6=[]
    Row7=[]
    Row8=[]
    screen=ImageGrab.grab()
    if x==1:
        if screen.getpixel((1677,716))[0]!=0:
            randNumber=randint(1,10)
            if randNumber==1:
                NleftClick(1449,820,0.1)
            elif randNumber==2:
                NleftClick(1524,820,0.1)
            elif randNumber==3:
                NleftClick(1594,820,0.1)
            elif randNumber==4:
                NleftClick(1658,820,0.1)
            elif randNumber==5:
                NleftClick(1732,820,0.1)
            elif randNumber==6:
                NleftClick(1449,886,0.1)
            elif randNumber==7:
                NleftClick(1524,886,0.1)
            elif randNumber==8:
                NleftClick(1594,886,0.1)
            elif randNumber==9:
                NleftClick(1658,886,0.1)
            elif randNumber==10:
                NleftClick(1732,886,0.1)
            #NleftClick(1726,886,0.3)


    for j in range(8):
        for i in range(8):
            # answer=trainColorGrab((1335+(72*i),135+(72*j),1341+(72*i),140+(72*j)))
            answer=screen.getpixel((1339+(72*i),134+(72*j)))[0]

            if answer==White:
                gem="W"
            elif answer==Yellow:
                gem="Y"
            elif answer==Red:
                gem="R"
            elif answer==Green:
                gem="G"
            elif answer==Blue:
                gem="B"
            elif answer==Purple:
                gem="P"
            else:
                gem="Blank"

            if j==0:
                Row1.append(gem)
            elif j==1:
                Row2.append(gem)
            elif j==2:
                Row3.append(gem)
            elif j==3:
                Row4.append(gem)
            elif j==4:
                Row5.append(gem)
            elif j==5:
                Row6.append(gem)
            elif j==6:
                Row7.append(gem)
            elif j==7:
                Row8.append(gem)
    count=0
    maxcount=1
    board=[]
    board.append(Row1)
    board.append(Row2)
    board.append(Row3)
    board.append(Row4)
    board.append(Row5)
    board.append(Row6)
    board.append(Row7)
    board.append(Row8)
    for i in range(8):
        print(board[i])
    # 세로
    if count<=maxcount:
        for j in range(8):
            for i in range(5):
                if board[j][i]!="Blank":
                    if board[j][i]==board[j][i+1]==board[j][i+3]:
                        ClickCord(j,i+2)
                        ClickCord(j,i+3)
                        board[j][i]="Blank"
                        board[j][i+1]="Blank"
                        board[j][i+3]="Blank"
                        count+=1
                    if board[j][i]==board[j][i+2]==board[j][i+3]:
                        ClickCord(j,i)
                        ClickCord(j,i+1)
                        board[j][i]="Blank"
                        board[j][i+2]="Blank"
                        board[j][i+3]="Blank"
                        count+=1
    # 가로
    if count<=maxcount:
        for j in range(5):
            for i in range(8):
                if board[j][i]!="Blank":
                    if board[j][i]==board[j+1][i]==board[j+3][i]:
                        ClickCord(j+2,i)
                        ClickCord(j+3,i)
                        board[j][i]="Blank"
                        board[j+1][i]="Blank"
                        board[j+3][i]="Blank"
                        count+=1
                    if board[j][i]==board[j+2][i]==board[j+3][i]:
                        ClickCord(j,i)
                        ClickCord(j+1,i)
                        board[j][i]="Blank"
                        board[j+2][i]="Blank"
                        board[j+3][i]="Blank"
                        count+=1
    #가로 ㅇ ㅇ 위아래
    if count<=maxcount:
        for j in range(1,7):
            for i in range(6):
                if board[j][i]!="Blank":
                    if board[j][i]==board[j][i+2]==board[j-1][i+1]:
                        ClickCord(j,i+1)
                        ClickCord(j-1,i+1)
                        board[j][i]="Blank"
                        board[j][i+2]="Blank"
                        board[j+1][i+1]="Blank"
                        count+=1
                    if board[j][i]==board[j][i+2]==board[j+1][i+1]:
                        ClickCord(j,i+1)
                        ClickCord(j+1,i+1)
                        board[j][i]="Blank"
                        board[j][i+2]="Blank"
                        board[j+1][i+1]="Blank"
                        count+=1
    #세로 ㅇ ㅇ 왼오른
    if count<=maxcount:
        for j in range(6):
            for i in range(1,7):
                if board[j][i]!="Blank":
                    if board[j][i]==board[j+2][i]==board[j+1][i-1]:
                        ClickCord(j+1,i)
                        ClickCord(j+1,i-1)
                        board[j][i]="Blank"
                        board[j+2][i]="Blank"
                        board[j+1][i-1]="Blank"
                        count+=1
                    if board[j][i]==board[j+2][i]==board[j+1][i+1]:
                        ClickCord(j+1,i)
                        ClickCord(j+1,i+1)
                        board[j][i]="Blank"
                        board[j+2][i]="Blank"
                        board[j+1][i+1]="Blank"
                        count+=1

    #가로 xㅇㅇ 아래
    if count<=maxcount:
        for j in range(0,7):
            for i in range(0,6):
                if board[j][i]!="Blank":
                    if board[j+1][i]==board[j][i+1]==board[j][i+2]:
                        ClickCord(j+1,i)
                        ClickCord(j,i)
                        board[j+1][i]="Blank"
                        board[j][i+1]="Blank"
                        board[j][i+2]="Blank"
                        count+=1

    #가로 xㅇㅇ 위
    if count<=maxcount:
        for j in range(1,8):
            for i in range(0,6):
                if board[j][i]!="Blank":
                    if board[j-1][i]==board[j][i+1]==board[j][i+2]:
                        ClickCord(j-1,i)
                        ClickCord(j,i)
                        board[j-1][i]="Blank"
                        board[j][i+1]="Blank"
                        board[j][i+2]="Blank"
                        count+=1

    #가로 ㅇㅇx 아래
    if count<=maxcount:
        for j in range(0,7):
            for i in range(0,6):
                if board[j][i]!="Blank":
                    if board[j][i]==board[j][i+1]==board[j+1][i+2]:
                        ClickCord(j+1,i+2)
                        ClickCord(j,i+2)
                        board[j][i]="Blank"
                        board[j][i+1]="Blank"
                        board[j+1][i+2]="Blank"
                        count+=1

    #가로 ㅇㅇx 위
    if count<=maxcount:
        for j in range(1,8):
            for i in range(0,6):
                if board[j][i]!="Blank":
                    if board[j][i]==board[j][i+1]==board[j-1][i+2]:
                        ClickCord(j-1,i+2)
                        ClickCord(j,i+2)
                        board[j][i]="Blank"
                        board[j][i+1]="Blank"
                        board[j-1][i+2]="Blank"
                        count+=1


    # 세로
    # X
    #  O
    #  O
    if count<=maxcount:
        for j in range(0,6):
            for i in range(0,7):
                if board[j][i]!="Blank":
                    if board[j][i]==board[j+1][i+1]==board[j+2][i+1]:
                        ClickCord(j,i)
                        ClickCord(j,i+1)
                        board[j][i]="Blank"
                        board[j+1][i+1]="Blank"
                        board[j+2][i+1]="Blank"
                        count+=1

    # 세로
    #   X
    #  O
    #  O
    if count<=maxcount:
        for j in range(0,6):
            for i in range(0,7):
                if board[j][i]!="Blank":
                    if board[j][i+1]==board[j+1][i]==board[j+2][i]:
                        ClickCord(j,i+1)
                        ClickCord(j,i)
                        board[j][i+1]="Blank"
                        board[j+1][i]="Blank"
                        board[j+2][i]="Blank"
                        count+=1

    # 세로
    #  O
    #  O
    # X
    if count<=maxcount:
        for j in range(0,6):
            for i in range(0,7):
                if board[j][i]!="Blank":
                    if board[j][i+1]==board[j+1][i+1]==board[j+2][i]:
                        ClickCord(j+2,i)
                        ClickCord(j+2,i+1)
                        board[j][i]="Blank"
                        board[j+1][i+1]="Blank"
                        board[j+2][i]="Blank"
                        count+=1

    # 세로
    #  O
    #  O
    #   X
    if count<=maxcount:
        for j in range(0,6):
            for i in range(0,7):
                if board[j][i]!="Blank":
                    if board[j][i]==board[j+1][i]==board[j+2][i+1]:
                        ClickCord(j+2,i+1)
                        ClickCord(j+2,i)
                        board[j][i]="Blank"
                        board[j+1][i]="Blank"
                        board[j+2][i+1]="Blank"
                        count+=1


def ClickCord(y,x):
    NleftClick(1341+(72*x),135+(72*y),0.01)








def test():
    start=(513,669)
    end=(1000,1200)
    screen=ImageGrab.grab()
    rgb=screen.getpixel((1339,134)) #해골
    print(rgb)
    rgb=screen.getpixel((1339+72+72,134)) #방패
    print(rgb)
    rgb=screen.getpixel((1339+72+72+72,134)) #얼음
    print(rgb)
    rgb=screen.getpixel((1339+72+72+72+72,134)) #프로토스
    print(rgb)
    rgb=screen.getpixel((1339+72+72,134+72)) #저그
    print(rgb)
    rgb=screen.getpixel((1339+72+72+72,134+72+72)) #가스
    print(rgb[0])

    # (169, 170, 169)
    # (180, 40, 10)
    # (87, 137, 134)
    # (7, 159, 156)
    # (112, 18, 121)
    # (219, 210, 184)
######################################################################################


def 대기x시(x): #0~23
    now=time.gmtime(time.time())
    while ((now.tm_hour+9)%24)!=x:
        print ((now.tm_hour+9)%24)
        time.sleep(1)
        now=time.gmtime(time.time())
    print("It is TIME")
    time.sleep(1)



def mousePos(cord):
    win32api.SetCursorPos( (cord[0], cord[1] ))


def NleftClick(x,y,a):
    leftClick((x,y))
    time.sleep(a)

def leftClick(cord):
    win32api.SetCursorPos( (cord[0], cord[1] ))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #print ("Click")

def NrightClick(x,y,a):
    rightClick((x,y))
    time.sleep(a)

def rightClick(cord):
    win32api.SetCursorPos( (cord[0], cord[1] ))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    #print ("Click")

def trainGrab(cords):
    box = (cords)
    im = ImageOps.grayscale(ImageGrab.grab(bbox=None,include_layered_windows=False, all_screens=True))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im=ImageGrab.grab(box)
    return im


def trainColorGrab(cords):
    box = (cords)
    #print (box)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    return a

def 화면전환():
    keyboard.press('Alt')
    time.sleep(0.1)
    keyboard.press_and_release('Tab')
    time.sleep(0.1)
    keyboard.release('Alt')

def 좌표구하기(x):
    time.sleep(3)
    for i in range(x):
        get_realcords()
        winsound.Beep(600,200)
        time.sleep(2)

def get_realcords():
    x,y = win32api.GetCursorPos()
    print (x,y)
    return (x,y)

def get_ColorGrab():
    time.sleep(3)
    a= get_realcords()[0]
    b= get_realcords()[1]
    winsound.Beep(600,200)
    time.sleep(3)
    c= get_realcords()[0]
    d= get_realcords()[1]
    winsound.Beep(600,200)
    print ("trainColorGrab((" + str(a) + "," + str(b) + "," + str(c) + "," + str(d) + "))"   )
    return trainGrab((a,b,c,d))


while True:
    별난보석(1)