import torch
import torch.optim as optim
from game_env.game import GoGame
from model.neural_network import GoNeuralNetwork
import random

class SelfPlayTrainer:
    def __init__(self, board_size=19):
        self.board_size = board_size
        self.game = GoGame(board_size)
        self.model = GoNeuralNetwork(board_size)
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)

    def get_board_tensor(self):
        # Convert the board to a tensor
        board_array = [[self.game.board[y][x] for x in range(self.board_size)] for y in range(self.board_size)]
        board_tensor = torch.tensor(board_array, dtype=torch.float32)
        board_tensor = board_tensor.unsqueeze(0).unsqueeze(0)  # Shape: (1, 1, board_size, board_size)
        return board_tensor

    def select_move(self, board_tensor):
        # Get move probabilities from the model
        with torch.no_grad():
            logits = self.model(board_tensor)
            probabilities = torch.softmax(logits.flatten(), dim=0)
        # Mask invalid moves
        valid_moves = self.game.get_valid_moves()
        valid_indices = [y * self.board_size + x for x, y in valid_moves]
        masked_probs = torch.zeros(self.board_size * self.board_size)
        masked_probs[valid_indices] = probabilities[valid_indices]
        # Normalize probabilities
        if masked_probs.sum().item() == 0:
            return random.choice(valid_moves)
        masked_probs /= masked_probs.sum()
        # Select a move based on probabilities
        move_index = torch.multinomial(masked_probs, 1).item()
        x = move_index % self.board_size
        y = move_index // self.board_size
        return (x, y)

    def play_game(self):
        # Play a single game
        self.game.reset()
        states = []
        actions = []
        while not self.game.is_game_over():
            board_tensor = self.get_board_tensor()
            move = self.select_move(board_tensor)
            self.game.make_move(*move)
            states.append(board_tensor)
            actions.append(move)
        # Placeholder: Store game result for training
        return states, actions

    def train(self, num_games=1000):
        for _ in range(num_games):
            states, actions = self.play_game()
            # Placeholder: Implement training logic using stored states and actions