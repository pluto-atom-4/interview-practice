#!/usr/bin/env python
"""
Runner script for single_non_duplicate_viz.py visualization.

This script renders the XOR bitwise operation visualization showing how to find
a single non-duplicate number by XORing all array elements together.

Usage:
    python single_non_duplicate_viz_example.py

The script generates two visualizations:
1. SingleNonDuplicateVisualization - Main animation showing step-by-step XOR
2. SingleNonDuplicateVisualizationExtended - Extended view of XOR properties

Output:
    Rendered videos saved to generated/media/videos/
"""

import subprocess
import sys
from pathlib import Path


def run_visualization(scene_name="SingleNonDuplicateVisualization"):
    """
    Run the visualization using manim.

    Args:
        scene_name: Name of the Scene class to render (default: main visualization)

    Returns:
        Exit code from manim command
    """
    script_dir = Path(__file__).parent
    viz_script = script_dir / "single_non_duplicate_viz.py"
    media_dir = script_dir.parent.parent / "generated" / "media"

    # Create media directory if it doesn't exist
    media_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "manim",
        "-qh",  # high quality
        "-p",   # preview after rendering
        "--media_dir",
        str(media_dir),
        str(viz_script),
        scene_name,
    ]

    try:
        print(f"Rendering {scene_name}...")
        result = subprocess.run(cmd, check=True, capture_output=False)
        print(f"\n✓ SUCCESS: Visualization rendered to {media_dir}")
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"\n✗ ERROR: Failed rendering visualization: {e}")
        return 1
    except FileNotFoundError:
        print("✗ ERROR: Manim not found. Install with: pip install manim")
        return 1


def main():
    """Render both visualizations."""
    # Render main visualization
    exit_code = run_visualization("SingleNonDuplicateVisualization")
    if exit_code != 0:
        return exit_code

    # Optionally render extended visualization (uncomment to enable)
    # print("\n" + "=" * 60)
    # exit_code = run_visualization("SingleNonDuplicateVisualizationExtended")
    # if exit_code != 0:
    #     return exit_code

    print("\n" + "=" * 60)
    print("All visualizations completed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
