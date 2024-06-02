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

def check_win(current_player):
    for row in range(3):
        if all(cell == current_player for cell in board[row]):
            return True
    for col in range(3):
        if all(board[row][col] == current_player for row in range(3)):
            return True
    if all(board[i][i] == current_player for i in range(3)):
        return True
    if all(board[i][2 - i] == current_player for i in range(3)):
        return True
    return False

def get_available_moves():
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                moves.append((row, col))
    return moves

def is_board_full():
    return all(all(cell != '' for cell in row) for row in board)

def ai_turn():
    best_move = None
    best_eval = -math.inf
    for move in get_available_moves():
        row, col = move
        board[row][col] = 'O'
        eval = minimax(board, 0, False)
        board[row][col] = ''
        if eval > best_eval:
            best_eval = eval
            best_move = move
    row, col = best_move
    board[row][col] = 'O'

def minimax(board, depth, maximizing_player):
    if check_win('O'):
        return 1
    if check_win('X'):
        return -1
    if is_board_full():
        return 0
    if maximizing_player:
        max_eval = -math.inf
        for move in get_available_moves():
            row, col = move
            board[row][col] = 'O'
            eval = minimax(board, depth + 1, False)
            board[row][col] = ''
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves():
            row, col = move
            board[row][col] = 'X'
            eval = minimax(board, depth + 1, True)
            board[row][col] = ''
            min_eval = min(min_eval, eval)
        return min_eval
    
def show_winner_message(winner_message):
    #loop to keep the window open
    while True:
        window.fill(WHITE)

        font = pygame.font.Font(None, 50)
        text = font.render(winner_message, True, GREEN)
        text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
        window.blit(text, text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

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

    if check_win('X'):
        winner_message = 'X wins!'
        running = False
        show_winner_message(winner_message)
    elif check_win('O'):
        winner_message = 'O wins!'
        running = False
        show_winner_message(winner_message)
    elif is_board_full():
        winner_message = 'It\'s a draw!'
        running = False
        show_winner_message(winner_message)
    else:
        winner_message = ''

    if current_player == 'O':
        ai_turn()
        current_player = 'X'

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