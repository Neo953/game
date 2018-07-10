import pygame
import random
import sys
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

#getting the ball
Ball = pygame.image.load("Ball.png")
Ball = pygame.transform.smoothscale(Ball, (100,100))
Ball_rect = Ball.get_rect()
Ball_speed = pygame.math.Vector2(0,5)
Ball_speed.rotate_ip(random.randint(0,360))


def Ball_move():
    #get information from screen in case of resizing
    screen_info = pygame.display.Info()
    Ball_rect.move_ip(Ball_speed)
    if Ball_rect.left < 0 or Ball_rect.right > screen_info.current_w:
        Ball_speed[0] *= -1
        Ball_rect.move_ip(Ball_speed[0], 0)
    if Ball_rect.top < 0 or Ball_rect.bottom > screen_info.current_h:
        Ball_speed[1] *= -1
        Ball_rect.move_ip(0, Ball_speed[1])


#set the width and the hight to the size of the screen

size = (width, height) = (screen_info.current_w, screen_info.current_h)
Ball_rect.center = (width/2, height/2)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (26,255,255)

def main():

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        Ball_move()
        screen.fill(color)
        screen.blit(Ball,Ball_rect)
        pygame.display.flip()

if __name__ == '__main__':
    main()

