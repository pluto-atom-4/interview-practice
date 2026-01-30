#!/usr/bin/env python
"""
Runner script for first_non_repeating_char_viz.py visualization.

This script renders the first non-repeating character algorithm visualization
using Manim, demonstrating the two-pass hash table approach with visual
frequency counting and search phases.

Usage:
    python first_non_repeating_char_viz_example.py

Output:
    Rendered video saved to generated/media/videos/
"""

import subprocess
import sys
from pathlib import Path


def run_visualization():
    """Run the visualization using manim."""
    script_dir = Path(__file__).parent
    viz_script = script_dir / "first_non_repeating_char_viz.py"
    media_dir = script_dir.parent.parent / "generated" / "media"

    media_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "manim",
        "-qh",  # high quality
        "-p",   # preview
        "--media_dir",
        str(media_dir),
        str(viz_script),
        "FirstNonRepeatingCharViz",
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
