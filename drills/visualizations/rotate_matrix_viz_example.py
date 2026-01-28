#!/usr/bin/env python
"""
Runner script for rotate_matrix_viz.py visualization.

This script renders the matrix rotation 90-degree clockwise algorithm visualization
using the coordinate transformation formula: rotated[c][rows - 1 - r] = matrix[r][c].

The visualization shows the step-by-step transformation of a 3×3 matrix with
element-by-element animation and coordinate mapping arrows.
"""

import subprocess
import sys
from pathlib import Path


def run_visualization():
    """Run the matrix rotation visualization using manim."""

    # Get the directory of this script
    script_dir = Path(__file__).parent
    viz_script = script_dir / "rotate_matrix_viz.py"
    media_dir = script_dir.parent.parent / "generated" / "media"

    # Ensure media directory exists
    media_dir.mkdir(parents=True, exist_ok=True)

    print(f"Rendering Matrix Rotation Visualization...")
    print(f"Output directory: {media_dir}")
    print()

    # Run manim command directly
    # -qh: high quality
    # -p: preview (open the result)
    # Using direct manim command to avoid RuntimeWarning from -m module flag
    cmd = [
        "manim",
        "-qh",
        "-p",
        "--media_dir",
        str(media_dir),
        str(viz_script),
        "MatrixRotationVisualization",
    ]

    try:
        result = subprocess.run(cmd, check=True, capture_output=False)
        print()
        print("SUCCESS: Visualization rendered successfully!")
        print(f"Location: {media_dir}")
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Failed rendering visualization: {e}")
        return 1
    except FileNotFoundError:
        print("ERROR: Manim not found. Please install it with: pip install manim")
        return 1


if __name__ == "__main__":
    sys.exit(run_visualization())
