"""
Convenience wrapper to run the Skip List visualization.

Usage:
    python skip_list_viz_runner.py
"""

import subprocess
import sys
from pathlib import Path


def main():
    script_path = Path(__file__).parent / "skip_list_viz.py"
    scene_name = "SkipListVisualization"

    cmd = [
        "manim",
        str(script_path),
        scene_name,
        "-p",   # preview
        "-qL",  # low quality for fast rendering
    ]

    print("Running Manim visualization...")
    print(" ".join(cmd))

    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        print("Error: Manim is not installed or not on PATH.")
        sys.exit(1)


if __name__ == "__main__":
    main()
