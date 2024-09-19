
### Training the Neural Network

To start training the model using self-play:

1. Create a new Python file, e.g., `train_model.py`, in the project root directory.

2. Add the following code to `train_model.py`:

   ```python
   from training.self_play import SelfPlayTrainer

   def main():
       trainer = SelfPlayTrainer()
       trainer.train(num_games=1000)  # Adjust the number of games as needed

   if __name__ == "__main__":
       main()
   ```

3. Run the training script:

   ```bash
   python train_model.py
   ```

This will start the training process using self-play. The model will play against itself for the specified number of games, improving its performance over time.

Note: The current implementation has placeholders for game over conditions and winner determination. You may need to implement these in the `GoGame` class before training for meaningful results.

## Customizing Training

You can customize the training process by modifying the `SelfPlayTrainer` class in `training/self_play.py`. Some possible improvements include:

- Implementing a proper reward system based on game outcomes
- Adding regularization to prevent overfitting
- Experimenting with different neural network architectures
- Implementing early stopping based on validation performance

## TODO

- Implement game over conditions and winner determination in `GoGame`.
- Complete the training loop in `SelfPlayTrainer`.
- Add functionality to save and load trained models.
- Implement additional Go game rules (e.g., capturing stones, ko rule).
- Improve the UI to display game information and allow for different board sizes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).