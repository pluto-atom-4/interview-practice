"""
Tree Visualization Examples
===========================

Demonstrates how to visualize tree structures using visualize_tree module.
Shows examples with 3-level trees using both JSON and Tree objects.
"""

import json

from data_structures.trees.tree import Tree, TreeNode
from data_structures.trees.visualize_tree import (
    tree_to_json,
    visualize_tree_json,
    visualize_tree_object,
)


def example_1_json_dict_3level():
    """Example 1: Visualize a 3-level tree from JSON dictionary."""
    print("=" * 60)
    print("Example 1: 3-Level Tree from JSON Dictionary")
    print("=" * 60)

    tree_json = {
        "value": "CEO",
        "children": [
            {
                "value": "VP Engineering",
                "children": [
                    {
                        "value": "Engineering Manager 1",
                        "children": [
                            {"value": "Engineer 1", "children": []},
                            {"value": "Engineer 2", "children": []},
                            {"value": "Engineer 3", "children": []},
                        ]
                    },
                    {
                        "value": "Engineering Manager 2",
                        "children": [
                            {"value": "Engineer 4", "children": []},
                            {"value": "Engineer 5", "children": []},
                        ]
                    },
                ]
            },
            {
                "value": "VP Sales",
                "children": [
                    {
                        "value": "Sales Manager 1",
                        "children": [
                            {"value": "Sales Rep 1", "children": []},
                            {"value": "Sales Rep 2", "children": []},
                        ]
                    },
                    {
                        "value": "Sales Manager 2",
                        "children": [
                            {"value": "Sales Rep 3", "children": []},
                        ]
                    },
                ]
            },
            {
                "value": "VP Operations",
                "children": [
                    {
                        "value": "Operations Manager",
                        "children": [
                            {"value": "Ops Specialist 1", "children": []},
                            {"value": "Ops Specialist 2", "children": []},
                            {"value": "Ops Specialist 3", "children": []},
                        ]
                    },
                ]
            },
        ]
    }

    print("\nJSON Structure:")
    print(json.dumps(tree_json, indent=2))

    print("\nVisualizing tree...")
    visualize_tree_json(
        tree_json,
        title="Organization Structure (3-Level Hierarchy)",
        figsize=(14, 10),
    )


def example_2_json_string_3level():
    """Example 2: Visualize a 3-level tree from JSON string."""
    print("\n" + "=" * 60)
    print("Example 2: 3-Level Tree from JSON String")
    print("=" * 60)

    tree_json_str = """{
        "value": "Root",
        "children": [
            {
                "value": "Branch A",
                "children": [
                    {
                        "value": "Leaf A1",
                        "children": []
                    },
                    {
                        "value": "Leaf A2",
                        "children": []
                    },
                    {
                        "value": "Leaf A3",
                        "children": []
                    }
                ]
            },
            {
                "value": "Branch B",
                "children": [
                    {
                        "value": "Leaf B1",
                        "children": []
                    },
                    {
                        "value": "Leaf B2",
                        "children": []
                    }
                ]
            },
            {
                "value": "Branch C",
                "children": [
                    {
                        "value": "Leaf C1",
                        "children": []
                    }
                ]
            }
        ]
    }"""

    print("\nJSON String:")
    print(tree_json_str)

    print("\nVisualizing tree from JSON string...")
    visualize_tree_json(
        tree_json_str,
        title="Simple 3-Level Tree from JSON String",
        figsize=(12, 8),
    )


def example_3_tree_object_3level():
    """Example 3: Visualize a 3-level tree using Tree object."""
    print("\n" + "=" * 60)
    print("Example 3: 3-Level Tree Object")
    print("=" * 60)

    # Level 0: Root
    root = TreeNode("File System")

    # Level 1: Directories
    home_dir = TreeNode("home")
    var_dir = TreeNode("var")
    etc_dir = TreeNode("etc")

    root.add_child(home_dir)
    root.add_child(var_dir)
    root.add_child(etc_dir)

    # Level 2: Subdirectories under home
    user_dir = TreeNode("user")
    documents_dir = TreeNode("documents")
    home_dir.add_child(user_dir)
    home_dir.add_child(documents_dir)

    # Level 2: Subdirectories under var
    log_dir = TreeNode("log")
    cache_dir = TreeNode("cache")
    var_dir.add_child(log_dir)
    var_dir.add_child(cache_dir)

    # Level 2: Subdirectories under etc
    config_dir = TreeNode("config")
    etc_dir.add_child(config_dir)

    # Create Tree object
    tree = Tree(root)

    # Display tree structure
    print("\nTree Structure:")
    print(tree)

    # Convert to JSON for inspection
    print("\nTree as JSON:")
    tree_json = tree_to_json(tree)
    print(json.dumps(tree_json, indent=2))

    # Visualize
    print("\nVisualizing tree...")
    visualize_tree_object(tree, title="File System Hierarchy", figsize=(12, 8))


def example_4_numeric_tree_3level():
    """Example 4: Visualize a 3-level tree with numeric values (binary tree structure)."""
    print("\n" + "=" * 60)
    print("Example 4: 3-Level Binary Tree with Numeric Values")
    print("=" * 60)

    # Level 0: Root
    root = TreeNode(1)

    # Level 1
    left_child = TreeNode(2)
    right_child = TreeNode(3)
    root.add_child(left_child)
    root.add_child(right_child)

    # Level 2
    left_child.add_child(TreeNode(4))
    left_child.add_child(TreeNode(5))
    right_child.add_child(TreeNode(6))
    right_child.add_child(TreeNode(7))

    # Create Tree object
    tree = Tree(root)

    # Display tree structure
    print("\nTree Structure:")
    print(tree)

    # Display traversals
    print(f"\nPreorder traversal:   {list(tree.preorder())}")
    print(f"Postorder traversal:  {list(tree.postorder())}")
    print(f"Level-order traversal: {list(tree.level_order())}")

    # Visualize
    print("\nVisualizing tree...")
    visualize_tree_object(
        tree, title="Binary Tree Structure (1-7)", figsize=(12, 8)
    )


def example_5_wide_tree_3level():
    """Example 5: Visualize a 3-level wide tree (many children per node)."""
    print("\n" + "=" * 60)
    print("Example 5: 3-Level Wide Tree")
    print("=" * 60)

    # Level 0: Root
    root = TreeNode("Company")

    # Level 1: Multiple departments
    departments = [
        "Engineering",
        "Sales",
        "Marketing",
        "HR",
        "Finance",
    ]
    dept_nodes = {}
    for dept in departments:
        dept_node = TreeNode(dept)
        root.add_child(dept_node)
        dept_nodes[dept] = dept_node

    # Level 2: Teams within each department
    team_assignments = {
        "Engineering": ["Backend Team", "Frontend Team", "DevOps Team"],
        "Sales": ["Enterprise", "SMB", "Startups"],
        "Marketing": ["Content", "Digital", "Events"],
        "HR": ["Recruitment", "Operations"],
        "Finance": ["Accounting", "Planning"],
    }

    for dept, teams in team_assignments.items():
        for team in teams:
            team_node = TreeNode(team)
            dept_nodes[dept].add_child(team_node)

    # Create Tree object
    tree = Tree(root)

    # Display tree structure
    print("\nTree Structure:")
    print(tree)

    # Visualize
    print("\nVisualizing tree...")
    visualize_tree_object(
        tree, title="Company Structure (Wide 3-Level Tree)", figsize=(14, 10)
    )


def example_6_convert_json_to_tree():
    """Example 6: Convert JSON to Tree object and visualize."""
    print("\n" + "=" * 60)
    print("Example 6: Convert JSON to Tree Object")
    print("=" * 60)

    # Start with JSON
    tree_json = {
        "value": "Continents",
        "children": [
            {
                "value": "Asia",
                "children": [
                    {"value": "India", "children": []},
                    {"value": "Japan", "children": []},
                    {"value": "China", "children": []},
                ]
            },
            {
                "value": "Europe",
                "children": [
                    {"value": "Germany", "children": []},
                    {"value": "France", "children": []},
                ]
            },
            {
                "value": "North America",
                "children": [
                    {"value": "USA", "children": []},
                    {"value": "Canada", "children": []},
                    {"value": "Mexico", "children": []},
                ]
            },
        ]
    }

    print("\nOriginal JSON:")
    print(json.dumps(tree_json, indent=2))

    # Convert JSON to Tree (manually for demonstration)
    def json_to_tree(json_node):
        """Helper function to convert JSON to Tree object."""
        node = TreeNode(json_node["value"])
        for child_json in json_node.get("children", []):
            node.add_child(json_to_tree(child_json))
        return node

    tree = Tree(json_to_tree(tree_json))

    print("\nTree Object Created:")
    print(tree)

    # Visualize
    print("\nVisualizing tree...")
    visualize_tree_object(tree, title="Geographic Hierarchy (3-Level)", figsize=(12, 8))


if __name__ == "__main__":
    print("\n" + "#" * 60)
    print("# Tree Visualization Examples - 3-Level Trees")
    print("#" * 60)

    # Run all examples
    example_1_json_dict_3level()
    example_2_json_string_3level()
    example_3_tree_object_3level()
    example_4_numeric_tree_3level()
    example_5_wide_tree_3level()
    example_6_convert_json_to_tree()

    print("\n" + "#" * 60)
    print("# All examples completed!")
    print("#" * 60 + "\n")

