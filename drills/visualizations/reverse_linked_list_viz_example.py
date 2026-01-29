#!/usr/bin/env python
"""
Runner script for reverse_linked_list_viz.py visualization.

This script renders the linked list reversal visualization using the three-pointer
iterative algorithm. The animation shows how prev, current, and nxt pointers work
together to reverse a linked list in O(n) time with O(1) space.

Usage:
    python reverse_linked_list_viz_example.py

Output:
    Animation saved to: generated/media/videos/1080p60/ReverseLinkedListVisualization.mp4
"""

import subprocess
import sys
from pathlib import Path


def run_visualization():
    """Run the visualization using manim."""
    script_dir = Path(__file__).parent
    viz_script = script_dir / "reverse_linked_list_viz.py"
    media_dir = script_dir.parent.parent / "generated" / "media"

    media_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "manim",
        "-qh",  # high quality
        "-p",   # preview
        "--media_dir", str(media_dir),
        str(viz_script),
        "ReverseLinkedListVisualization",
    ]

    try:
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
