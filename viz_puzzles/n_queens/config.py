"""Theme and color configuration for N-Queens visualization."""

from dataclasses import dataclass


@dataclass
class Theme:
    """Color theme for the visualization."""

    background: tuple  # RGB
    board_dark: tuple  # Dark square
    board_light: tuple  # Light square
    queen: tuple  # Queen color
    queen_border: tuple  # Queen border
    checking: tuple  # Cell being checked
    valid: tuple  # Valid placement highlight
    invalid: tuple  # Invalid placement highlight
    text: tuple  # Text color
    grid_border: tuple  # Grid border


# Dark theme (default)
DARK_THEME = Theme(
    background=(30, 30, 30),
    board_dark=(50, 50, 50),
    board_light=(100, 100, 100),
    queen=(255, 215, 0),  # Gold
    queen_border=(200, 170, 0),
    checking=(255, 100, 100),  # Red highlight for checking
    valid=(100, 255, 100),  # Green for valid
    invalid=(255, 100, 100),  # Red for invalid
    text=(255, 255, 255),
    grid_border=(200, 200, 200),
)

# Light theme
LIGHT_THEME = Theme(
    background=(240, 240, 240),
    board_dark=(180, 140, 70),  # Brown
    board_light=(240, 217, 181),  # Light tan
    queen=(255, 100, 0),  # Orange
    queen_border=(200, 70, 0),
    checking=(255, 150, 150),
    valid=(150, 255, 150),
    invalid=(255, 150, 150),
    text=(20, 20, 20),
    grid_border=(100, 100, 100),
)

THEMES = {
    'dark': DARK_THEME,
    'light': LIGHT_THEME,
}
