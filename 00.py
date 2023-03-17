import pygame
import sys
SIZE_BLOCK = 20
FRAME_COLOR = (251, 87, 11)
HEAD_COLOR = (0, 204, 153)
SNAKE_COLOR = (185, 0, 0)
WHITE = (255, 255, 255)
GRAY = (80, 166, 253)
size = [460, 530]
COUNT_BLOCK = 20 
MARGIN = 1   

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake game")
icon = pygame.image.load("mysnake.png")
pygame.display.set_icon(icon)
timer = pygame.time.Clock()


class SnakeBlock:
    def init(self, x, y):
        self.x = x
        self.y = y
    def is_inside(self):
        return 0 <= self.x < SIZE_BLOCK and 0 <= self.y < SIZE_BLOCK
    
        

snake_block = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]


def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [20+(column*SIZE_BLOCK)+MARGIN*(column+1), 90+(row*SIZE_BLOCK)+MARGIN*(row+1), SIZE_BLOCK, SIZE_BLOCK])


d_row = 0
d_col = 1
while True:
    for event in pygame.event.get():
        if (event.type) == pygame.QUIT:
            print('Exist')
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col !=0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEAD_COLOR, [0, 0, 460, 91])
    
    for row in range(COUNT_BLOCK):
        for column in range(COUNT_BLOCK):
            if(column+row)%2 == 0:
                color = WHITE
            else:
                color = GRAY
            draw_block(color, row, column)    

    head = snake_block[-1]
    if head.is_inside():
        for block in snake_block:
            draw_block(SNAKE_COLOR, block.x, block.y)
    else:
        print('Crush')
        pygame.quit()
        sys.exit()

    
    new_head = SnakeBlock(head.x+d_row, head.y+d_col)
    snake_block.append(new_head)
    snake_block.pop(0)

    # pygame.draw.rect(screen ,WHITE, [10, 20, SIZE_BLOCK, SIZE_BLOCK])
    pygame.display.flip()
    timer.tick(2)