"""
Test suite for level-order parsing tree functionality.

Tests cover:
- Expression tokenization and parsing
- Infix to postfix conversion (Shunting Yard algorithm)
- Expression tree construction
- Expression evaluation
- Level-order traversal
- Operator precedence handling
- Error cases and edge conditions
"""

import pytest

from data_structures.trees.level_order_parsing_tree import (
    ExpressionNode,
    ExpressionTree,
    ParsingTreeBuilder,
)
from data_structures.trees.tree import Tree, TreeNode


class TestExpressionNodeCreation:
    """Test ExpressionNode creation and properties."""

    def test_create_operand_node(self):
        """Test creating operand node."""
        node = ExpressionNode(5, is_operator=False)
        assert node.value == 5
        assert not node.is_operator
        assert node.children == []

    def test_create_operator_node(self):
        """Test creating operator node."""
        node = ExpressionNode("+", is_operator=True)
        assert node.value == "+"
        assert node.is_operator
        assert node.children == []

    def test_node_repr(self):
        """Test node string representation."""
        op_node = ExpressionNode("+", is_operator=True)
        num_node = ExpressionNode(5, is_operator=False)

        assert "Op" in repr(op_node)
        assert "Num" in repr(num_node)

    def test_add_child_to_operator(self):
        """Test adding children to operator node."""
        op_node = ExpressionNode("+", is_operator=True)
        left = ExpressionNode(3, is_operator=False)
        right = ExpressionNode(5, is_operator=False)

        op_node.add_child(left)
        op_node.add_child(right)

        assert len(op_node.children) == 2
        assert op_node.children[0].value == 3
        assert op_node.children[1].value == 5


class TestTokenization:
    """Test expression tokenization."""

    def test_simple_expression(self):
        """Test tokenizing simple expression."""
        tokens = ExpressionTree._tokenize("2 + 3")
        assert tokens == ["2", "+", "3"]

    def test_expression_with_multiple_operators(self):
        """Test tokenizing expression with multiple operators."""
        tokens = ExpressionTree._tokenize("2 + 3 * 4")
        assert tokens == ["2", "+", "3", "*", "4"]

    def test_expression_with_parentheses(self):
        """Test tokenizing expression with parentheses."""
        tokens = ExpressionTree._tokenize("(2 + 3) * 4")
        assert tokens == ["(", "2", "+", "3", ")", "*", "4"]

    def test_expression_without_spaces(self):
        """Test tokenizing expression without spaces."""
        tokens = ExpressionTree._tokenize("2+3*4")
        assert tokens == ["2", "+", "3", "*", "4"]

    def test_multi_digit_numbers(self):
        """Test tokenizing multi-digit numbers."""
        tokens = ExpressionTree._tokenize("123 + 456")
        assert tokens == ["123", "+", "456"]

    def test_decimal_numbers(self):
        """Test tokenizing decimal numbers."""
        tokens = ExpressionTree._tokenize("3.14 + 2.86")
        assert tokens == ["3.14", "+", "2.86"]


class TestPrecedence:
    """Test operator precedence."""

    def test_addition_subtraction_same_precedence(self):
        """Test that + and - have same precedence."""
        assert ExpressionTree._get_precedence("+") == ExpressionTree._get_precedence("-")

    def test_multiplication_division_same_precedence(self):
        """Test that * and / have same precedence."""
        assert ExpressionTree._get_precedence("*") == ExpressionTree._get_precedence("/")

    def test_multiplication_higher_than_addition(self):
        """Test that * has higher precedence than +."""
        assert ExpressionTree._get_precedence("*") > ExpressionTree._get_precedence("+")

    def test_exponentiation_highest(self):
        """Test that ^ has highest precedence."""
        assert ExpressionTree._get_precedence("^") > ExpressionTree._get_precedence("*")

    def test_unknown_operator(self):
        """Test precedence of unknown operator."""
        assert ExpressionTree._get_precedence("?") == 0


class TestInfixToPostfix:
    """Test Shunting Yard algorithm for infix to postfix conversion."""

    def test_simple_addition(self):
        """Test conversion of simple addition."""
        result = ExpressionTree._infix_to_postfix(["2", "+", "3"])
        assert result == ["2", "3", "+"]

    def test_simple_multiplication(self):
        """Test conversion of simple multiplication."""
        result = ExpressionTree._infix_to_postfix(["2", "*", "3"])
        assert result == ["2", "3", "*"]

    def test_precedence_matters(self):
        """Test that precedence is respected."""
        result = ExpressionTree._infix_to_postfix(["2", "+", "3", "*", "4"])
        assert result == ["2", "3", "4", "*", "+"]

    def test_parentheses_override_precedence(self):
        """Test that parentheses override precedence."""
        result = ExpressionTree._infix_to_postfix(["(", "2", "+", "3", ")", "*", "4"])
        assert result == ["2", "3", "+", "4", "*"]

    def test_nested_parentheses(self):
        """Test conversion with nested parentheses."""
        result = ExpressionTree._infix_to_postfix(
            ["(", "(", "2", "+", "3", ")", "*", "4", ")"]
        )
        assert result == ["2", "3", "+", "4", "*"]

    def test_multiple_operators_same_precedence(self):
        """Test left-to-right evaluation for same precedence."""
        result = ExpressionTree._infix_to_postfix(["2", "-", "3", "-", "4"])
        assert result == ["2", "3", "-", "4", "-"]


class TestExpressionTreeConstruction:
    """Test building expression trees from expressions."""

    def test_build_simple_addition(self):
        """Test building tree for simple addition."""
        tree = ExpressionTree.from_infix("2 + 3")
        assert tree.root.is_operator
        assert tree.root.value == "+"

    def test_build_with_precedence(self):
        """Test building tree respects precedence."""
        tree = ExpressionTree.from_infix("2 + 3 * 4")
        # Root should be + since it's at lowest precedence
        assert tree.root.value == "+"
        # Right child should be * (higher precedence)
        assert tree.root.children[1].value == "*"

    def test_build_with_parentheses(self):
        """Test building tree with parentheses."""
        tree = ExpressionTree.from_infix("(2 + 3) * 4")
        # Root should be * since parentheses force + to be evaluated first
        assert tree.root.value == "*"

    def test_invalid_expression_missing_operand(self):
        """Test error handling for missing operand."""
        with pytest.raises(ValueError):
            ExpressionTree.from_infix("2 + ")

    def test_invalid_expression_too_many_operands(self):
        """Test error handling for too many operands."""
        with pytest.raises(ValueError):
            ExpressionTree.from_infix("2 3 +")

    def test_invalid_number(self):
        """Test error handling for invalid number."""
        with pytest.raises(ValueError):
            ExpressionTree.from_infix("abc + 3")


class TestExpressionEvaluation:
    """Test expression evaluation."""

    def test_evaluate_addition(self):
        """Test evaluating addition."""
        tree = ExpressionTree.from_infix("2 + 3")
        assert tree.evaluate() == 5

    def test_evaluate_subtraction(self):
        """Test evaluating subtraction."""
        tree = ExpressionTree.from_infix("5 - 2")
        assert tree.evaluate() == 3

    def test_evaluate_multiplication(self):
        """Test evaluating multiplication."""
        tree = ExpressionTree.from_infix("3 * 4")
        assert tree.evaluate() == 12

    def test_evaluate_division(self):
        """Test evaluating division."""
        tree = ExpressionTree.from_infix("12 / 3")
        assert tree.evaluate() == 4

    def test_evaluate_with_precedence(self):
        """Test evaluation respects precedence."""
        tree = ExpressionTree.from_infix("2 + 3 * 4")
        assert tree.evaluate() == 14  # Not 20

    def test_evaluate_with_parentheses(self):
        """Test evaluation with parentheses."""
        tree = ExpressionTree.from_infix("(2 + 3) * 4")
        assert tree.evaluate() == 20

    def test_evaluate_complex_expression(self):
        """Test evaluating complex expression."""
        tree = ExpressionTree.from_infix("2 + 3 * 4 - 5 / 2")
        # 2 + 12 - 2.5 = 11.5
        assert tree.evaluate() == 11.5

    def test_evaluate_negative_result(self):
        """Test evaluation with negative result."""
        tree = ExpressionTree.from_infix("2 - 5")
        assert tree.evaluate() == -3

    def test_evaluate_decimal_numbers(self):
        """Test evaluation with decimal numbers."""
        tree = ExpressionTree.from_infix("3.5 + 2.5")
        assert tree.evaluate() == 6.0

    def test_evaluate_division_by_zero(self):
        """Test division by zero handling."""
        tree = ExpressionTree.from_infix("5 / 0")
        result = tree.evaluate()
        assert result == float("inf")


class TestLevelOrderTraversal:
    """Test level-order traversal functionality."""

    def test_level_order_simple_tree(self):
        """Test level-order traversal on simple tree."""
        tree = ExpressionTree.from_infix("2 + 3")
        values = list(tree.level_order())
        assert values[0] == "+"  # Root is operator

    def test_level_order_with_context(self):
        """Test level-order traversal with context."""
        tree = ExpressionTree.from_infix("2 + 3 * 4")
        traversal = list(tree.level_order_with_context())

        # First node should be at level 0
        assert traversal[0][1] == 0

    def test_level_order_deeper_tree(self):
        """Test level-order on deeper tree."""
        tree = ExpressionTree.from_infix("2 + 3 * 4 - 5")
        traversal = list(tree.level_order_with_context())

        # Check we have multiple levels
        levels = set(node[1] for node in traversal)
        assert len(levels) > 1


class TestTreeStructureSummary:
    """Test tree structure summary statistics."""

    def test_simple_tree_summary(self):
        """Test summary for simple tree."""
        tree = ExpressionTree.from_infix("2 + 3")
        summary = tree.tree_structure_summary()

        assert summary["total_nodes"] == 3
        assert summary["operators"] == 1
        assert summary["operands"] == 2

    def test_complex_tree_summary(self):
        """Test summary for complex tree."""
        tree = ExpressionTree.from_infix("2 + 3 * 4")
        summary = tree.tree_structure_summary()

        assert summary["total_nodes"] == 5
        assert summary["operators"] == 2
        assert summary["operands"] == 3

    def test_summary_depth(self):
        """Test depth calculation in summary."""
        tree = ExpressionTree.from_infix("2 + 3 * 4 - 5")
        summary = tree.tree_structure_summary()

        assert summary["depth"] > 1
        assert "levels" in summary


class TestParsingTreeBuilder:
    """Test ParsingTreeBuilder utility class."""

    def test_build_empty_tokens(self):
        """Test building tree from empty tokens."""
        root = ParsingTreeBuilder.build_from_tokens_level_order([])
        assert root is None

    def test_build_single_token(self):
        """Test building tree from single token."""
        root = ParsingTreeBuilder.build_from_tokens_level_order(["A"])
        assert root.value == "A"
        assert root.children == []

    def test_build_binary_tree_structure(self):
        """Test building tree creates binary structure."""
        tokens = ["A", "B", "C", "D", "E", "F", "G"]
        root = ParsingTreeBuilder.build_from_tokens_level_order(tokens)

        tree = Tree(root)
        # Verify tree structure
        assert tree.root.value == "A"
        assert len(tree.root.children) == 2

    def test_build_from_mathematical_expression(self):
        """Test building from mathematical expression."""
        tree = ParsingTreeBuilder.parse_mathematical_expression("2 + 3")
        assert isinstance(tree, ExpressionTree)
        assert tree.evaluate() == 5

    def test_builder_expression_with_precedence(self):
        """Test builder respects precedence."""
        tree = ParsingTreeBuilder.parse_mathematical_expression("2 + 3 * 4")
        assert tree.evaluate() == 14


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_single_number(self):
        """Test expression with just a number."""
        tree = ExpressionTree.from_infix("42")
        assert tree.evaluate() == 42

    def test_negative_numbers(self):
        """Test handling of negative numbers (as operands)."""
        tree = ExpressionTree.from_infix("-5 + 3")
        # Note: This might fail depending on tokenizer implementation
        # Included to identify limitations

    def test_whitespace_handling(self):
        """Test that extra whitespace is handled."""
        tree1 = ExpressionTree.from_infix("2 + 3")
        tree2 = ExpressionTree.from_infix("2+3")
        tree3 = ExpressionTree.from_infix("2  +  3")

        assert tree1.evaluate() == tree2.evaluate() == tree3.evaluate()

    def test_deeply_nested_parentheses(self):
        """Test deeply nested parentheses."""
        tree = ExpressionTree.from_infix("((2 + 3))")
        assert tree.evaluate() == 5

    def test_all_operators(self):
        """Test all operators are handled."""
        expressions = [
            ("2 + 3", 5),
            ("5 - 2", 3),
            ("3 * 4", 12),
            ("12 / 3", 4),
        ]

        for expr, expected in expressions:
            tree = ExpressionTree.from_infix(expr)
            assert tree.evaluate() == expected, f"Failed for {expr}"

    def test_zero_values(self):
        """Test handling of zero."""
        tree = ExpressionTree.from_infix("0 + 5")
        assert tree.evaluate() == 5

    def test_large_numbers(self):
        """Test handling of large numbers."""
        tree = ExpressionTree.from_infix("1000000 + 2000000")
        assert tree.evaluate() == 3000000


class TestTreeConversion:
    """Test tree structure conversions."""

    def test_expression_tree_inherits_tree(self):
        """Test ExpressionTree is subclass of Tree."""
        tree = ExpressionTree.from_infix("2 + 3")
        assert isinstance(tree, Tree)

    def test_tree_string_representation(self):
        """Test tree can be converted to string."""
        tree = ExpressionTree.from_infix("2 + 3")
        tree_str = str(tree)
        assert "+" in tree_str

    def test_node_traversal_methods(self):
        """Test all traversal methods work."""
        tree = ExpressionTree.from_infix("2 + 3 * 4")

        preorder = list(tree.preorder())
        postorder = list(tree.postorder())
        level_order = list(tree.level_order())

        # All should have same number of nodes
        assert len(preorder) == len(postorder) == len(level_order)

        # All should contain all values
        assert set(preorder) == set(postorder) == set(level_order)


class TestComplexScenarios:
    """Test complex real-world scenarios."""

    def test_mathematical_sequence(self):
        """Test sequence of mathematical operations."""
        expressions = [
            ("2 + 2", 4),
            ("2 * 2", 4),
            ("4 / 2", 2),
            ("2 + 2 * 2", 6),
            ("(2 + 2) * 2", 8),
        ]

        for expr, expected in expressions:
            tree = ExpressionTree.from_infix(expr)
            assert tree.evaluate() == expected

    def test_mixed_operations_evaluation(self):
        """Test evaluation of mixed operations."""
        tree = ExpressionTree.from_infix("10 - 2 * 3 + 4 / 2")
        # 10 - 6 + 2 = 6
        assert tree.evaluate() == 6

    def test_tree_structure_consistency(self):
        """Test tree structure remains consistent."""
        expr = "2 + 3 * 4"
        tree = ExpressionTree.from_infix(expr)

        # Multiple evaluations should give same result
        results = [tree.evaluate() for _ in range(5)]
        assert len(set(results)) == 1

