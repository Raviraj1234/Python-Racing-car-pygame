import pygame
import random
import time
pygame.init()

display_width = 700
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (219,87,87)
bright_red=(230,85,85)
choclate=(141,95,95)
bright_choclate=(167,111,111)
car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("DHOOM 3")
clock = pygame.time.Clock()

carImg = pygame.image.load('car.jpg')
carImg2 = pygame.image.load('car2.png')
carImg3 = pygame.image.load('car3.png')
carImg4 = pygame.image.load('car4.png')
carImg5 = pygame.image.load('car5.jpg')
carImg6 = pygame.image.load('car6.png')

game_introImg=pygame.image.load('game_intro.png')
y_y=0
score=0
crashImg=pygame.image.load('crash.jpg')
surfaceImg=pygame.image.load('pygame_UI.jpg')
obs=0
car_pic = pygame.image.load('car1.png')

def car(x,y): 
    gameDisplay.blit(carImg,(x,y))
    
def crash():
    message_display('CRASHED')
def message_display(message):
    largetext=pygame.font.Font('freesansbold.ttf',115)
    Textsurf,Textrect=text_objects(message,largetext)
    Textrect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(Textsurf,Textrect)
    time.sleep(0.5)
    pygame.display.update()
    pygame.quit()
    quit()
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()   
    
def Score(score):
    font=pygame.font.SysFont(None,40)
    text=font.render("Score: "+str(score),True,black)
    gameDisplay.blit(text,(0,0))
def things(startx,starty,obs):

    global car_pic    
    if(obs==0):
        car_pic = pygame.image.load('car1.png')
    if(obs==1):
        car_pic = pygame.image.load('car2.png')
    if(obs==2):
        car_pic = pygame.image.load('car3.png')
    if(obs==3):
        car_pic = pygame.image.load('car4.png')
    if(obs==4):
        car_pic = pygame.image.load('car5.jpg')
    if(obs==5):
        car_pic = pygame.image.load('car6.png')
    print(obs)
    
    gameDisplay.blit(car_pic,(startx,starty))

def button(msg,startx,starty,pix,piy,color1,color2,action):
    
    mouse=pygame.mouse.get_pos()
    button_pressed=pygame.mouse.get_pressed()
    print(mouse)
    if(startx<mouse[0]<startx+pix and starty<mouse[1]<starty+piy):           
        pygame.draw.rect(gameDisplay,color1,(startx,starty,pix,piy))
        if(button_pressed[0]==1 and action!=None):
            if(action=="play"):
                game_loop()
            elif(action=="quit"):
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay,color2,(startx,starty,pix,piy))
    small_text=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,small_text)
    textrect.center=((startx+pix/2),(starty+piy/2))
    gameDisplay.blit(textsurf,textrect)
    
def game_intro():
    intro=True

    while (intro):
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                quit()
        gameDisplay.blit(game_introImg,(0,0))
             
        
        button("START",100,400,100,40,red,bright_red,"play")
        button("STOP",500,400,100,40,choclate,bright_choclate,"quit")
        
        pygame.display.update()
        clock.tick(15)
        
def game_loop():
    global y_y
    global score
    x = (display_width * 0.45)
    y = (display_height * 0.70)
    obs=0
    x_change = 0
    startx=random.randrange(130,500)
    starty=-300
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        rel_y=y_y%surfaceImg.get_rect().height
        gameDisplay.blit(surfaceImg,(0,rel_y-surfaceImg.get_rect().height))
        if(rel_y<display_height):
            gameDisplay.blit(surfaceImg,(0,rel_y))
        y_y=y_y+10
        
        Score(score)
        
        car(x,y)
        things(startx,starty,obs)
        starty=starty+15
        if(starty>display_height):
            score=score+1
            starty=-300     
            startx=random.randrange(130,500)
            obs=random.randrange(0,6)
            
        
        
        if (x > display_width - car_width-120 or x < 140) :
            crash()
        if(starty+100>y):
            if((x>startx and x<=startx+60) or ((x+63)>startx and(x+63)<=startx+60)):
                crash()            
        pygame.display.update()
        clock.tick(60)


game_intro()
pygame.quit()
quit()