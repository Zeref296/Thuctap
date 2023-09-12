import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_rong = 800
dis_dai = 600

dis=pygame.display.set_mode((dis_rong,dis_dai))
pygame.display.set_caption('Rắn săn mồi')


snake_block = 10
tocdo = 15

clock = pygame.time.Clock()



font_style = pygame.font.SysFont("Blackadder ITC", 27)
score_font = pygame.font.SysFont("Times New Roman", 35)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_rong/3.5, dis_dai/2.5])

def snake_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [ x[0], x[1], snake_block, snake_block ])
def diemso(score):
    diem = score_font.render("Điểm số: " +str(score), True, black)
    dis.blit(diem, [0, 0])
def gameloop():
    game_over=False
    game_close=False 

    x1 = dis_rong/2
    x2 = dis_dai/2
    
    x1_change = 0
    x2_change = 0

    snake_List = []
    Length_of_snake = 1

    thucan1 = round(random.randrange(0, dis_rong - snake_block) / 10.0) * 10.0
    thucan2 = round(random.randrange(0, dis_dai - snake_block) / 10.0 ) * 10.0


    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Q-Quit or C-Play Again", red)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN :
                if event.key==pygame.K_LEFT :
                    x1_change = -snake_block
                    x2_change = 0
                elif event.key==pygame.K_UP :
                    x2_change = -snake_block
                    x1_change = 0
                elif event.key==pygame.K_RIGHT :
                    x1_change = snake_block
                    x2_change = 0
                elif event.key==pygame.K_DOWN : 
                    x2_change = snake_block
                    x1_change = 0
        if x1 >= dis_rong or x1 < 0 or x2 >= dis_dai or x2 < 0:
            game_close=True
        x1 += x1_change
        x2 += x2_change
        dis.fill(white)
        pygame.draw.rect(dis,red,[thucan1,thucan2,snake_block,snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(x2)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake_snake(snake_block, snake_List)
        diemso(Length_of_snake - 1)
        pygame.display.update()

        if x1 == thucan1 and x2 == thucan2:
            thucan1 = round(random.randrange(0, dis_rong - snake_block) / 10.0) * 10.0
            thucan2 = round(random.randrange(0, dis_dai - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(tocdo)

    pygame.quit()
    quit()
gameloop()