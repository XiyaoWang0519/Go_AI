import torch
import torch.nn as nn
import torch.nn.functional as F

class GoNeuralNetwork(nn.Module):
    def __init__(self, board_size=19):
        super(GoNeuralNetwork, self).__init__()
        self.board_size = board_size
        self.conv1 = nn.Conv2d(1, 64, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.fc = nn.Linear(128 * board_size * board_size, board_size * board_size)

    def forward(self, x):
        # x should have shape (batch_size, 1, board_size, board_size)
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = x.view(-1, 128 * self.board_size * self.board_size)
        x = self.fc(x)
        x = x.view(-1, self.board_size, self.board_size)
        return x