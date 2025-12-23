"""
Level-Order Parsing Tree Visualization Examples
================================================

Demonstrates visualization of parsing trees using the level-order traversal.
Shows how to:
1. Parse mathematical expressions into tree structures
2. Visualize the resulting expression trees
3. Show tree construction step-by-step
4. Compare different parsing strategies

This demonstrates the motion of parsing trees with level-order traversal.
"""

import json

from data_structures.trees.level_order_parsing_tree import (
    ExpressionTree,
    ParsingTreeBuilder,
)
from data_structures.trees.tree import Tree, TreeNode


def example_1_simple_expression_parsing():
    """Example 1: Parse and visualize a simple expression."""
    print("=" * 70)
    print("Example 1: Simple Expression Parsing")
    print("=" * 70)

    expr = "2 + 3"
    print(f"\nExpression: {expr}")

    # Step 1: Tokenize
    tokens = ExpressionTree._tokenize(expr)
    print(f"Step 1 - Tokenize: {tokens}")

    # Step 2: Convert to postfix
    postfix = ExpressionTree._infix_to_postfix(tokens)
    print(f"Step 2 - Infix to Postfix: {postfix}")

    # Step 3: Build tree
    tree = ExpressionTree.from_infix(expr)
    print(f"Step 3 - Tree Structure:")
    print(tree)

    # Step 4: Evaluate
    result = tree.evaluate()
    print(f"Step 4 - Evaluation: {result}")

    # Step 5: Level-order traversal
    print(f"\nLevel-order traversal:")
    for node, level, pos in tree.level_order_with_context():
        print(f"  Level {level}: {node.value}")

    # Step 6: Summary
    summary = tree.tree_structure_summary()
    print(f"\nTree Summary:")
    print(f"  Total nodes: {summary['total_nodes']}")
    print(f"  Operators: {summary['operators']}")
    print(f"  Operands: {summary['operands']}")


def example_2_precedence_aware_parsing():
    """Example 2: Show how precedence affects tree structure."""
    print("\n" + "=" * 70)
    print("Example 2: Operator Precedence in Parsing")
    print("=" * 70)

    expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
    ]

    for expr in expressions:
        print(f"\n--- Expression: {expr} ---")

        tree = ExpressionTree.from_infix(expr)
        result = tree.evaluate()

        print(f"Tree structure:")
        for line in str(tree).split("\n"):
            print(f"  {line}")

        print(f"Evaluation: {result}")

        # Show level-order view
        print(f"Level-order view:")
        for node, level, pos in tree.level_order_with_context():
            node_type = "Op" if node.is_operator else "Num"
            indent = "  " * (level + 1)
            print(f"{indent}L{level}:P{pos} {node.value}({node_type})")


def example_3_complex_expression_motion():
    """Example 3: Show parsing motion for complex expression."""
    print("\n" + "=" * 70)
    print("Example 3: Complex Expression Parsing Motion")
    print("=" * 70)

    expr = "2 + 3 * 4 - 5 / 2"
    print(f"\nExpression: {expr}")

    # Show parsing steps
    tokens = ExpressionTree._tokenize(expr)
    print(f"\nStep 1 - Tokenization:")
    for i, token in enumerate(tokens):
        print(f"  Token {i}: '{token}'")

    postfix = ExpressionTree._infix_to_postfix(tokens)
    print(f"\nStep 2 - Shunting Yard Algorithm (Postfix notation):")
    print(f"  {' '.join(postfix)}")

    # Build tree
    tree = ExpressionTree.from_infix(expr)
    print(f"\nStep 3 - Build Tree (from postfix):")
    print(tree)

    # Evaluate
    result = tree.evaluate()
    print(f"\nStep 4 - Evaluate: {result}")

    # Level-order traversal
    print(f"\nStep 5 - Level-Order Traversal (BFS Motion):")
    levels = {}
    for node, level, pos in tree.level_order_with_context():
        if level not in levels:
            levels[level] = []
        levels[level].append(node.value)

    for level in sorted(levels.keys()):
        print(f"  Level {level}: {levels[level]}")

    # Summary
    summary = tree.tree_structure_summary()
    print(f"\nTree Statistics:")
    print(f"  Depth: {summary['depth']}")
    print(f"  Total nodes: {summary['total_nodes']}")
    print(f"  Operators: {summary['operators']}")
    print(f"  Operands: {summary['operands']}")


def example_4_level_order_construction():
    """Example 4: Build tree level-by-level."""
    print("\n" + "=" * 70)
    print("Example 4: Level-Order Tree Construction")
    print("=" * 70)

    tokens = ["A", "B", "C", "D", "E", "F", "G", "H"]
    print(f"\nTokens: {tokens}")

    # Build tree using level-order
    root = ParsingTreeBuilder.build_from_tokens_level_order(tokens)
    tree = Tree(root)

    print(f"\nTree structure (built level-by-level):")
    print(tree)

    # Show level-order traversal
    print(f"\nLevel-order traversal:")
    level_order_values = list(tree.level_order())
    print(f"  {' -> '.join(str(v) for v in level_order_values)}")

    # Show what happens at each level
    print(f"\nLevel-by-level breakdown:")
    levels = {}
    queue = [(root, 0)]
    while queue:
        node, level = queue.pop(0)
        if level not in levels:
            levels[level] = []
        levels[level].append(node.value)
        for child in node.children:
            queue.append((child, level + 1))

    for level in sorted(levels.keys()):
        print(f"  Level {level}: {levels[level]}")


def example_5_traversal_comparison():
    """Example 5: Compare different traversal orders."""
    print("\n" + "=" * 70)
    print("Example 5: Traversal Order Comparison")
    print("=" * 70)

    expr = "2 + 3 * 4"
    tree = ExpressionTree.from_infix(expr)

    print(f"\nExpression: {expr}")
    print(f"\nTree structure:")
    print(tree)

    # Different traversals
    preorder = list(tree.preorder())
    postorder = list(tree.postorder())
    level_order = list(tree.level_order())

    print(f"\nTraversal Comparisons:")
    print(f"  Preorder (NLR):   {' -> '.join(str(v) for v in preorder)}")
    print(f"  Postorder (LRN):  {' -> '.join(str(v) for v in postorder)}")
    print(f"  Level-order (BFS):{' -> '.join(str(v) for v in level_order)}")

    print(f"\nUse cases:")
    print(f"  Preorder:   Used for copying trees, prefix notation")
    print(f"  Postorder:  Used for evaluation, deleting trees, postfix notation")
    print(f"  Level-order: Used for tree construction, printing levels")


def example_6_json_representation():
    """Example 6: Show tree as JSON."""
    print("\n" + "=" * 70)
    print("Example 6: Tree JSON Representation")
    print("=" * 70)

    expr = "2 + 3 * 4"
    tree = ExpressionTree.from_infix(expr)

    print(f"\nExpression: {expr}")

    # Convert to JSON-like structure
    def tree_to_dict(node):
        return {
            "value": node.value,
            "type": "operator" if node.is_operator else "operand",
            "children": [tree_to_dict(child) for child in node.children]
        }

    tree_dict = tree_to_dict(tree.root)
    print(f"\nTree as JSON:")
    print(json.dumps(tree_dict, indent=2))


def example_7_expression_parsing_variations():
    """Example 7: Parse various expressions and show their trees."""
    print("\n" + "=" * 70)
    print("Example 7: Expression Parsing Variations")
    print("=" * 70)

    expressions = [
        "2 + 3",
        "2 * 3",
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "2 * 3 + 4 * 5",
        "((2 + 3) * 4) / 5",
    ]

    for expr in expressions:
        try:
            tree = ExpressionTree.from_infix(expr)
            result = tree.evaluate()
            print(f"\n{expr:20} = {result}")

            summary = tree.tree_structure_summary()
            print(f"  (depth={summary['depth']}, nodes={summary['total_nodes']})")

        except Exception as e:
            print(f"\n{expr:20} ERROR: {e}")


if __name__ == "__main__":
    print("\n" + "#" * 70)
    print("# LEVEL-ORDER PARSING TREE VISUALIZATION DEMONSTRATIONS")
    print("# Motion of Parsing Trees with Level-Order Traversal")
    print("#" * 70)

    example_1_simple_expression_parsing()
    example_2_precedence_aware_parsing()
    example_3_complex_expression_motion()
    example_4_level_order_construction()
    example_5_traversal_comparison()
    example_6_json_representation()
    example_7_expression_parsing_variations()

    print("\n" + "#" * 70)
    print("# DEMONSTRATIONS COMPLETE")
    print("#" * 70 + "\n")

