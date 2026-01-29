"""
## Operation Overview

Visualization of the Count Islands algorithm that identifies connected components
in a 2D grid using BFS with a 4-directional connectivity pattern.

Shows the step-by-step transformation using Breadth-First Search (BFS):
- Original grid with land (1) and water (0) cells
- BFS traversal from each unvisited land cell
- Visited tracking matrix
- Island counter incrementing as each connected component completes

Example with concrete values:
Input: [[1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 0]]
Output: 3 islands

Visualizes:
1. Original grid layout with land (1) and water (0) cells
2. Visited tracking matrix updating in real-time
3. BFS queue showing cells waiting for exploration
4. Color-coded traversal highlighting current exploration path
5. Island counter incrementing as each component completes
"""

from manim import (  # Colors; Directions; Shapes; Animations; Special
    BLACK,
    BLUE,
    DOWN,
    GRAY,
    GREEN,
    LEFT,
    ORANGE,
    ORIGIN,
    PURPLE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    AnimationGroup,
    Arrow,
    Create,
    FadeIn,
    FadeOut,
    Indicate,
    Line,
    Rectangle,
    Scene,
    Text,
    Transform,
    VGroup,
    Write,
    config,
)

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_rate = 30


class CountIslandsVisualization(Scene):
    """
    Visualization of the Count Islands algorithm using BFS.

    Shows how BFS explores connected components from an unvisited land cell,
    marking visited cells, and counting each complete exploration as one island.
    Demonstrates the algorithm's logic with real-time queue management, visited
    tracking, and visual color-coding of exploration progress.
    """

    def construct(self):
        # Scene Layout Strategy
        # - Original grid on LEFT showing land (1, green) and water (0, gray)
        # - Visited matrix in CENTER showing True/False as the algorithm progresses
        # - BFS queue on RIGHT displaying cells waiting for exploration
        # - Island counter at BOTTOM showing incremental count

        # Color Scheme
        # - GREEN: Land cells (value = 1)
        # - GRAY: Water cells (value = 0)
        # - YELLOW: Currently processing cell in BFS
        # - ORANGE: Cell in the BFS queue (waiting)
        # - BLUE: Already visited land cell
        # - RED: Island counter highlight

        # Animation Flow
        # 1. Title and problem setup (1s)
        # 2. Grid and visited matrix initialization (1s)
        # 3. Main loop: scan grid for unvisited land cells (2s)
        # 4. BFS exploration for each island: queue management and traversal (5-10s per island)
        # 5. Island counter increment (0.5s)
        # 6. Summary with final island count (1s)

        # ===== TITLE AND SETUP =====
        title = Text("Count Islands - BFS with Visited Matrix", font_size=32)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Problem description
        problem = Text("4-directional connectivity in 2D grid", font_size=24)
        problem.next_to(title, DOWN, buff=0.3)
        self.play(Write(problem))
        self.wait(0.3)

        # ===== GRID SETUP =====
        # Test grid: 4x4
        grid = [[1, 1, 0, 0],
                [1, 0, 0, 1],
                [0, 0, 1, 1],
                [0, 0, 0, 0]]

        rows, cols = len(grid), len(grid[0])

        # Create grid visualization
        grid_group = VGroup()
        grid_cells = []
        cell_size = 0.5
        grid_spacing = 0.6

        # Position grid on LEFT side
        grid_start_pos = ORIGIN + LEFT * 4 + UP * 1.5

        for r in range(rows):
            row_cells = []
            for c in range(cols):
                # Create cell rectangle
                cell = Rectangle(width=cell_size, height=cell_size, stroke_width=2)
                cell_pos = grid_start_pos + RIGHT * (c * grid_spacing) + DOWN * (r * grid_spacing)
                cell.move_to(cell_pos)

                # Color and label based on grid value
                value = grid[r][c]
                if value == 1:
                    cell.set_fill(GREEN, opacity=0.7)
                    cell.set_stroke(BLACK, width=2)
                else:
                    cell.set_fill(GRAY, opacity=0.3)
                    cell.set_stroke(BLACK, width=2)

                # Add text label
                label = Text(str(value), font_size=16)
                label.move_to(cell.get_center())

                grid_group.add(cell)
                grid_group.add(label)
                row_cells.append((cell, label))

            grid_cells.append(row_cells)

        # Grid label
        grid_label = Text("Original Grid", font_size=18, color=BLUE)
        grid_label.next_to(grid_group, UP, buff=0.3)

        self.play(Create(grid_group), Write(grid_label))
        self.wait(1)

        # ===== VISITED MATRIX =====
        visited_group = VGroup()
        visited_cells = []
        visited_start_pos = ORIGIN + UP * 1.5

        visited = [[False] * cols for _ in range(rows)]

        for r in range(rows):
            row_visited = []
            for c in range(cols):
                # Create visited cell
                v_cell = Rectangle(width=0.4, height=0.4, stroke_width=1.5)
                v_pos = visited_start_pos + RIGHT * (c * 0.5) + DOWN * (r * 0.5)
                v_cell.move_to(v_pos)
                v_cell.set_fill(WHITE, opacity=0.5)
                v_cell.set_stroke(BLACK, width=1)

                # Label: F for False
                v_label = Text("F", font_size=12)
                v_label.move_to(v_cell.get_center())

                visited_group.add(v_cell)
                visited_group.add(v_label)
                row_visited.append((v_cell, v_label))

            visited_cells.append(row_visited)

        # Visited matrix label
        visited_label = Text("Visited Matrix", font_size=18, color=BLUE)
        visited_label.next_to(visited_group, UP, buff=0.3)

        self.play(Create(visited_group), Write(visited_label))
        self.wait(0.5)

        # ===== ISLAND COUNTER =====
        counter_label = Text("Islands: ", font_size=20)
        counter_label.to_edge(DOWN)
        counter_value = Text("0", font_size=20, color=RED)
        counter_value.next_to(counter_label, RIGHT, buff=0.2)

        self.play(Write(counter_label), Write(counter_value))
        self.wait(0.5)

        # ===== ALGORITHM EXECUTION =====
        island_count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Scan grid for unvisited land cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    # Found start of new island - highlight it
                    start_cell, start_label = grid_cells[r][c]
                    self.play(Indicate(start_cell, color=YELLOW, scale_factor=1.3))
                    self.wait(0.3)

                    # BFS from this cell
                    from collections import deque
                    queue = deque()
                    queue.append((r, c))
                    visited[r][c] = True

                    # Update visited matrix
                    v_cell, v_label = visited_cells[r][c]
                    self.play(
                        Transform(v_label, Text("T", font_size=12)),
                        v_cell.animate.set_fill(BLUE, opacity=0.7)
                    )

                    # BFS exploration
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        curr_cell, _ = grid_cells[curr_r][curr_c]

                        # Highlight current cell as being processed
                        self.play(Indicate(curr_cell, color=ORANGE, scale_factor=1.2))
                        self.wait(0.2)

                        # Explore 4 directions
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc

                            # Check bounds and if land and not visited
                            if (0 <= nr < rows and 0 <= nc < cols and
                                not visited[nr][nc] and grid[nr][nc] == 1):

                                visited[nr][nc] = True
                                queue.append((nr, nc))

                                # Update visited matrix
                                v_cell_new, v_label_new = visited_cells[nr][nc]
                                neighbor_cell, _ = grid_cells[nr][nc]

                                # Draw arrow showing connection
                                arrow = Arrow(
                                    curr_cell.get_center(),
                                    neighbor_cell.get_center(),
                                    color=PURPLE,
                                    stroke_width=2
                                )

                                self.play(
                                    Create(arrow),
                                    neighbor_cell.animate.set_fill(BLUE, opacity=0.7),
                                    Transform(v_label_new, Text("T", font_size=12)),
                                    v_cell_new.animate.set_fill(BLUE, opacity=0.7),
                                    run_time=0.3
                                )

                                # Clean up arrow
                                self.play(FadeOut(arrow), run_time=0.2)

                        self.wait(0.2)

                    # Island found - increment counter
                    island_count += 1
                    new_counter = Text(str(island_count), font_size=20, color=RED)
                    self.play(
                        Transform(counter_value, new_counter),
                        Indicate(counter_label, color=RED, scale_factor=1.2)
                    )
                    self.wait(0.5)

        # ===== SUMMARY =====
        self.wait(0.5)
        summary = Text(f"Total Islands Found: {island_count}", font_size=28, color=GREEN)
        summary.to_edge(DOWN).shift(UP * 2)

        self.play(Write(summary))
        self.wait(1)

        # Final frame info
        complexity_info = Text(
            f"Time: O(rows×cols)  Space: O(rows×cols)",
            font_size=16,
            color=GRAY
        )
        complexity_info.next_to(summary, DOWN, buff=0.5)
        self.play(Write(complexity_info))
        self.wait(1.5)
