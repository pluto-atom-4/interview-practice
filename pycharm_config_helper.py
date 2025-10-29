#!/usr/bin/env python3
"""
Helper script to find Python executable paths for PyCharm configuration.
Run this script to get the exact paths you need for File Watchers setup.
"""

import os
import subprocess
import sys


def find_python_executable():
    """Find the current Python executable path."""
    return sys.executable


def find_black_executable():
    """Find black executable if installed."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "black", "--version"], capture_output=True, text=True
        )
        if result.returncode == 0:
            return f"{sys.executable} -m black"
        else:
            return "Black not found"
    except:
        return "Black not found"


def find_isort_executable():
    """Find isort executable if installed."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "isort", "--version"], capture_output=True, text=True
        )
        if result.returncode == 0:
            return f"{sys.executable} -m isort"
        else:
            return "isort not found"
    except:
        return "isort not found"


def main():
    print("=" * 60)
    print("PyCharm File Watchers Configuration Helper")
    print("=" * 60)
    print()

    python_path = find_python_executable()
    print(f"Python Executable Path: {python_path}")
    print()

    print("File Watcher Configuration:")
    print("-" * 30)
    print("For Black:")
    print(f"  Program: {python_path}")
    print(f"  Arguments: -m black $FilePath$")
    print()

    print("For isort:")
    print(f"  Program: {python_path}")
    print(f"  Arguments: -m isort $FilePath$")
    print()

    print("Tool Status:")
    print("-" * 15)
    black_status = find_black_executable()
    isort_status = find_isort_executable()
    print(f"Black: {black_status}")
    print(f"isort: {isort_status}")
    print()

    # Check if we're in the correct project directory
    if os.path.exists("pyproject.toml"):
        print("✅ Found pyproject.toml - configuration will be used")
    else:
        print("❌ No pyproject.toml found - tools will use default settings")

    print()
    print("Copy the paths above into your PyCharm File Watchers configuration!")


if __name__ == "__main__":
    main()
