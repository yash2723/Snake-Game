import pygame
from pygame import mixer
import random

pygame.init()
game_exit = False

# Colors
white = (255,255,255)
food = (173 , 255 , 70)
words = (255 , 0 , 0 )
black = ( 85 , 6 , 244 )

Game_window=pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake Game")

# Sound
mixer.music.load("music.mp3")
mixer.music.play(loops = 10)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,45)

def text_screen(text,color,x,y):
    screen_text = font.render(text , True , color)
    Game_window.blit(screen_text,[x,y])

def draw_rect(color , snake_list , snake_size):
    for x,y in snake_list :
        pygame.draw.rect(Game_window,color,[x,y,snake_size,snake_size])

bgimg = pygame.image.load("welcome.jpg")
bg = pygame.transform.scale(bgimg,(600,600)).convert_alpha()

game_bg = pygame.image.load("game.jpg")
game_bg = pygame.transform.scale(game_bg,(600,600)).convert_alpha()

def welcome():
    while not game_exit:
        Game_window.fill((222,220,230))
        Game_window.blit(bg,(0,0)) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                
        pygame.display.update()       

def game_loop() :
    # Game Specific Variable
    game_exit = False
    game_over = False
    snake_x = 60
    snake_y = 70
    snake_size = 10
    fps = 30
    init_velocity = 7
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(60,500)
    food_y = random.randint(60,490)
    score = 0
    snake_length = 1
    snake_list = []

    hiscore = open("High_Score.txt")
    h1 = int(hiscore.read())

    while not game_exit:
        #pygame.draw.rect(Game_window,words,[28,28,snake_size,snake_size])
        #pygame.draw.rect(Game_window,words,[560,523,snake_size,snake_size])
        pygame.display.update()
        '''
        for event in pygame.event.get():
            print(event)
        '''
            
        if game_over :
            update = open("High_Score.txt",'w')
            update.write(str(h1))
            Game_window.fill(white)
            text_screen(" Game is over . Press enter for Restart ",words,0,250)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else :
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_exit=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        #snake_x = snake_x + 10
                        velocity_x = init_velocity
                        velocity_y = 0

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_DOWN:
                        #snake_y = snake_y + 10
                        velocity_x = 0
                        velocity_y = init_velocity

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        #snake_y = snake_y - 10
                        velocity_x = 0
                        velocity_y = -init_velocity

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        #snake_x = snake_x - 10
                        velocity_x = -init_velocity
                        velocity_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        init_velocity += 1

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        if init_velocity > 0 :
                            init_velocity -= 1

                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_p:
                        pygame.display.update()
                        while True :
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                        
                                if event.type == pygame.KEYDOWN :
                                    if event.key == pygame.K_SPACE:
                                            continue
                        pygame.display.update()

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 8  and  abs(snake_y - food_y) < 8 :
                score += 10
                snake_length = snake_length + 5 
                food_x = random.randint(200,400)
                food_y = random.randint(100,400)
                if score > h1:
                    h1 = score

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length :
                del snake_list[0]

            if snake_x < 30 or snake_x > 555 or snake_y < 30 or snake_y > 520 :
                game_over = True

            if head in snake_list[ :-1]:
                game_over = True

            Game_window.fill(white)
            Game_window.blit(game_bg , (0,0))
            text_screen("Score : " + str(score) , words , 40 , 565 )
            text_screen("High Score : " + str(h1) , words , 250 , 565 )
            pygame.draw.rect(Game_window,food,[food_x,food_y,snake_size,snake_size])
            draw_rect(black,snake_list,snake_size)
            pygame.display.update()
            clock.tick(fps)

welcome()
pygame.quit()

