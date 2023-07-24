# rush-hour-game
# Rush Hour Puzzle Solver

## Overview

The Rush Hour Puzzle Solver is a Python program designed to solve the classic Rush Hour puzzle game. The Rush Hour puzzle consists of a 6x6 grid board with cars of varying lengths placed on it. The goal is to move the cars horizontally or vertically to create a path for the red car to reach the exit at the rightmost edge of the board.

This project consists of three main classes: Board, Car, and Game. The Board class represents the game board, the Car class represents the cars on the board, and the Game class manages the game and allows the player to interact with the board.

## Features

- Read car configurations from a JSON file and place them on the board.
- Allow the player to move the cars using a simple text-based user interface.
- Check the validity of the moves and update the board accordingly.
- Provide an interactive and efficient Rush Hour puzzle solver.

## Usage

1. Run the `game.py` script with the path to a JSON file containing car configurations as a command-line argument.
2. Follow the prompts to input the name of the car and the direction you want to move it (up, down, left, or right).
3. The program will check the validity of the moves and update the board accordingly until the red car reaches the exit.

## Requirements

- Python 3.x

## File Structure

- `board.py`: Contains the Board class representing the game board.
- `car.py`: Contains the Car class representing the cars on the board.
- `game.py`: Contains the Game class managing the game and the main driver of the program.

## Note

This project is implemented as an exercise for the Intro to Computer Science course in the 2022-2023 academic year.

## Contributors

- Amitai Turkel

Feel free to contribute to this project by adding new features, improving existing code, or suggesting enhancements.

Happy Rush Hour Puzzle Solving!
