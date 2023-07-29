import pygame as pg,sys
from pygame.locals import *
import time
import copy
import random
import flatten_dict
from flatten_dict import flatten
from flatten_dict import unflatten

#initialize global variables
database={}
record=[]
XO = 'x'
winner = None
width = 400
height = 400
white = (255, 255, 255)
line_color = (10,10,10)
attempt=0

#initizlizing array defining the game
TTT = [['x++']*3,[None]*3,['o++']*3]
#initializing pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100),0,32)
pg.display.set_caption("HEXAPAWN")

#loading the images
opening = pg.image.load('Tic-tac-toe.png')
clear_img=pg.image.load('clear.png')
x_img = pg.image.load('x.png')
o_img = pg.image.load('o.png')
rx_img = pg.image.load('Red_x.png')
ro_img = pg.image.load('red_o.png')
#resizing images
x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.transform.scale(o_img, (80,80))
ro_img = pg.transform.scale(ro_img, (80,80))
rx_img = pg.transform.scale(rx_img, (80,80))
clear_img = pg.transform.scale(clear_img, (80,80))
opening = pg.transform.scale(opening, (width, height+100))


def game_opening():
    #screen.blit(opening,(0,0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)
    
    # Drawing vertical lines
    pg.draw.line(screen,line_color,(width/3,0),(width/3, height),7)
    pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2, height),7)
    # Drawing horizontal lines
    pg.draw.line(screen,line_color,(0,height/3),(width, height/3),7)
    pg.draw.line(screen,line_color,(0,height/3*2),(width, height/3*2),7)
    screen.blit(x_img,(30,30))
    screen.blit(x_img,(width/3+30,30))
    screen.blit(x_img,(2*width/3+30,30))
    screen.blit(o_img,(30,2*width/3+30))
    screen.blit(o_img,(width/3+30,2*width/3+30))
    screen.blit(o_img,(2*width/3+30,2*width/3+30))
    draw_status()
    

def draw_status():
    global draw,winner

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))

    # copy the rendered message onto the board
    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win():
    global TTT, winner,draw
    checko=0
    checki=0
    # check for winning rows
    for i in TTT:
     if 'x++' in i:
      if TTT.index(i)==2:
       winner='x'
    #   break
      checki=1
      
    
       
    for i in TTT:
  
     if 'o++' in i:
      if TTT.index(i)==0:
       winner='o'
    #   break
      checko=1
      
      
    if checki==0:
            winner = 'o'
      
    if(checko==0):
      
       
        winner = 'x'
    if winner:
      modification()
      reset_game()
      
    draw_status()   
 


def drawXO(row,col):
    global TTT,XO,srow,scol,posy,posx,attempt,winner
    status=""
    #if in insertion phase make sure that it is moving directly forward when there's nobody there and move diagonally only whne ther'e somebody there
    if(XO=='x++'):
      
      if (row==(1+srow) and col==(scol)) and ( TTT[row-1][col-1]==None):
        attempt=0
        TTT[srow-1][scol-1]=None
        status='moving'
      elif(row==(1+srow) and ((col==(scol+1))or(col==(scol-1))) and TTT[row-1][col-1]=='o++'):
        attempt=0
        TTT[srow-1][scol-1]=None
        status='attacking'
        screen.blit(clear_img,(posy,posx))
      else:
        XO='x'
        attempt+=1
        screen.blit(clear_img,(posy,posx))
        screen.blit(x_img,(posy,posx))
        if attempt>=3:
         winner='o'
        return;
        
    if(XO=='o++'):
      time.sleep(1)
      if (row==(-1+srow) and col==(scol) and TTT[row-1][col-1]==None):
        attempt=0
        TTT[srow-1][scol-1]=None
        status='moving'
      elif(row==(-1+srow) and ((col==(scol+1))or(col==(scol-1))) and TTT[row-1][col-1]=='x++'):
        attempt=0
        TTT[srow-1][scol-1]=None
        status='attacking'
        screen.blit(clear_img,(posy,posx))
      else:
        XO='o'
        attempt+=1
        screen.blit(clear_img,(posy,posx))
        screen.blit(o_img,(posy,posx))
        modification()
        if attempt>=3:
         winner='x'
        return;
        
    if row==1:
        posx = 30
        srow=1
    if row==2:
        posx = width/3 + 30
        srow=2
    if row==3:
        posx = width/3*2 + 30
        srow=3

    if col==1:
        posy = 30
        scol=1
    if col==2:
        posy = height/3 + 30
        scol=2
    if col==3:
        posy = height/3*2 + 30
        scol=3
             
    
    if(XO == 'x++'):
       TTT[row-1][col-1] = XO#figuire this out
       if status=='moving':
        screen.blit(clear_img,(posy,posx-height/3))
        screen.blit(x_img,(posy,posx))
        XO='o'
        return;
       if status=='attacking':
       # screen.blit(clear_img,(posy,posx-height/3))
        screen.blit(clear_img,(posy,posx))
        screen.blit(x_img,(posy,posx))
        TTT[row-1][col-1]='x++'
        XO='o'
        return;
        
    if(XO == 'o++'):
       TTT[row-1][col-1] = XO
       if status=='moving':
        screen.blit(clear_img,(posy,posx+height/3))
        screen.blit(o_img,(posy,posx))
        XO='x'
        return;
       if status=='attacking':
       # screen.blit(clear_img,(posy,posx+height/3))
        screen.blit(clear_img,(posy,posx))
        screen.blit(o_img,(posy,posx))
        TTT[row-1][col-1]='o++'
        XO='x'
        return;
        
        
    if(XO == 'x'):
     if (TTT[row-1][col-1]=='x++'):
        screen.blit(clear_img,(posy,posx))
        screen.blit(rx_img,(posy,posx))
        XO= 'x++'
        return
    if XO=='o':
     if (TTT[row-1][col-1]=='o++'):
        screen.blit(ro_img,(posy,posx))
        XO= 'o++'
        
    pg.display.update()
   
    

def userClick():
    #get coordinates of mouse click
    x,y = pg.mouse.get_pos()
    #get column of mouse click (1-3)
    if(x<width/3):
        col = 1
    elif (x<width/3*2):
        col = 2
    elif(x<width):
        col = 3
    else:
        col = None
        
    #get row of mouse click (1-3)
    if(y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None
 
    if(row and col):
        global XO
        
        #draw the x or o on screen
        drawXO(row,col)
        check_win()
        
        

def reset_game():
    print('entered reset game')
    print(database)
    global TTT, winner,XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    draw_status()
    winner=None
    TTT = [['x++']*3,[None]*3,['o++']*3]
    game_opening()
def modification():
   global database,value,winner,record,XO
   
   if winner=='x':
    dict=flatten(database)
    for i in record:
     state=(list(i.keys()))
     r=list(i.values())[0][0][0]
     o=list(i.values())[0][0][1]
     if i==record[-1]:
      dict[(state[0]),r,o]/=8
     else:
      dict[(state[0]),r,o]/=2    
    record=[]
    database=unflatten(dict)
    return
   elif winner=='o':
    dict=flatten(database)
    for i in record:
     state=(list(i.keys()))
     r=list(i.values())[0][0][0]
     o=list(i.values())[0][0][1]
     if i==record[-1]:
      dict[(state[0]),r,o]*=8
     else:
      dict[(state[0]),r,o]*=2
    record=[]
    database=unflatten(dict)
    return
   elif (attempt!=0):
    dict=flatten(database)
    i=record[-1]
    state=(list(i.keys()))
    r=list(i.values())[0][0][0]
    o=list(i.values())[0][0][1]
    dict[(state[0]),r,o]=0
    database=unflatten(dict) 
def computers_turn():

  global database,value,winner,record,XO


  red_o={}
  black_o={}
  TTT1=[]
  TTT1=copy.deepcopy(TTT)
  
  #print(TTT1)
  if str(TTT) not in database:
   database[str(TTT)]=red_o#creating database with key as state and value as dictionary with possible o++'s to be moved
   
   for i in (TTT1):
     for j in i:
       if j=='o++':#if o++ id in the state
          #print("entering o++ state")
          #print(i,i.index(j))
          red_o[(str(TTT1.index(i)+1))+','+str(i.index(j)+1)]=black_o#creating dictionary with possible places to place the o
          for k in range(3):
           black_o[str(TTT1.index(i))+','+str(k+1)]=10
          a=TTT1.index(i)
          b=i.index(j) 
          TTT1[a][b]='-'
          TTT[a][b]='o++'
  lst=[]
  weight=[]
  for i in database[str(TTT)]:
    for j in database[str(TTT)][i]:
        lst+=[[i,j]]
        weight.append(database[str(TTT)][i][j])
  if sum(weight)==0:
    winner='x'
    modification()
    draw_status()
    reset_game()
    return
  value=random.choices(lst,weights=weight,k=1)
  dicts={str(TTT):value}
  record.append(dicts)#checkback
  rovalue=row,col=map(int,(value[0][0]).split(','))
  XO='o'
  drawXO(row,col)
  rovalue=row,col=map(int,(value[0][1]).split(','))
  XO='o++'
  drawXO(row,col)
  check_win()
   
    
#starting the game
game_opening()

# run the game loop forever
while(True):
    for event in pg.event.get():
       
        if event.type == QUIT:
            print("quitting")
            pg.quit()
            sys.exit()
        elif XO=='o':
           print("entering computer phase")
           computers_turn()
           
        elif event.type == MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            userClick()
            if(winner):
                reset_game()
            
    pg.display.update()
    CLOCK.tick(fps)
