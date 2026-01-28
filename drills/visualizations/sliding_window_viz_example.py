#!/usr/bin/env python
"""
Runner script for sliding_window_viz.py visualization.

This script renders the sliding window two-pointer algorithm visualization
for finding the longest substring without repeating characters.

The visualization shows the process with input "abcabcbb" and expected result "abc".
"""

import subprocess
import sys
from pathlib import Path


def run_visualization():
    """Run the sliding window visualization using manim."""

    # Get the directory of this script
    script_dir = Path(__file__).parent
    viz_script = script_dir / "sliding_window_viz.py"
    media_dir = script_dir.parent.parent / "generated" / "media"

    # Ensure media directory exists
    media_dir.mkdir(parents=True, exist_ok=True)

    print(f"Rendering Sliding Window Visualization...")
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
        "SlidingWindowVisualization",
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
