"""
Main application for sorting algorithm visualization using pygame.
"""

import pygame
import sys
import random
import os

# Add parent directory to path to support running as script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from viz_algos.render import render_frame
from viz_algos.algos.bubble_sort import bubble_sort
from viz_algos.algos.merge_sort import merge_sort


# Configuration
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 10  # Frames per second for animation


def get_user_input():
    """Get array size and algorithm choice from user input."""
    while True:
        try:
            algo = input("Choose sorting algorithm (1=Bubble Sort, 2=Merge Sort): ")
            algo = int(algo)
            if algo not in [1, 2]:
                print("Please enter 1 or 2.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        while True:
            try:
                size = input("Enter number of items to sort (5-30): ")
                size = int(size)
                if 5 <= size <= 30:
                    return algo, size
                else:
                    print("Please enter a number between 5 and 30.")
            except ValueError:
                print("Please enter a valid number.")


def generate_array(size):
    """Generate a random array of given size."""
    return [random.randint(10, 100) for _ in range(size)]


def main():
    """Initialize and run the visualization."""
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    # Get user input for algorithm and array size
    algo_choice, array_size = get_user_input()
    arr = generate_array(array_size)

    # Select algorithm and set caption
    if algo_choice == 1:
        sorter = bubble_sort(arr)
        algo_name = "Bubble Sort"
    else:
        sorter = merge_sort(arr)
        algo_name = "Merge Sort"

    pygame.display.set_caption(f"Sorting Algorithm Visualizer - {algo_name}")

    # Theme management
    theme = 'dark'
    themes = ['light', 'dark']

    current_event = None
    done = False

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Reset and restart
                    if algo_choice == 1:
                        sorter = bubble_sort(arr)
                    else:
                        sorter = merge_sort(arr)
                    current_event = None
                    done = False
                elif event.key == pygame.K_t:
                    # Toggle theme
                    current_idx = themes.index(theme)
                    theme = themes[(current_idx + 1) % len(themes)]
                elif event.key == pygame.K_q:
                    # Close the window
                    running = False

        if not done:
            try:
                current_event = next(sorter)
            except StopIteration:
                done = True

        # Render
        if current_event:
            render_frame(
                screen,
                current_event['array'],
                current_event['indices'],
                current_event['type'],
                theme
            )
        else:
            render_frame(screen, arr, theme=theme)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
