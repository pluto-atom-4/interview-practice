#!/usr/bin/env python
"""
Runner script for merge_sort_viz.py visualization.

This script renders the merge sort algorithm visualization using Manim.
The visualization shows the sorting process as a bar chart where:
- X-axis: position in the array
- Y-axis: value at that position
- Bars change color as they are sorted

Execution: python merge_sort_viz_runner.py
Output: Animated video saved to generated/media/videos/
"""

import subprocess
import sys
from pathlib import Path


def run_visualization():
    """Run the merge sort visualization using manim."""
    script_dir = Path(__file__).parent
    viz_script = script_dir / "merge_sort_viz.py"
    media_dir = script_dir.parent.parent / "generated" / "media"

    # Create media directory if it doesn't exist
    media_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "manim",
        "-qh",  # high quality (1080p)
        "-p",   # preview after rendering
        "--media_dir",
        str(media_dir),
        str(viz_script),
        "MergeSortVisualization",
    ]

    try:
        print("Rendering Merge Sort visualization...")
        print(f"Output directory: {media_dir}")
        result = subprocess.run(cmd, check=True, capture_output=False)
        print(f"\n✓ SUCCESS: Visualization rendered to {media_dir}")
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"\n✗ ERROR: Failed rendering visualization: {e}")
        return 1
    except FileNotFoundError:
        print("✗ ERROR: Manim not found.")
        print("Install with: pip install manim")
        return 1


if __name__ == "__main__":
    sys.exit(run_visualization())
