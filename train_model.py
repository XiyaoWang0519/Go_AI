# Install required packages
!pip install torch numpy

# Clone the repository (assuming your project is on GitHub)
!git clone https://github.com/your-username/your-repo-name.git
%cd Go_AI

# Import necessary modules
from training.self_play import SelfPlayTrainer
from model.neural_network import NeuralNetwork
from game_env.game import GoGame

# Set up the neural network, game environment, and trainer
input_size = 81  # 9x9 board
hidden_size = 128
output_size = 81  # 9x9 possible moves
learning_rate = 0.001

neural_net = NeuralNetwork(input_size, hidden_size, output_size)
game = GoGame()
trainer = SelfPlayTrainer(neural_net, game, learning_rate)

# Train the model
num_games = 1000
trainer.train(num_games=num_games)

# Save the trained model
import torch
torch.save(neural_net.state_dict(), 'trained_model.pth')

print(f"Training completed. Model saved as 'trained_model.pth'")

# Optional: Download the trained model
from google.colab import files
files.download('trained_model.pth')