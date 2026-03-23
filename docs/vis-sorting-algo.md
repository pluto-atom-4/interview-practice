# Visualize sorting algo

## Prerequisite:
 - using pygame

## script structures:

- main.py
  - initializes the canvas
  - calls rendering function in render.py by passing the sorting algos 
    in the loop:

- render.py 
  - to draw basic: 
    - canvas, 
    - y: 0 axis line
    - x: 0 axis line
  - to draw process of sorting algo
    - box to represent the height is the value of each item, the width is fixed value 24 px as default 
    - gets the every single position change and call the function in render.py, so to update the box accordingly.    
  
- algos/
  - various sorting algo in the individual script. e.g. bubble_sort.py provide the Bubble Sort algo.
  - The script yields any delta for instance  comparing and swapping items while processing the sorting.
