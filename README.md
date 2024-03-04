# 2048-AI

This is a Python implementation of the popular game 2048, with an option to use an AI player.

## Project Structure

The project is structured as follows:

- `src/main.py`: This is the main entry point of the application.
- `src/game/game.py`: This file contains the logic for the game, including starting the game, adding and moving tiles, and checking the game status.
- `src/game/game_class.py`: This file defines the `Game` class, which is used to create a game instance and play the game.
- `src/game/ai.py`: This file contains the logic for the AI player.
- `src/ai/ai_class.py`: This file defines the `AI` class, which will be used to implement an AI player instance for the game.

## How to Run

To run the game, navigate to the `src` directory and run `main.py`:

```bash
python main.py
```

When prompted, enter `y` to play the game or `n` to let the AI play the game.

## How to Play

The game is played in the CLI. The game board is a 4x4 grid, where each cell can contain a tile with a number. The goal of the game is to combine tiles with the same number to create a tile with the number 2048.  To move the tiles, enter one of the following commands:

- `w`: Move the tiles up
- `a`: Move the tiles left
- `s`: Move the tiles down
- `d`: Move the tiles right

If the game board cannot be moved in the chosen direction, you will need to choose a different direction. The game ends when a tile with the number 2048 is created (you win), or the board is full and no more moves can be made (you lose).
