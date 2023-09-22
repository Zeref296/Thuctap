import pygame
import sys
import random

# Khởi tạo Pygame
pygame.init()

# Khởi tạo biến trạng thái trò chơi
game_over = False
# Khởi tạo biến điểm số
score = 0
# Cài đặt màn hình
WIDTH, HEIGHT = 400, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rắn săn mồi")

# Màu sắc
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Khởi tạo rắn
snake = [(100, 50), (90, 50), (80, 50)]
dx, dy = 10, 0

hit = False
# Tốc độ mặc định của rắn
snake_speed = 10  

# Khởi tạo thức ăn
food = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))
background_img = pygame.image.load("background.jpg")


# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        dx, dy = 0, -10
    if keys[pygame.K_DOWN]:
        dx, dy = 0, 10
    if keys[pygame.K_LEFT]:
        dx, dy = -10, 0
    if keys[pygame.K_RIGHT]:
        dx, dy = 10, 0

    # Cập nhật vị trí rắn
    new_head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, new_head)
    
    # Kiểm tra xem đầu của rắn có va chạm vào thân
    if new_head in snake[1:]:
        hit = True  
        


    
    
    # Kiểm tra xem rắn đã ăn thức ăn chưa
    if snake[0] == food:
        food = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))
        score += 1 # Tăng điểm số khi ăn thức ăn
        snake_speed += 1
        hit = False
        
    else:
        if hit:
            game_over = True
            
        snake.pop()

    # Kiểm tra nếu rắn chạm vào tường
    if (
        snake[0][0] < 0
        or snake[0][0] >= WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= HEIGHT
        
    ):
        game_over = True

    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over! Play again (Y/N)?", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        win.blit(text, text_rect)
        pygame.display.update()

        # Hỏi người chơi có muốn chơi lại không
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        # Reset trạng thái trò chơi
                        game_over = False
                        snake = [(100, 50), (90, 50), (80, 50)]
                        dx, dy = 10, 0
                        score = 0
                        snake_speed = 10
                        food = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))
                    elif event.key == pygame.K_n:
                        pygame.quit()
                        sys.exit()

    # Hiển thị điểm số lên màn hình
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    text_rect = text.get_rect(topleft=(10, 10))
    win.blit(text, text_rect) 
    # Vẽ thức ăn lên màn hình
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(food[0], food[1], 10, 10))

    
    pygame.display.update()                   
    # Vẽ màn hình
    win.fill(BLACK)
    pygame.draw.rect(win, RED, (food[0], food[1], 10, 10))
    for segment in snake:
        pygame.draw.rect(win, GREEN, (segment[0], segment[1], 10, 10))
    #pygame.display.update()

    # Tốc độ game
    pygame.time.delay(1000 // snake_speed )
