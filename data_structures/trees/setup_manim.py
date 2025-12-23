"""
Setup and Testing Script for Manim Animations
==============================================

Provides utilities to:
1. Check Manim installation
2. Generate all animations
3. Test individual animations
4. Create video compilations
"""

import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


class ManifAnimationSetup:
    """Setup and manage Manim animations for parsing trees."""

    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.manim_files = [
            "manim_level_order_parsing_tree.py",
            "manim_advanced_trees.py",
        ]
        self.scenes = {
            "manim_level_order_parsing_tree.py": [
                "TokenizationAnimation",
                "ShuntingYardAnimation",
                "TreeConstructionAnimation",
                "LevelOrderTraversalAnimation",
                "ExpressionEvaluationAnimation",
                "CompleteParsingSummary",
                "InteractiveExpressionParser",
            ],
            "manim_advanced_trees.py": [
                "TreeBuildingVisualization",
                "PrecedenceComparison",
                "LevelOrderAnimationAdvanced",
                "DynamicTreeGrowth",
                "ExpressionToTreeFlow",
            ],
        }

    def check_manim_installation(self) -> bool:
        """Check if Manim is installed and working."""
        print("Checking Manim installation...")

        try:
            result = subprocess.run(
                ["manim", "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                print(f"✓ Manim is installed: {result.stdout.strip()}")
                return True
            else:
                print("✗ Manim installation found but may have issues")
                print(f"  Error: {result.stderr}")
                return False

        except FileNotFoundError:
            print("✗ Manim is not installed")
            print("  Install with: pip install manim")
            return False
        except Exception as e:
            print(f"✗ Error checking Manim: {e}")
            return False

    def install_manim(self) -> bool:
        """Attempt to install Manim."""
        print("Attempting to install Manim...")

        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "manim"],
                capture_output=True,
                text=True,
                timeout=300,
            )

            if result.returncode == 0:
                print("✓ Manim installed successfully")
                return True
            else:
                print(f"✗ Failed to install Manim: {result.stderr}")
                return False

        except Exception as e:
            print(f"✗ Error installing Manim: {e}")
            return False

    def render_animation(
        self,
        filename: str,
        scene_name: str,
        quality: str = "ql",
        play: bool = True,
    ) -> bool:
        """Render a specific animation.

        Args:
            filename: Python file containing the scene
            scene_name: Name of the scene class
            quality: Quality setting (ql, qm, qh, qk)
            play: Whether to play after rendering

        Returns:
            True if successful, False otherwise
        """
        filepath = self.project_root / "data_structures" / "trees" / filename

        if not filepath.exists():
            print(f"✗ File not found: {filepath}")
            return False

        quality_flag = f"-{quality}"
        play_flag = "-p" if play else "-n"

        cmd = ["manim", play_flag, quality_flag, str(filepath), scene_name]

        print(f"Rendering {scene_name} from {filename}...")
        print(f"Command: {' '.join(cmd)}")

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=600,  # 10 minutes timeout
            )

            if result.returncode == 0:
                print(f"✓ Successfully rendered {scene_name}")
                return True
            else:
                print(f"✗ Failed to render {scene_name}")
                print(f"  Error: {result.stderr}")
                return False

        except subprocess.TimeoutExpired:
            print(f"✗ Rendering timed out for {scene_name}")
            return False
        except Exception as e:
            print(f"✗ Error rendering {scene_name}: {e}")
            return False

    def render_all_animations(self, quality: str = "ql", play: bool = False) -> dict:
        """Render all animations.

        Args:
            quality: Quality setting
            play: Whether to play after rendering

        Returns:
            Dictionary with results
        """
        results = {}

        for filename, scenes in self.scenes.items():
            results[filename] = {}

            for scene in scenes:
                print(f"\n{'=' * 60}")
                success = self.render_animation(filename, scene, quality, play)
                results[filename][scene] = success

        return results

    def get_render_commands(self) -> List[str]:
        """Get all render commands."""
        commands = []

        for filename, scenes in self.scenes.items():
            for scene in scenes:
                cmd = f"manim -pql data_structures/trees/{filename} {scene}"
                commands.append(cmd)

        return commands

    def print_setup_report(self):
        """Print detailed setup report."""
        print("\n" + "=" * 70)
        print("MANIM ANIMATION SETUP REPORT")
        print("=" * 70)

        # Check installation
        installed = self.check_manim_installation()

        if not installed:
            print("\nWould you like to install Manim now? (y/n)")
            response = input().strip().lower()
            if response == "y":
                self.install_manim()

        # Show available scenes
        print("\n" + "-" * 70)
        print("AVAILABLE ANIMATIONS:")
        print("-" * 70)

        total_scenes = 0
        for filename, scenes in self.scenes.items():
            print(f"\n{filename}:")
            for i, scene in enumerate(scenes, 1):
                print(f"  {i}. {scene}")
            total_scenes += len(scenes)

        print(f"\nTotal animations available: {total_scenes}")

        # Show render commands
        print("\n" + "-" * 70)
        print("RENDER COMMANDS:")
        print("-" * 70)

        commands = self.get_render_commands()
        print("\nQuick command to render all:")
        print("\n".join(commands[:3]))
        print(f"... and {len(commands) - 3} more")

        # Show instructions
        print("\n" + "-" * 70)
        print("QUICK START:")
        print("-" * 70)
        print("\n1. Render first animation:")
        print("   manim -pql data_structures/trees/manim_level_order_parsing_tree.py TokenizationAnimation")
        print("\n2. Render all animations:")
        print("   python -c 'from setup_manim import *; setup = ManifAnimationSetup(); setup.render_all_animations()'")
        print("\n3. Check quality options:")
        print("   -ql : Low quality (fastest)")
        print("   -qm : Medium quality")
        print("   -qh : High quality")
        print("   -qk : 4K quality (slowest)")


# Quick test functions

def test_tokenization_animation():
    """Quick test for tokenization animation."""
    print("Testing TokenizationAnimation...")
    setup = ManifAnimationSetup(".")
    return setup.render_animation(
        "manim_level_order_parsing_tree.py",
        "TokenizationAnimation",
        quality="ql",
        play=True,
    )


def test_all_basic_animations():
    """Test all basic animations."""
    print("Testing all basic animations...")
    setup = ManifAnimationSetup(".")
    results = setup.render_all_animations(quality="ql", play=False)

    print("\n" + "=" * 70)
    print("TEST RESULTS:")
    print("=" * 70)

    total = 0
    passed = 0

    for filename, scenes in results.items():
        print(f"\n{filename}:")
        for scene, success in scenes.items():
            status = "✓ PASS" if success else "✗ FAIL"
            print(f"  {status}: {scene}")
            total += 1
            if success:
                passed += 1

    print(f"\nTotal: {passed}/{total} passed")

    return passed == total


# Integration with level_order_parsing_tree

INTEGRATION_CODE = '''
# In your level_order_parsing_tree.py, add:

def generate_animations():
    """Generate Manim animations for this module."""
    from setup_manim import ManifAnimationSetup
    
    setup = ManifAnimationSetup()
    
    # Check installation
    if not setup.check_manim_installation():
        print("Installing Manim...")
        setup.install_manim()
    
    # Render animations
    print("Generating animations...")
    results = setup.render_all_animations(quality="ql")
    
    return results

if __name__ == "__main__":
    generate_animations()
'''


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Manim Animation Setup")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check Manim installation",
    )
    parser.add_argument(
        "--install",
        action="store_true",
        help="Install Manim",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Print setup report",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Test first animation",
    )
    parser.add_argument(
        "--test-all",
        action="store_true",
        help="Test all animations",
    )
    parser.add_argument(
        "--render-all",
        action="store_true",
        help="Render all animations",
    )
    parser.add_argument(
        "--quality",
        default="ql",
        choices=["ql", "qm", "qh", "qk"],
        help="Rendering quality",
    )

    args = parser.parse_args()

    setup = ManifAnimationSetup()

    if args.check:
        setup.check_manim_installation()
    elif args.install:
        setup.install_manim()
    elif args.report:
        setup.print_setup_report()
    elif args.test:
        test_tokenization_animation()
    elif args.test_all:
        test_all_basic_animations()
    elif args.render_all:
        results = setup.render_all_animations(quality=args.quality)
        print("\nRender complete!")
    else:
        setup.print_setup_report()

