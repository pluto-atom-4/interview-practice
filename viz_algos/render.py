"""
Rendering functions for sorting algorithm visualization.
Handles drawing canvas, axes, and array elements.
"""

import pygame


# Theme definitions
THEMES = {
    'light': {
        'BG_COLOR': (240, 240, 240),
        'AXIS_COLOR': (100, 100, 100),
        'DEFAULT_COLOR': (100, 150, 200),
        'COMPARE_COLOR': (255, 200, 0),
        'SWAP_COLOR': (200, 100, 100),
        'DONE_COLOR': (100, 200, 100),
        'TEXT_COLOR': (50, 50, 50),
    },
    'dark': {
        'BG_COLOR': (30, 30, 35),
        'AXIS_COLOR': (150, 150, 150),
        'DEFAULT_COLOR': (100, 200, 255),
        'COMPARE_COLOR': (255, 200, 50),
        'SWAP_COLOR': (255, 100, 100),
        'DONE_COLOR': (100, 255, 150),
        'TEXT_COLOR': (230, 230, 230),
    }
}

# Dimensions
BAR_WIDTH = 24
PADDING = 40
AXIS_WIDTH = 2


def draw_background(surface, theme='dark'):
    """Draw the background color."""
    colors = THEMES[theme]
    surface.fill(colors['BG_COLOR'])


def draw_axes(surface, width, height, theme='dark'):
    """Draw x and y axes."""
    colors = THEMES[theme]
    pygame.draw.line(
        surface,
        colors['AXIS_COLOR'],
        (PADDING, height - PADDING),
        (width - PADDING, height - PADDING),
        AXIS_WIDTH
    )
    pygame.draw.line(
        surface,
        colors['AXIS_COLOR'],
        (PADDING, PADDING),
        (PADDING, height - PADDING),
        AXIS_WIDTH
    )


def draw_bars(surface, arr, highlighted_indices=None, event_type=None, theme='dark'):
    """
    Draw bars representing array values.

    Args:
        surface: pygame surface
        arr: array of values to visualize
        highlighted_indices: list of indices to highlight
        event_type: 'compare', 'swap', or 'done' to determine color
        theme: 'light' or 'dark' theme
    """
    if highlighted_indices is None:
        highlighted_indices = []

    colors = THEMES[theme]
    width, height = surface.get_size()
    max_val = max(arr) if arr else 1
    usable_height = height - 2 * PADDING

    for i, val in enumerate(arr):
        x = PADDING + i * BAR_WIDTH
        bar_height = (val / max_val) * usable_height
        y = height - PADDING - bar_height

        # Determine color
        if i in highlighted_indices:
            if event_type == 'swap':
                color = colors['SWAP_COLOR']
            elif event_type == 'compare':
                color = colors['COMPARE_COLOR']
            elif event_type == 'done':
                color = colors['DONE_COLOR']
            else:
                color = colors['DEFAULT_COLOR']
        else:
            color = colors['DEFAULT_COLOR']

        pygame.draw.rect(surface, color, (x, y, BAR_WIDTH - 2, bar_height))
        pygame.draw.rect(surface, colors['AXIS_COLOR'], (x, y, BAR_WIDTH - 2, bar_height), 1)


def render_frame(surface, arr, highlighted_indices=None, event_type=None, theme='dark'):
    """
    Render a complete frame with axes and bars.

    Args:
        surface: pygame surface
        arr: array to visualize
        highlighted_indices: indices to highlight
        event_type: type of operation ('compare', 'swap', 'done')
        theme: 'light' or 'dark' theme
    """
    draw_background(surface, theme)
    width, height = surface.get_size()
    draw_axes(surface, width, height, theme)
    draw_bars(surface, arr, highlighted_indices, event_type, theme)
