import math
import pygame

pygame.init()

window_width = 300
window_height = 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Noughts and Crosses")

BLACK = (20, 20, 20)
WHITE = (230, 230, 230)
BLUE = (0, 102, 204)
ORANGE = (255, 102, 0)
GREEN = (0, 153, 51)

board = [['', '', ''],
        ['', '', ''],
        ['', '', '']]

current_player = 'X'

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            cell_x = mouse_x // (window_width // 3)
            cell_y = mouse_y // (window_height // 3)
            
            if board[cell_y][cell_x] == '':
                board[cell_y][cell_x] = current_player
                current_player = 'O' if current_player == 'X' else 'X'

    window.fill(WHITE)
    cell_width = window_width // 3
    cell_height = window_height // 3
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(window, BLACK, (col * cell_width, row * cell_height, cell_width, cell_height), 5)
            if board[row][col] != '':
                font = pygame.font.Font(None, 100)
                if board[row][col] == 'X':
                    text = font.render(board[row][col], True, BLUE)
                else:
                    text = font.render(board[row][col], True, ORANGE)
                text_rect = text.get_rect(center=(col * cell_width + cell_width // 2, row * cell_height + cell_height // 2))
                window.blit(text, text_rect) 

    pygame.display.flip()

pygame.quit()