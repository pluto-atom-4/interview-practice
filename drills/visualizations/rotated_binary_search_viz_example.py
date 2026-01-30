#!/usr/bin/env python
"""
Runner script for rotated_binary_search_viz.py visualization.

This script renders the rotated binary search visualization showing how the
modified binary search algorithm detects sorted halves and narrows the search
space to locate a target in O(log n) time.

Usage:
    python rotated_binary_search_viz_runner.py
"""

import subprocess
import sys
from pathlib import Path


def run_visualization():
    """Run the visualization using manim."""
    script_dir = Path(__file__).parent
    viz_script = script_dir / "rotated_binary_search_viz.py"
    media_dir = script_dir.parent / "generated" / "media"

    media_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "manim",
        "-qh",  # high quality
        "-p",   # preview after rendering
        "--media_dir", str(media_dir),
        str(viz_script),
        "RotatedBinarySearchVisualization",
    ]

    try:
        result = subprocess.run(cmd, check=True, capture_output=False)
        print(f"\n✓ SUCCESS: Visualization rendered to {media_dir}")
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"✗ ERROR: Failed rendering visualization: {e}")
        return 1
    except FileNotFoundError:
        print("✗ ERROR: Manim not found. Install with: pip install manim")
        return 1

if __name__ == "__main__":
    sys.exit(run_visualization())
