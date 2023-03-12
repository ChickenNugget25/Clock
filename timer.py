import pygame

import datetime as dt

with open('Data/reds.txt','r+') as f:
    lines=f.readlines()
    lines= [lines[i][:-1] for i in range(len(lines)-1)]

reds = []

for i in lines:
    reds.append([i.split(' ')[0],i.split(' ')[1]])

#reds = [['1132','1200'],['1207','1230'],['1237','1250']]
time = dt.datetime.now()

pygame.init()

pygame.display.set_caption("Clock")

pygame.display.set_icon(pygame.image.load('Data/icon.png'))

width,height=(500,500)

screen=pygame.display.set_mode((width,height))

running = True

font = pygame.font.Font('Data/Numbers.ttf',226)
font2 = pygame.font.Font('Data/Numbers.ttf',64)
font3 = pygame.font.Font('Data/Other.ttf',24)

currentColor = (0,225,0)

outside=False

def checkMinute():
    for i in range(len(reds)):
        for x in range(2):
            #if the red < current time
            if(((int(reds[i][x][:-2])*60)+int(reds[i][x][-2:]))<(((12 if time.hour==0 else time.hour)*60)+time.minute)+1):
                currentRed=i
                if(x==1 and i!=len(reds)-1):
                    currentColor=(0,255,0)
                elif(x==1):
                    
                    currentColor=(1,1,1)
                else:
                    currentColor=(255,0,0)
            elif(i==0 and x==0):
                return (225,225,225),i
    return currentColor,currentRed

import math

def updateTimer():
    if(currentColor==(225,225,225)):
        return "n:nn"
    else:
        t1 = dt.datetime.strptime(str(12 if time.hour == 0 else time.hour) + ':' + str(time.minute) + ':' + str(time.second),"%H:%M:%S")
        t2 = dt.datetime.strptime(currentInterval.split(' - ')[1]+':00', "%H:%M:%S")
        d=t2-t1
        dStr = str(math.floor(d.total_seconds()/60)) + ':' + str(int(d.total_seconds()-(math.floor(d.total_seconds()/60)*60)))
        if(dStr[-2]==':'):
            dStr = dStr[:-1] + '0' + dStr[-1]
        return dStr

def fix(currentColor):
    if(currentColor==(0,255,0)):
        currentInterval=reds[currentRed][1][:-2] + ':' + reds[currentRed][1][-2:] + ' - ' + reds[currentRed+1][0][:-2] + ':' + reds[currentRed+1][0][-2:]
    elif(currentColor==(255,0,0)):
        currentInterval=reds[currentRed][0][:-2] + ':' + reds[currentRed][0][-2:] + ' - ' + reds[currentRed][1][:-2] + ':' + reds[currentRed][1][-2:]
    elif(currentColor==(1,1,1)):
        currentColor=(225,225,225)
        currentInterval="will show tmr"
    else:
        currentInterval = reds[0][0][:-2] + ':' + reds[0][0][-2:]
    return currentInterval, currentColor

currentColor,currentRed=checkMinute()
currentInterval,currentColor = fix(currentColor)
currentTime=updateTimer()

while running:
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            running=False
    if(time.minute != dt.datetime.now().minute):
        time=dt.datetime.now()
        currentColor,currentRed=checkMinute()
        currentInterval,currentColor=fix(currentColor)
        time=dt.datetime.now()
        currentTime=updateTimer() 
    elif(time.second != dt.datetime.now().second):
        time=dt.datetime.now()
        currentTime=updateTimer()
    topText = font2.render(currentInterval,True,currentColor)
    text=font.render(currentTime,True,currentColor)
    screen.fill((0,0,0))
    screen.blit(text,((width/2)-(text.get_width()/2),(height/2)-166))
    screen.blit(topText,((width/2)-(topText.get_width()/2),(height/8)-topText.get_height()))
    pygame.display.flip()
