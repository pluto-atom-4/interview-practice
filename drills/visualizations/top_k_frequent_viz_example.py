#!/usr/bin/env python
"""
Runner script for top_k_frequent_viz.py visualization.

This script renders the Top-K Frequent Elements visualization using the min-heap approach.
The visualization shows how the algorithm efficiently finds k most frequent elements
in O(n log k) time by maintaining a fixed-size heap.

Usage:
    python run_top_k_frequent_viz.py

Output:
    Renders animation to generated/media/ directory
"""

import subprocess
import sys
from pathlib import Path


def run_visualization():
    """Run the Top-K Frequent visualization using manim."""
    script_dir = Path(__file__).parent
    viz_script = script_dir / "top_k_frequent_viz.py"
    media_dir = script_dir.parent.parent / "generated" / "media"

    media_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "manim",
        "-qh",  # high quality
        "-p",   # preview after rendering
        "--media_dir", str(media_dir),
        str(viz_script),
        "TopKFrequentVisualization",
    ]

    try:
        print(f"Rendering visualization: {viz_script}")
        print(f"Output directory: {media_dir}")
        result = subprocess.run(cmd, check=True, capture_output=False)
        print(f"\n✓ SUCCESS: Visualization rendered to {media_dir}")
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"\n✗ ERROR: Failed rendering visualization: {e}")
        return 1
    except FileNotFoundError:
        print("✗ ERROR: Manim not found. Install with: pip install manim")
        return 1


if __name__ == "__main__":
    sys.exit(run_visualization())
