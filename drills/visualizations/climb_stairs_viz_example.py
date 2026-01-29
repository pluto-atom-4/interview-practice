#!/usr/bin/env python
"""
Runner script for climb_stairs_viz.py visualization.

This script renders the Climb Stairs visualization showing space-optimized
dynamic programming using a rolling window approach.

Execution:
    python climb_stairs_viz_example.py

Output:
    Animation saved to: generated/media/videos/
"""

import subprocess
import sys
from pathlib import Path


def run_visualization():
    """Run the Climb Stairs visualization using manim."""
    script_dir = Path(__file__).parent
    viz_script = script_dir / "climb_stairs_viz.py"
    media_dir = script_dir.parent.parent / "generated" / "media"

    media_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "manim",
        "-qh",  # high quality
        "-p",   # preview
        "--media_dir",
        str(media_dir),
        str(viz_script),
        "ClimbStairsVisualization",
    ]

    try:
        result = subprocess.run(cmd, check=True, capture_output=False)
        print(f"\n✓ SUCCESS: Climb Stairs visualization rendered to {media_dir}")
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"\n✗ ERROR: Failed rendering visualization: {e}")
        return 1
    except FileNotFoundError:
        print(
            "\n✗ ERROR: Manim not found. Install with: pip install manim"
        )
        return 1


if __name__ == "__main__":
    sys.exit(run_visualization())
