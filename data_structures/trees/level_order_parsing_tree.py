"""
Level-Order Parsing Tree
========================

Demonstrates parsing tree structures using level-order traversal.
Shows how to:
1. Parse expressions into tree structures
2. Build trees level by level
3. Traverse and evaluate expression trees using level-order traversal
4. Visualize the parsing process

Key Concepts:
- Level-order traversal for tree construction and evaluation
- Expression parsing (infix to tree)
- Tree evaluation at each level
- Breadth-first construction and traversal

Time Complexity:
- Building tree from tokens: O(N) where N is number of tokens
- Level-order traversal: O(N)
- Evaluation: O(N)

This structure is useful for:
- Mathematical expression parsing
- SQL query parsing
- Compiler design (Abstract Syntax Trees)
- Configuration file parsing
"""

from collections import deque
from typing import Any, Callable, List, Optional, Union

from data_structures.trees.tree import Tree, TreeNode


class ExpressionNode(TreeNode):
    """Extended TreeNode for expression trees with operator/operand distinction."""

    def __init__(self, value: Any, is_operator: bool = False) -> None:
        super().__init__(value)
        self.is_operator = is_operator

    def __repr__(self) -> str:
        node_type = "Op" if self.is_operator else "Num"
        return f"ExpressionNode({self.value!r}, {node_type})"


class ExpressionTree(Tree):
    """Binary expression tree with parsing and evaluation capabilities."""

    def __init__(self, root: Optional[ExpressionNode] = None) -> None:
        super().__init__(root)

    @staticmethod
    def _tokenize(expression: str) -> List[str]:
        """Tokenize mathematical expression into tokens.

        Args:
            expression: Mathematical expression string (e.g., "3 + 5 * 2")

        Returns:
            List of tokens.
        """
        tokens = []
        current = ""
        for char in expression:
            if char in "+-*/()" or char.isspace():
                if current:
                    tokens.append(current)
                    current = ""
                if char != " ":
                    tokens.append(char)
            else:
                current += char
        if current:
            tokens.append(current)
        return tokens

    @staticmethod
    def _get_precedence(operator: str) -> int:
        """Get operator precedence.

        Args:
            operator: Operator symbol

        Returns:
            Precedence level (higher = binds tighter)
        """
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        return precedence.get(operator, 0)

    @staticmethod
    def _infix_to_postfix(tokens: List[str]) -> List[str]:
        """Convert infix notation to postfix (Reverse Polish Notation).

        Uses the Shunting Yard algorithm.

        Args:
            tokens: List of tokens in infix notation

        Returns:
            List of tokens in postfix notation
        """
        output = []
        operator_stack = []

        for token in tokens:
            if token not in "+-*/()^":
                # It's a number/operand
                output.append(token)
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack and operator_stack[-1] != "(":
                    output.append(operator_stack.pop())
                if operator_stack:
                    operator_stack.pop()  # Remove '('
            else:
                # It's an operator
                while (
                    operator_stack
                    and operator_stack[-1] != "("
                    and ExpressionTree._get_precedence(operator_stack[-1])
                    >= ExpressionTree._get_precedence(token)
                ):
                    output.append(operator_stack.pop())
                operator_stack.append(token)

        while operator_stack:
            output.append(operator_stack.pop())

        return output

    @classmethod
    def from_infix(cls, expression: str) -> "ExpressionTree":
        """Build expression tree from infix notation.

        Args:
            expression: Mathematical expression in infix notation (e.g., "3 + 5 * 2")

        Returns:
            ExpressionTree object

        Raises:
            ValueError: If expression is invalid
        """
        tokens = cls._tokenize(expression)
        postfix = cls._infix_to_postfix(tokens)
        return cls._build_from_postfix(postfix)

    @classmethod
    def _build_from_postfix(cls, postfix: List[str]) -> "ExpressionTree":
        """Build expression tree from postfix notation using stack.

        Args:
            postfix: List of tokens in postfix notation

        Returns:
            ExpressionTree object
        """
        stack: List[ExpressionNode] = []

        for token in postfix:
            if token in "+-*/^":
                # Pop two operands
                if len(stack) < 2:
                    raise ValueError(f"Invalid expression: insufficient operands for {token}")
                right = stack.pop()
                left = stack.pop()

                # Create operator node
                op_node = ExpressionNode(token, is_operator=True)
                op_node.add_child(left)
                op_node.add_child(right)
                stack.append(op_node)
            else:
                # It's a number
                try:
                    value = float(token) if "." in token else int(token)
                    stack.append(ExpressionNode(value, is_operator=False))
                except ValueError:
                    raise ValueError(f"Invalid number: {token}")

        if len(stack) != 1:
            raise ValueError("Invalid expression: too many operands")

        return cls(stack[0])

    def evaluate(self) -> float:
        """Evaluate the expression tree.

        Returns:
            Result of evaluating the expression
        """
        if self.root is None:
            raise ValueError("Tree is empty")

        def _evaluate_node(node: ExpressionNode) -> float:
            if not node.is_operator:
                return float(node.value)

            if len(node.children) != 2:
                raise ValueError(f"Operator {node.value} must have exactly 2 children")

            left = _evaluate_node(node.children[0])
            right = _evaluate_node(node.children[1])

            operators = {
                "+": lambda a, b: a + b,
                "-": lambda a, b: a - b,
                "*": lambda a, b: a * b,
                "/": lambda a, b: a / b if b != 0 else float("inf"),
                "^": lambda a, b: a ** b,
            }

            return operators[node.value](left, right)

        return _evaluate_node(self.root)

    def level_order_with_context(self):
        """Traverse tree level-order and yield (node, level, position_in_level).

        Yields:
            Tuple of (node, level, position_in_level)
        """
        if not self.root:
            return

        queue: deque[tuple[ExpressionNode, int, int]] = deque([(self.root, 0, 0)])
        level_counts: dict[int, int] = {0: 1}

        while queue:
            node, level, pos = queue.popleft()
            yield node, level, pos

            if node.children:
                next_level = level + 1
                if next_level not in level_counts:
                    level_counts[next_level] = 0

                for idx, child in enumerate(node.children):
                    queue.append((child, next_level, level_counts[next_level]))
                    level_counts[next_level] += 1

    def tree_structure_summary(self) -> dict:
        """Get summary of tree structure.

        Returns:
            Dictionary with tree statistics
        """
        if not self.root:
            return {}

        levels = {}
        operators = 0
        operands = 0

        for node, level, pos in self.level_order_with_context():
            if level not in levels:
                levels[level] = []
            levels[level].append(node.value)

            if node.is_operator:
                operators += 1
            else:
                operands += 1

        return {
            "total_nodes": operators + operands,
            "operators": operators,
            "operands": operands,
            "levels": levels,
            "depth": len(levels),
        }


class ParsingTreeBuilder:
    """Utility class for building parsing trees from various formats."""

    @staticmethod
    def build_from_tokens_level_order(tokens: List[str]) -> Optional[TreeNode]:
        """Build a simple tree from tokens using level-order construction.

        This demonstrates level-by-level tree building.

        Args:
            tokens: List of node values to insert level by level

        Returns:
            Root node of constructed tree, or None if tokens is empty
        """
        if not tokens:
            return None

        root = TreeNode(tokens[0])
        queue: deque[TreeNode] = deque([root])
        idx = 1

        while queue and idx < len(tokens):
            node = queue.popleft()

            # Add up to 2 children (binary tree structure)
            for _ in range(2):
                if idx < len(tokens):
                    child = TreeNode(tokens[idx])
                    node.add_child(child)
                    queue.append(child)
                    idx += 1

        return root

    @staticmethod
    def parse_mathematical_expression(expression: str) -> ExpressionTree:
        """Parse mathematical expression into tree.

        Args:
            expression: Mathematical expression (e.g., "2 + 3 * 4")

        Returns:
            ExpressionTree object
        """
        return ExpressionTree.from_infix(expression)


def demonstrate_level_order_parsing():
    """Demonstrate level-order parsing and traversal."""
    print("=" * 70)
    print("LEVEL-ORDER PARSING TREE DEMONSTRATION")
    print("=" * 70)

    # Example 1: Simple expression tree
    print("\n" + "-" * 70)
    print("Example 1: Simple Expression Tree - '2 + 3'")
    print("-" * 70)

    expr1 = "2 + 3"
    tree1 = ExpressionTree.from_infix(expr1)

    print(f"Expression: {expr1}")
    print(f"Tree structure:\n{tree1}")
    print(f"Evaluation: {tree1.evaluate()}")

    # Example 2: Complex expression with precedence
    print("\n" + "-" * 70)
    print("Example 2: Complex Expression - '2 + 3 * 4'")
    print("-" * 70)

    expr2 = "2 + 3 * 4"
    tree2 = ExpressionTree.from_infix(expr2)

    print(f"Expression: {expr2}")
    print(f"Tree structure:\n{tree2}")
    print(f"Evaluation: {tree2.evaluate()}")

    # Level-order traversal with context
    print("\nLevel-order traversal with depth info:")
    for node, level, pos in tree2.level_order_with_context():
        node_type = "Op" if node.is_operator else "Num"
        indent = "  " * level
        print(f"{indent}Level {level}, Pos {pos}: {node.value} ({node_type})")

    # Tree structure summary
    print("\nTree structure summary:")
    summary = tree2.tree_structure_summary()
    for key, value in summary.items():
        if key != "levels":
            print(f"  {key}: {value}")

    # Example 3: Expression with parentheses
    print("\n" + "-" * 70)
    print("Example 3: Expression with Parentheses - '(2 + 3) * 4'")
    print("-" * 70)

    expr3 = "(2 + 3) * 4"
    tree3 = ExpressionTree.from_infix(expr3)

    print(f"Expression: {expr3}")
    print(f"Tree structure:\n{tree3}")
    print(f"Evaluation: {tree3.evaluate()}")

    # Example 4: Deeper expression
    print("\n" + "-" * 70)
    print("Example 4: Deeper Expression - '2 + 3 * 4 - 5 / 2'")
    print("-" * 70)

    expr4 = "2 + 3 * 4 - 5 / 2"
    tree4 = ExpressionTree.from_infix(expr4)

    print(f"Expression: {expr4}")
    print(f"Tree structure:\n{tree4}")
    print(f"Evaluation: {tree4.evaluate()}")

    # Level-order traversal
    print("\nLevel-order traversal:")
    print("Values: ", " -> ".join(str(val) for val in tree4.level_order()))

    # Tree summary
    print("\nTree structure summary:")
    summary = tree4.tree_structure_summary()
    for key, value in summary.items():
        if key != "levels":
            print(f"  {key}: {value}")
        else:
            print(f"  levels:")
            for level, values in value.items():
                print(f"    Level {level}: {values}")

    # Example 5: Demonstrate tree building from tokens
    print("\n" + "-" * 70)
    print("Example 5: Level-Order Tree Building from Tokens")
    print("-" * 70)

    tokens = ["A", "B", "C", "D", "E", "F", "G"]
    root = ParsingTreeBuilder.build_from_tokens_level_order(tokens)
    if root:
        built_tree = Tree(root)
        print(f"Tokens: {tokens}")
        print(f"Built tree:\n{built_tree}")
        print(f"Level-order traversal: {list(built_tree.level_order())}")


def demonstrate_visualization():
    """Demonstrate visualization of parsing trees."""
    print("\n" + "=" * 70)
    print("VISUALIZATION OF PARSING TREES")
    print("=" * 70)

    try:
        import json

        from visualize_tree import tree_to_json, visualize_tree_object

        # Example: Visualize expression tree
        expr = "2 + 3 * 4"
        tree = ExpressionTree.from_infix(expr)

        print(f"\nVisualizing expression tree for: {expr}")
        print(f"Result: {tree.evaluate()}")

        # Convert to JSON and display
        tree_json = tree_to_json(tree)
        print(f"\nTree as JSON:")
        print(json.dumps(tree_json, indent=2))

        # Visualize
        visualize_tree_object(tree, title=f"Expression Tree: {expr}", show=False)

    except ImportError:
        print("Visualization modules not available")


if __name__ == "__main__":
    demonstrate_level_order_parsing()
    demonstrate_visualization()

    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)

