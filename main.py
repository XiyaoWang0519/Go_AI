import pygame
from go_game import GoGame, BLACK, WHITE, EMPTY

WINDOW_SIZE = (800, 600)  # Adjust the values as needed
BOARD_COLOR = (220, 179, 92)  # Light wood color

def draw_game_info(screen, game):
    font = pygame.font.Font(None, 24)
    current_player = "Black" if game.current_player == BLACK else "White"
    text = font.render(f"Current Player: {current_player}", True, (0, 0, 0))
    screen.blit(text, (10, WINDOW_SIZE[1] - 30))

    if game.is_game_over():
        winner = game.get_winner()
        if winner == BLACK:
            result = "Black Wins!"
        elif winner == WHITE:
            result = "White Wins!"
        else:
            result = "Draw!"
        text = font.render(result, True, (0, 0, 0))
        screen.blit(text, (WINDOW_SIZE[0] - 100, WINDOW_SIZE[1] - 30))

def get_board_position(x, y, board_size):
    board_width = min(WINDOW_SIZE)
    cell_size = board_width / board_size
    row = int(y / cell_size)
    col = int(x / cell_size)
    return row, col

def draw_board(screen, game):
    board_width = min(WINDOW_SIZE)
    cell_size = board_width / game.size
    for row in range(game.size):
        for col in range(game.size):
            x = col * cell_size
            y = row * cell_size
            pygame.draw.rect(screen, (0, 0, 0), (x, y, cell_size, cell_size), 1)
            if game.board[row][col] != EMPTY:
                color = (0, 0, 0) if game.board[row][col] == BLACK else (255, 255, 255)
                pygame.draw.circle(screen, color, (int(x + cell_size/2), int(y + cell_size/2)), int(cell_size/2 - 2))

def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Go Game")

    board_sizes = [9, 13, 19]
    current_size_index = 0
    game = GoGame(board_sizes[current_size_index])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    x, y = event.pos
                    row, col = get_board_position(x, y, game.size)
                    game.make_move(row, col)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_size_index = (current_size_index + 1) % len(board_sizes)
                    game = GoGame(board_sizes[current_size_index])

        screen.fill(BOARD_COLOR)
        draw_board(screen, game)
        draw_game_info(screen, game)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()