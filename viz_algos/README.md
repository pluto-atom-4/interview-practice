# Sorting Algorithm Visualizer

A visual representation of sorting algorithms using pygame.

## Quick Start

From the project root directory:
```bash
python viz_algos/main.py
```

## Controls

- **Space**: Reset and restart the animation
- **T**: Toggle between light and dark theme
- **Q**: Close the application
- **Close Window**: Exit the application

## User Input

When you run the application, you'll be prompted to enter the number of items to sort (between 5 and 30). The app will generate a random array and visualize the sorting process.

## Features

### Current Implementation
- **Bubble Sort**: Visual step-by-step bubble sort with comparisons and swaps highlighted
- **Dynamic Array Size**: User can specify the number of items (5-30) to sort
- **Random Array Generation**: Each run generates a new random array
- **Theme Support**: Light and dark themes for comfortable viewing

### Visual Feedback (Light Theme)
- **Blue bars**: Default color for unsorted/sorted elements
- **Yellow bars**: Comparison operations (current pair being compared)
- **Red bars**: Swap operations (elements being swapped)
- **Green bars**: Sorting complete

### Visual Feedback (Dark Theme)
- **Bright Blue bars**: Default color for unsorted/sorted elements
- **Golden bars**: Comparison operations
- **Bright Red bars**: Swap operations
- **Bright Green bars**: Sorting complete

### Configuration

Adjust in `main.py`:
- `WINDOW_WIDTH`, `WINDOW_HEIGHT`: Window dimensions
- `FPS`: Animation speed (frames per second)
- `arr`: Test array for sorting

## Project Structure

```
viz_algos/
├── __init__.py
├── main.py          # Entry point and pygame loop
├── render.py        # Rendering functions (axes, bars)
├── algos/           # Sorting algorithms
│   ├── __init__.py
│   └── bubble_sort.py   # Bubble sort algorithm with event yields
└── README.md
```

## How It Works

1. **Algorithm Generator**: Each sorting algorithm yields events for comparisons and swaps
2. **Main Loop**: Pygame loop processes events and renders each frame
3. **Rendering**: Bars represent array values; color indicates operation type

## Future Enhancements

- Add more sorting algorithms (merge sort, quick sort, etc.)
- Add statistics (comparisons, swaps, time elapsed)
- Add speed controls
- Save/export visualization as video
