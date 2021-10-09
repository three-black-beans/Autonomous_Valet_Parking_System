import pygame
import sys
from pygame.locals import *
from time import sleep

pygame.init()
SURFACE=pygame.display.set_mode((1000,600))
screen_width=1000
screen_height=600
pygame.display.set_caption("Drawing")
FPSCLOCK=pygame.time.Clock()

def main():
    sysfont=pygame.font.SysFont(None,36)
    counter=110
    background=pygame.image.load("주차장이요.png")
    car=pygame.image.load("자동차요.png")
    car_pos_x=800
    car_pos_y=300
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
                
        counter-=1
        SURFACE.fill((255,255,255))
        SURFACE.blit(background,(0,0),Rect(0,0,1000,600))
        count_image=sysfont.render("{}".format(int(counter/10)),True,(255,255,255))
        SURFACE.blit(count_image,(0,0))
        SURFACE.blit(car,(450,200))
       
            
        pygame.display.update()
        FPSCLOCK.tick(20)






if __name__=='__main__':
    main()