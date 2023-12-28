# Conway's Game of Life

## Overview

Conway's Game of Life is a cellular automaton devised by mathematician John Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state and requires no further input. The game takes place on a grid of cells, and each cell can be in one of two states: alive or dead. The game follows a set of simple rules to determine the state of each cell in the next generation, leading to mesmerizing patterns and behaviors.

## Rules

The rules of Conway's Game of Life are straightforward:

1. Any live cell with fewer than two live neighbors dies (underpopulation).
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies (overpopulation).
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

These rules create fascinating patterns and structures that can evolve over time.

## Running the Game

To run Conway's Game of Life, you'll need to have a programming environment or an implementation of the game. You can find numerous versions available in different programming languages and platforms.

Here's an example of running the game using Python:

1. Ensure you have Python installed on your system.
2. Clone or download this repository.
3. Navigate to the directory containing the Conway's Game of Life code.
4. Run the Python script:

   ```bash
   python main.py
   ```

5. Follow the instructions to set up the initial state of the game.

## Customizing the Game

You can modify various aspects of the Game of Life to experiment with different behaviors and patterns:

- **Grid Size:** Change the dimensions of the grid to observe different scales of patterns.
- **Initial State:** Set the initial configuration of live and dead cells to see how the evolution unfolds; By default the initial state is **random**.
- **Clear Window:** Make all the cell dead by hitting ```R``` in keyboard.
- **Adding Cells:** 
    - ```right_click``` to add live cells
    - ```left_click``` to add dead cells

## Examples

Here are a few examples of well-known patterns in Conway's Game of Life:

- **Glider:** A pattern that moves diagonally across the grid.
   - ![App Screenshot]((https://github.com/Yash2402/Conway-s-Game-of-Life/blob/main/Glider.png))
- **Gosper Glider Gun:** A pattern that produces gliders periodically.

## Notes

- While the rules are straightforward, Conway's Game of Life is Turing complete, meaning that it can simulate a universal Turing machine. This fact makes it particularly intriguing for computer scientists and mathematicians.
- The game's evolution is entirely deterministic, meaning that the same initial state will always produce the same subsequent generations.

## Resources

To learn more about Conway's Game of Life, you can check out the following resources:

- [Wikipedia - Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [The Online Life-Like CA Lexicon](https://www.conwaylife.com/wiki/Main_Page)

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it as you like!

Enjoy the mesmerizing world of Conway's Game of Life!
## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

