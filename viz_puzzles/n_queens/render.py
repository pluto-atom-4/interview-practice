"""Pygame renderer for N-Queens visualization."""

import pygame
import math
from typing import List, Tuple, Optional

from .config import Theme, THEMES


class NQueensRenderer:
    """Renders N-Queens puzzle solving animation."""

    def __init__(self, n: int, theme: str = 'dark', cell_size: int = 80):
        """
        Initialize the renderer.

        Args:
            n: Board size (N x N)
            theme: Theme name ('dark' or 'light')
            cell_size: Size of each cell in pixels
        """
        self.n = n
        self.theme: Theme = THEMES[theme]
        self.cell_size = cell_size
        self.margin = 20

        # Calculate window size
        self.board_size = n * cell_size
        self.width = self.board_size + 2 * self.margin
        self.height = self.board_size + 2 * self.margin + 60

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(f"N-Queens Visualization (N={n})")

        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)

        # State tracking
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.checking_cell: Optional[Tuple[int, int]] = None
        self.current_row = 0
        self.solutions = []
        self.solution_index = 0

        # Animation settings
        self.event_delay = 50  # ms between events
        self.last_event_time = 0

    def draw_board(self):
        """Draw the N x N chessboard."""
        for r in range(self.n):
            for c in range(self.n):
                x = self.margin + c * self.cell_size
                y = self.margin + r * self.cell_size

                # Alternate colors
                is_dark = (r + c) % 2 == 0
                color = self.theme.board_dark if is_dark else self.theme.board_light

                pygame.draw.rect(self.screen, color, (x, y, self.cell_size, self.cell_size))

                # Draw border
                pygame.draw.rect(
                    self.screen,
                    self.theme.grid_border,
                    (x, y, self.cell_size, self.cell_size),
                    2,
                )

    def draw_queen(self, row: int, col: int):
        """Draw a queen at the given position."""
        x = self.margin + col * self.cell_size + self.cell_size // 2
        y = self.margin + row * self.cell_size + self.cell_size // 2
        radius = self.cell_size // 3

        # Draw queen circle
        pygame.draw.circle(self.screen, self.theme.queen, (x, y), radius)
        pygame.draw.circle(self.screen, self.theme.queen_border, (x, y), radius, 3)

    def draw_checking_cell(self, row: int, col: int):
        """Highlight a cell being checked."""
        x = self.margin + col * self.cell_size
        y = self.margin + row * self.cell_size

        # Draw semi-transparent overlay
        overlay = pygame.Surface((self.cell_size, self.cell_size))
        overlay.set_alpha(100)
        overlay.fill(self.theme.checking)
        self.screen.blit(overlay, (x, y))

    def draw_queens(self):
        """Draw all queens currently on the board."""
        for r in range(self.n):
            for c in range(self.n):
                if self.board[r][c] == 'Q':
                    self.draw_queen(r, c)

    def draw_checking_highlight(self):
        """Draw highlight for the cell being checked."""
        if self.checking_cell:
            self.draw_checking_cell(self.checking_cell[0], self.checking_cell[1])

    def draw_info(self):
        """Draw information text."""
        info_y = self.margin + self.board_size + 10

        row_text = self.font_small.render(f"Row: {self.current_row}/{self.n}", True, self.theme.text)
        self.screen.blit(row_text, (self.margin, info_y))

        if self.solutions:
            sol_text = self.font_small.render(
                f"Solutions: {len(self.solutions)} (Showing #{self.solution_index + 1})",
                True,
                self.theme.text,
            )
            self.screen.blit(sol_text, (self.margin, info_y + 25))

    def process_event(self, event_type: str, *args):
        """Process an algorithm event."""
        if event_type == 'place':
            row, col = args
            self.board[row][col] = 'Q'
            self.current_row = row

        elif event_type == 'check':
            row, col = args
            self.checking_cell = (row, col)
            self.current_row = row

        elif event_type == 'remove':
            row, col = args
            self.board[row][col] = '.'

        elif event_type == 'solution':
            solution = args[0]
            self.solutions.append(solution)

    def render(self, event_generator):
        """
        Main rendering loop that processes events from the solver.

        Args:
            event_generator: Generator yielding algorithm events
        """
        running = True
        paused = False
        event_iter = iter(event_generator)
        last_event_time = 0
        animation_complete = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = not paused
                    elif event.key == pygame.K_LEFT and self.solution_index > 0:
                        self.solution_index -= 1
                    elif event.key == pygame.K_RIGHT and self.solution_index < len(self.solutions) - 1:
                        self.solution_index += 1

            # Process next event if not paused and enough time has elapsed
            current_time = pygame.time.get_ticks()
            if not paused and not animation_complete and (current_time - last_event_time) >= self.event_delay:
                try:
                    event = next(event_iter)
                    self.process_event(*event)
                    last_event_time = current_time
                except StopIteration:
                    # Animation complete, show solutions
                    animation_complete = True
                    if self.solutions:
                        self.show_solutions()

            # Clear screen
            self.screen.fill(self.theme.background)

            # Draw board
            self.draw_board()
            self.draw_checking_highlight()

            # Show current board state during solving
            if not self.solutions or len(self.solutions) == 0:
                self.draw_queens()
            else:
                # Show selected solution
                solution = self.solutions[self.solution_index]
                for r in range(self.n):
                    for c in range(self.n):
                        if solution[r][c] == 'Q':
                            self.draw_queen(r, c)

            self.draw_info()

            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS

        pygame.quit()

    def show_solutions(self):
        """Display all solutions."""
        print(f"\nFound {len(self.solutions)} solution(s) for {self.n}-Queens:")
        for idx, solution in enumerate(self.solutions, 1):
            print(f"\nSolution {idx}:")
            for row in solution:
                print(''.join(row))
