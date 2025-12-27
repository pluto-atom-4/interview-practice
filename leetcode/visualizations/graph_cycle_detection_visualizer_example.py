import json
import subprocess
import sys
from pathlib import Path


def run_cycle_visualizer(edges, n):
    """
    Launch the Manim visualizer and pass graph data via environment variables.
    The visualizer script will read these values at runtime.
    """

    # Convert data to JSON strings
    edges_json = json.dumps(edges)
    n_json = json.dumps(n)

    env = {
        **os.environ,
        "GRAPH_EDGES": edges_json,
        "GRAPH_N": n_json,
    }

    script_path = Path(__file__).parent / "graph_cycle_detection_visualizer.py"

    cmd = [
        "manim",
        "-pqh",
        str(script_path),
        "GraphCycleDetectionVisualizer",
        "--media_dir",
        str(Path(__file__).parents[2] / "generated" / "media"),
    ]

    print("Running Manim visualizer...")
    subprocess.run(cmd, env=env)


if __name__ == "__main__":
    import os

    # Example graph with a cycle
    edges = [(0, 1), (1, 2), (2, 0)]
    n = 3

    run_cycle_visualizer(edges, n)
