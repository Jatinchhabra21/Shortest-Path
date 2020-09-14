import pygame
import sys
pygame.init()
black = 0,0,0
red = 255,0,0
green = 0,255,0
white = 255,255,255
size = width,height = 1000,1000
screen = pygame.display.set_mode(size)
screen.fill(white)


def inp_points():
    p1 = input('Enter Point 1 (min - 0,0; max - 49,49) - ')
    p2 = input('Enter Point 2 (min - 0,0; max - 49,49) - ')
    p1 = p1.split(',')
    p2 = p2.split(',')
    for i in range(2):
        p1[i] = int(p1[i])
        p2[i] = int(p2[i])
    p1 = tuple(p1)
    p2=tuple(p2)
    print(p1,p2)
    colour_points(p1,red)
    colour_points(p2,red)
    return [p1,p2]

def colour_points(p,colour):
    pygame.draw.rect(screen,colour,(p[0]*20,p[1]*20,20,20))

def shortest_path(p1,p2):
    x,y = p1
    x1,y1 = p2
    pygame.display.update()
    while(x!=x1 or y!=y1):
        pygame.time.delay(200)
        pygame.display.update()
        if(x==x1 and y!=y1):
            if(y<y1):
                y=y+1
                colour_points((x,y),green)
                continue
            else:
                y=y-1
                colour_points((x,y),green)
                continue
        elif(y==y1 and x!=x1):
            if(x<x1):
                x=x+1
                colour_points((x,y),green)
                continue
            else:
                x=x-1
                colour_points((x,y),green)
                continue
        elif(x>x1 and y>y1):
            x=x-1
            y=y-1
            colour_points((x,y),green)
            continue
        elif(x>x1 and y<y1):
            x=x-1
            y=y+1
            colour_points((x,y),green)
            continue
        elif(x<x1 and y>y1):
            x=x+1
            y=y-1
            colour_points((x,y),green)
            continue
        elif(x<x1 and y<y1):
            x=x+1
            y=y+1
            colour_points((x,y),green)
            continue
        pygame.display.update()

def draw_canvas(screen):
    for i in range(100):
        pygame.draw.lines(screen,black,False,[(i*20,0),(i*20,1000)])
        pygame.draw.lines(screen,black,False,[(0,i*20),(1000,i*20)])
    

l = inp_points()
draw_canvas(screen)
shortest_path(l[0],l[1])
colour_points(l[1],red)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()

    
