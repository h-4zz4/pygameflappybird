import pygame
from pygame.locals import *
import time
import random
pygame.init() #sets up pygame

clock = pygame.time.Clock()

win = pygame.display.set_mode((400,600))
pygame.display.set_caption('Flappy Bird') 
bg = pygame.image.load('C:/Users/200309/Desktop/programs/flappybird/birdbg.png')
b_i = pygame.image.load('C:/Users/200309/Desktop/programs/flappybird/f_bird.png')
b_j = pygame.image.load('C:/Users/200309/Desktop/programs/flappybird/bird_jump.png')
b_d = pygame.image.load('C:/Users/200309/Desktop/programs/flappybird/bird_d.png')
p_1 = pygame.image.load('C:/Users/200309/Desktop/programs/flappybird/pipe_1.png')
p_2 = pygame.image.load('C:/Users/200309/Desktop/programs/flappybird/pipe_2.png')
score = 0                                 #creates screen, caption, background, and score counter

font = pygame.font.Font('freesansbold.ttf', 24)
font_l = pygame.font.Font('freesansbold.ttf', 36)
text = font.render('', True, (255,255,255), (0,0,0))
g_o = font_l.render('Game Over. Score', True, (255,255,0), (0,0,0)) #renders all of the fonts used

pipe_speed = 2
pipe1x = 345
pipe2x = 345+220
pipe1y = -270
pipe2y = 420
pipe3y = -270
pipe4y = 420
width = 72
height1 = 400
height2 = 3000 #creates measurement variables for the 'pipes' featured in the game

ww = 0 # this is a tick after birdjump counter used for many things
birdJump = False
vel = 5
bird_x = 20
bird_y = 100 #creates all of the variables nessasary for the bird

yy = 0#these are template variables used for RNG
xx = 0

class fb:
    def move():
        global pipe1x
        global pipe2x
        global yy
        global pipe1y
        global pipe2y
        global pipe3y
        global pipe4y
        global bird_x
        global bird_y
        global pipe_speed
        global score #globalises these integers/strings
        global xx
        pipe1x -= pipe_speed
        pipe2x -= pipe_speed
        if pipe1x < -60:
            pipe1x = 345
            yy = random.randint(-350,0)
            pipe1y = yy
            pipe2y = pipe1y + 555       #checks if the pipes are fully of screen and, if so, moves them back to the other side,
            score += 1                  #adding 1 to the score variable as it does so
        if pipe2x < -60:
            pipe2x = 345
            yy = random.randint(-350,0)
            pipe3y = yy
            pipe4y = pipe3y + 555
            score += 1
        win.blit(bg, (0,0))
        pipe1 = pygame.draw.rect(win, (88, 192, 203), (pipe1x, pipe1y, width, height1))
        pipe2 = pygame.draw.rect(win, (88, 192, 203), (pipe1x, pipe2y, width, height2))
        pipe3 = pygame.draw.rect(win, (88, 192, 203), (pipe2x, pipe3y, width, height1))
        pipe4 = pygame.draw.rect(win, (88, 192, 203), (pipe2x, pipe4y, width, height2))
        bird = pygame.draw.rect(win, (88, 192, 203), (bird_x, bird_y, 40, 32))
        if ww < 21:
            win.blit(b_j, (bird_x, bird_y))
        elif ww > 20 and ww < 30:
            win.blit(b_i, (bird_x, bird_y))
        else:
            win.blit(b_d, (bird_x, bird_y))
        win.blit(p_2,(pipe1x, pipe1y))
        win.blit(p_1,(pipe1x, pipe2y))
        win.blit(p_2,(pipe2x, pipe3y))
        win.blit(p_1,(pipe2x, pipe4y))
        text = font.render(f'Score: {str(score)}', True, (255,255,255))     #creating the rectangles used to represent the background,
        win.blit(text, (275,0))                                             #pipes, score, and bird; the bird image is pasted over the
        pygame.display.update()                                             #
        if ww > 15:                                                         #blue rectangle later
            bird_y += 4              #adds 2 to the bird's y variable, moving it down
            if ww > 19:
                bird_y += 2
                if ww > 39:
                    bird_y += 3
        if ww < 6:
            bird_y -= 13 
        if bird.colliderect(pipe3) == True:
            fb.gameover()      
        if bird.colliderect(pipe4) == True:
            fb.gameover()        
        if bird.colliderect(pipe1) == True:
            fb.gameover()       
        if bird.colliderect(pipe2) == True:
            fb.gameover()                   #sending the user to the gameover() function if the bird collides with a pipe
    def gameover():
        global score
        time.sleep(0.5)
        pygame.draw.rect(win,(0,0,0), (0,0,1000,1000))
        g_o = font_l.render(f'Game Over. Score: {score}', True, (255,255,0), (0,0,0))
        win.blit(g_o, (15,275)) 
        pygame.display.update()
        score = 0
        time.sleep(3)
        pygame.quit()      #creates a 'game over' message, waits 5 seconds, then quits                               
    def checks():
        global yy
        global bird_x
        global bird_y
        global pipex
        if bird_y > 600:         #checks if the bird is below the floor
            fb.gameover()
    def pause():
        time.sleep(1)               #sleeps for 1 second, so the user can hold the space button down and halt the game
ww = 31
while True:
    ww += 1
    keys = pygame.key.get_pressed() #checks for any pressed keys
    if keys[pygame.K_b]:                        
        fb.pause()                 
    fb.move()                       
    #time.sleep(0.005)               #as not to run at hyperspeed
    fb.checks()
    for event in pygame.event.get():    #Why is this necassary? (how does one spell that word???)
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        elif event.type==KEYDOWN:
            if event.key==K_SPACE:
                ww = 0
    clock.tick(60)

#github: h-4zz4