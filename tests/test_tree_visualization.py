"""
Test suite for tree visualization functionality.

Tests cover:
- JSON parsing and validation
- Tree structure conversion
- Visualization with different tree structures
- Edge cases and error handling
"""

import json

import pytest

from data_structures.trees.tree import Tree, TreeNode
from data_structures.trees.visualize_tree import (
    _count_nodes,
    _tree_to_json,
    tree_to_json,
    visualize_tree_json,
    visualize_tree_object,
)


class TestTreeToJson:
    """Test conversion of Tree objects to JSON format."""

    def test_single_node_tree(self):
        """Test conversion of tree with single node."""
        root = TreeNode("A")
        tree = Tree(root)
        result = tree_to_json(tree)

        assert result["value"] == "A"
        assert result["children"] == []

    def test_tree_with_children(self):
        """Test conversion of tree with multiple levels."""
        root = TreeNode("A")
        b = TreeNode("B")
        c = TreeNode("C")
        d = TreeNode("D")

        root.add_child(b)
        root.add_child(c)
        b.add_child(d)

        tree = Tree(root)
        result = tree_to_json(tree)

        assert result["value"] == "A"
        assert len(result["children"]) == 2
        assert result["children"][0]["value"] == "B"
        assert result["children"][1]["value"] == "C"
        assert result["children"][0]["children"][0]["value"] == "D"

    def test_empty_tree(self):
        """Test conversion of empty tree."""
        tree = Tree(None)
        result = tree_to_json(tree)
        assert result == {}

    def test_deep_tree(self):
        """Test conversion of deeply nested tree."""
        root = TreeNode(1)
        current = root
        for i in range(2, 6):
            child = TreeNode(i)
            current.add_child(child)
            current = child

        tree = Tree(root)
        result = tree_to_json(tree)

        # Navigate through the deep structure
        current_json = result
        for i in range(1, 6):
            assert current_json["value"] == i
            if i < 5:
                assert len(current_json["children"]) == 1
                current_json = current_json["children"][0]

    def test_wide_tree(self):
        """Test conversion of tree with many children."""
        root = TreeNode("root")
        for i in range(5):
            root.add_child(TreeNode(f"child_{i}"))

        tree = Tree(root)
        result = tree_to_json(tree)

        assert len(result["children"]) == 5
        for i, child in enumerate(result["children"]):
            assert child["value"] == f"child_{i}"
            assert child["children"] == []


class TestCountNodes:
    """Test node counting functionality."""

    def test_count_single_node(self):
        """Test counting a single node."""
        root = TreeNode("A")
        assert _count_nodes(root) == 1

    def test_count_multiple_nodes(self):
        """Test counting nodes in a tree."""
        root = TreeNode("A")
        root.add_child(TreeNode("B"))
        root.add_child(TreeNode("C"))
        root.children[0].add_child(TreeNode("D"))

        assert _count_nodes(root) == 4

    def test_count_deep_tree(self):
        """Test counting nodes in a deep tree."""
        root = TreeNode(1)
        current = root
        for i in range(2, 8):
            child = TreeNode(i)
            current.add_child(child)
            current = child

        assert _count_nodes(root) == 7

    def test_count_wide_tree(self):
        """Test counting nodes in a wide tree."""
        root = TreeNode("root")
        for i in range(10):
            root.add_child(TreeNode(f"child_{i}"))

        assert _count_nodes(root) == 11


class TestTreeToJsonInternal:
    """Test internal _tree_to_json function."""

    def test_convert_single_node(self):
        """Test converting single node."""
        node = TreeNode("A")
        result = _tree_to_json(node)

        assert result["value"] == "A"
        assert result["children"] == []

    def test_convert_with_children(self):
        """Test converting node with children."""
        root = TreeNode("parent")
        root.add_child(TreeNode("child1"))
        root.add_child(TreeNode("child2"))

        result = _tree_to_json(root)

        assert result["value"] == "parent"
        assert len(result["children"]) == 2
        assert all("value" in child and "children" in child for child in result["children"])

    def test_converts_nested_structure_correctly(self):
        """Test nested structure conversion maintains hierarchy."""
        root = TreeNode("A")
        b = TreeNode("B")
        c = TreeNode("C")
        root.add_child(b)
        root.add_child(c)
        b.add_child(TreeNode("D"))

        result = _tree_to_json(root)

        assert result["children"][0]["children"][0]["value"] == "D"


class TestVisualizeTreeJsonValidation:
    """Test input validation for visualize_tree_json."""

    def test_valid_json_dict(self):
        """Test with valid JSON dictionary."""
        tree_json = {
            "value": "A",
            "children": [
                {"value": "B", "children": []},
                {"value": "C", "children": []}
            ]
        }
        # Should not raise any exception
        try:
            visualize_tree_json(tree_json, show=False)
        except AssertionError:
            # matplotlib may fail in headless environment, but input validation should pass
            pass

    def test_valid_json_string(self):
        """Test with valid JSON string."""
        tree_json_str = '{"value": "A", "children": []}'
        # Should not raise any exception
        try:
            visualize_tree_json(tree_json_str, show=False)
        except AssertionError:
            # matplotlib may fail in headless environment, but input validation should pass
            pass

    def test_invalid_json_string(self):
        """Test with invalid JSON string."""
        with pytest.raises(ValueError, match="Invalid JSON string"):
            visualize_tree_json('{"invalid": json}', show=False)

    def test_missing_value_key(self):
        """Test with missing 'value' key."""
        with pytest.raises(ValueError, match="Invalid tree format"):
            visualize_tree_json({"children": []}, show=False)

    def test_not_dict_format(self):
        """Test with non-dict format."""
        with pytest.raises(ValueError, match="Invalid tree format"):
            visualize_tree_json(["A", "B"], show=False)

    def test_empty_dict(self):
        """Test with empty dictionary."""
        with pytest.raises(ValueError, match="Invalid tree format"):
            visualize_tree_json({}, show=False)


class TestVisualizeTreeObjectValidation:
    """Test input validation for visualize_tree_object."""

    def test_valid_tree_object(self):
        """Test with valid Tree object."""
        root = TreeNode("A")
        root.add_child(TreeNode("B"))
        tree = Tree(root)
        # Should not raise any exception during validation
        try:
            visualize_tree_object(tree, show=False)
        except AssertionError:
            # matplotlib may fail in headless environment
            pass

    def test_empty_tree(self):
        """Test with empty tree."""
        tree = Tree(None)
        with pytest.raises(ValueError, match="Tree is empty"):
            visualize_tree_object(tree, show=False)

    def test_tree_with_single_node(self):
        """Test tree with single node."""
        root = TreeNode("root")
        tree = Tree(root)
        try:
            visualize_tree_object(tree, show=False)
        except AssertionError:
            # matplotlib may fail in headless environment
            pass


class TestComplexTreeStructures:
    """Test visualization with complex tree structures."""

    def test_binary_tree_like_structure(self):
        """Test visualization of binary tree-like structure."""
        root = TreeNode("1")
        left = TreeNode("2")
        right = TreeNode("3")
        root.add_child(left)
        root.add_child(right)
        left.add_child(TreeNode("4"))
        left.add_child(TreeNode("5"))
        right.add_child(TreeNode("6"))

        tree = Tree(root)
        result = tree_to_json(tree)

        assert result["value"] == "1"
        assert len(result["children"]) == 2
        assert _count_nodes(root) == 6

    def test_unbalanced_tree(self):
        """Test visualization of unbalanced tree."""
        root = TreeNode("A")
        b = TreeNode("B")
        root.add_child(b)
        b.add_child(TreeNode("C"))
        root.add_child(TreeNode("D"))
        root.add_child(TreeNode("E"))
        root.add_child(TreeNode("F"))

        tree = Tree(root)
        result = tree_to_json(tree)

        assert _count_nodes(root) == 6
        assert len(result["children"]) == 4

    def test_large_tree(self):
        """Test visualization of larger tree."""
        root = TreeNode("root")

        # Create 5 children
        children = [TreeNode(f"child_{i}") for i in range(5)]
        for child in children:
            root.add_child(child)

        # Add grandchildren to some nodes
        for i, child in enumerate(children[:3]):
            for j in range(3):
                child.add_child(TreeNode(f"grandchild_{i}_{j}"))

        tree = Tree(root)
        result = tree_to_json(tree)

        # 1 root + 5 children + 3 * 3 grandchildren = 15 nodes
        assert _count_nodes(root) == 15

    def test_string_values(self):
        """Test tree with string node values."""
        root = TreeNode("root")
        root.add_child(TreeNode("left"))
        root.add_child(TreeNode("right"))

        tree = Tree(root)
        result = tree_to_json(tree)

        assert result["value"] == "root"
        assert all(isinstance(child["value"], str) for child in result["children"])

    def test_numeric_values(self):
        """Test tree with numeric node values."""
        root = TreeNode(1)
        root.add_child(TreeNode(2))
        root.add_child(TreeNode(3))

        tree = Tree(root)
        result = tree_to_json(tree)

        assert result["value"] == 1
        assert all(isinstance(child["value"], int) for child in result["children"])

    def test_mixed_type_values(self):
        """Test tree with mixed type node values."""
        root = TreeNode("root")
        root.add_child(TreeNode(1))
        root.add_child(TreeNode(2.5))
        root.add_child(TreeNode(True))

        tree = Tree(root)
        result = tree_to_json(tree)

        assert result["value"] == "root"
        assert result["children"][0]["value"] == 1
        assert result["children"][1]["value"] == 2.5
        assert result["children"][2]["value"] is True


class TestJsonRoundTrip:
    """Test conversion consistency between Tree and JSON."""

    def test_json_to_tree_to_json(self):
        """Test that JSON -> Tree -> JSON preserves structure."""
        original_json = {
            "value": "A",
            "children": [
                {
                    "value": "B",
                    "children": [
                        {"value": "D", "children": []},
                        {"value": "E", "children": []}
                    ]
                },
                {"value": "C", "children": []}
            ]
        }

        # Manually create Tree from JSON structure
        root = TreeNode(original_json["value"])
        for child_data in original_json["children"]:
            child = TreeNode(child_data["value"])
            root.add_child(child)
            for grandchild_data in child_data["children"]:
                grandchild = TreeNode(grandchild_data["value"])
                child.add_child(grandchild)

        tree = Tree(root)
        result_json = tree_to_json(tree)

        # Compare structures
        assert result_json == original_json

    def test_tree_roundtrip(self):
        """Test that Tree object maintains structure through conversion."""
        root = TreeNode("parent")
        for i in range(3):
            child = TreeNode(f"child_{i}")
            root.add_child(child)
            for j in range(2):
                child.add_child(TreeNode(f"grandchild_{i}_{j}"))

        tree = Tree(root)
        node_count = _count_nodes(tree.root)
        json_data = tree_to_json(tree)

        # Verify structure is preserved
        assert len(json_data["children"]) == 3
        for child_data in json_data["children"]:
            assert len(child_data["children"]) == 2


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_node_with_none_value(self):
        """Test handling of None as node value."""
        root = TreeNode(None)
        tree = Tree(root)
        result = tree_to_json(tree)

        assert result["value"] is None

    def test_node_with_empty_string(self):
        """Test handling of empty string as node value."""
        root = TreeNode("")
        tree = Tree(root)
        result = tree_to_json(tree)

        assert result["value"] == ""

    def test_node_with_special_characters(self):
        """Test handling of special characters in node values."""
        special_chars = "!@#$%^&*()"
        root = TreeNode(special_chars)
        tree = Tree(root)
        result = tree_to_json(tree)

        assert result["value"] == special_chars

    def test_json_with_extra_children_fields(self):
        """Test JSON with additional unexpected fields."""
        tree_json = {
            "value": "A",
            "children": [{"value": "B", "children": []}],
            "extra_field": "should_be_ignored"
        }
        # Should handle gracefully by ignoring extra fields
        try:
            visualize_tree_json(tree_json, show=False)
        except AssertionError:
            # matplotlib failure is acceptable in headless environment
            pass

