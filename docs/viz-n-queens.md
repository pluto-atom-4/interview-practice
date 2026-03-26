# Visualize N Queens Puzzle

## Prerequisite:
 - using pygame
 - 'viz_puzzles/n_queens' where the scripts are saved 
 - utilize the logic defined in 'leetcode/n_queens.py' as a base.

## scripts:

- Color: Support light/dark color thema (default: dark)

- main.py
  - read a number from 1 to 9 as a grid size
  - calls rendering function in render.py  by passing the solution algo and the number 

- render.py 
  - draws basic: 
    - grid n by n (n is provided by the calling functions) 
  - draws process of solution algo
    - render the queen in the cell
    - render the arrow to check 
  - flushes the border of grind when solving.
  - show the final solution. to render grids for multiple result accordingly.
  
- algos/
  - The script yields any delta, for instance, To add and remove a queen, To checking the collision.
