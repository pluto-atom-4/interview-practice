"""
Integration Example: Complete Parsing Tree Workflow
====================================================

Demonstrates a complete workflow combining:
1. Parsing trees for expression handling
2. Tree visualization
3. Level-order traversal motion
4. Multiple parsing strategies
"""

import json

from data_structures.trees.level_order_parsing_tree import (
    ExpressionTree,
    ParsingTreeBuilder,
)
from data_structures.trees.tree import Tree, TreeNode


def workflow_1_parse_and_evaluate():
    """Workflow 1: Parse expression and evaluate."""
    print("=" * 70)
    print("Workflow 1: Parse and Evaluate Expression")
    print("=" * 70)

    expressions = [
        ("2 + 3", 5),
        ("2 * 3 + 4", 10),
        ("(2 + 3) * 4", 20),
        ("10 - 2 * 3 + 4 / 2", 6),
    ]

    for expr, expected in expressions:
        tree = ExpressionTree.from_infix(expr)
        result = tree.evaluate()
        status = "✓" if result == expected else "✗"
        print(f"{status} {expr:20} = {result:6} (expected: {expected})")


def workflow_2_analyze_tree_structure():
    """Workflow 2: Analyze tree structure after parsing."""
    print("\n" + "=" * 70)
    print("Workflow 2: Analyze Tree Structure")
    print("=" * 70)

    expr = "2 + 3 * 4 - 5 / 2"
    tree = ExpressionTree.from_infix(expr)

    print(f"\nExpression: {expr}")
    print(f"\nTree Structure:")
    print(tree)

    summary = tree.tree_structure_summary()
    print(f"\nStructure Analysis:")
    print(f"  Total nodes: {summary['total_nodes']}")
    print(f"  Operators: {summary['operators']}")
    print(f"  Operands: {summary['operands']}")
    print(f"  Depth: {summary['depth']}")

    print(f"\nLevel-by-level:")
    for level in sorted(summary['levels'].keys()):
        values = summary['levels'][level]
        print(f"  Level {level}: {values}")


def workflow_3_level_order_motion():
    """Workflow 3: Show level-order motion through tree."""
    print("\n" + "=" * 70)
    print("Workflow 3: Level-Order Tree Motion")
    print("=" * 70)

    expr = "2 + 3 * 4"
    tree = ExpressionTree.from_infix(expr)

    print(f"\nExpression: {expr}")
    print(f"\nLevel-Order Traversal Motion (BFS):")

    nodes_by_level = {}
    for node, level, pos in tree.level_order_with_context():
        if level not in nodes_by_level:
            nodes_by_level[level] = []
        nodes_by_level[level].append((node, pos))

    visit_order = []
    for level in sorted(nodes_by_level.keys()):
        print(f"\n  >>> Visiting Level {level}:")
        for node, pos in nodes_by_level[level]:
            node_type = "Op" if node.is_operator else "Num"
            print(f"      Position {pos}: {node.value} ({node_type})")
            visit_order.append(node.value)

    print(f"\nFinal visit order: {' → '.join(str(v) for v in visit_order)}")


def workflow_4_build_and_construct():
    """Workflow 4: Build tree level-by-level."""
    print("\n" + "=" * 70)
    print("Workflow 4: Level-Order Tree Construction")
    print("=" * 70)

    tokens = ["root", "left", "right", "ll", "lr", "rl", "rr"]
    print(f"\nTokens to insert: {tokens}")

    print(f"\nBuilding tree level-by-level...")
    root = ParsingTreeBuilder.build_from_tokens_level_order(tokens)
    tree = Tree(root)

    print(f"\nResulting Tree Structure:")
    print(tree)

    print(f"\nLevel-order traversal:")
    level_values = list(tree.level_order())
    print(f"  {' → '.join(str(v) for v in level_values)}")


def workflow_5_compare_precedence():
    """Workflow 5: Compare how precedence affects tree structure."""
    print("\n" + "=" * 70)
    print("Workflow 5: Operator Precedence Impact")
    print("=" * 70)

    # Same operands, different precedence due to parentheses
    test_cases = [
        ("2 + 3 * 4", "No parentheses"),
        ("(2 + 3) * 4", "Parentheses override"),
        ("2 * 3 + 4", "Different order"),
        ("2 * (3 + 4)", "Force addition first"),
    ]

    print(f"\nComparing tree structures:\n")
    for expr, description in test_cases:
        tree = ExpressionTree.from_infix(expr)
        result = tree.evaluate()
        summary = tree.tree_structure_summary()

        print(f"{expr:15} ({description})")
        print(f"  Evaluation: {result}")
        print(f"  Root operator: {tree.root.value}")
        print(f"  Depth: {summary['depth']}")
        print()


def workflow_6_traversal_comparison():
    """Workflow 6: Compare different traversal methods."""
    print("\n" + "=" * 70)
    print("Workflow 6: Traversal Method Comparison")
    print("=" * 70)

    expr = "2 + 3 * 4"
    tree = ExpressionTree.from_infix(expr)

    print(f"\nExpression: {expr}")
    print(f"\nTree Structure:")
    print(tree)

    preorder = list(tree.preorder())
    postorder = list(tree.postorder())
    level_order = list(tree.level_order())

    print(f"\nTraversal Methods:")
    print(f"  Preorder (NLR):    {' → '.join(str(v) for v in preorder)}")
    print(f"  Postorder (LRN):   {' → '.join(str(v) for v in postorder)}")
    print(f"  Level-order (BFS): {' → '.join(str(v) for v in level_order)}")

    print(f"\nUse Cases:")
    print(f"  Preorder:   Copy tree, prefix notation, tree traversal")
    print(f"  Postorder:  Evaluate expression, postfix notation, delete tree")
    print(f"  Level-order: Tree construction, printing by level")


def workflow_7_parsing_pipeline():
    """Workflow 7: Show complete parsing pipeline."""
    print("\n" + "=" * 70)
    print("Workflow 7: Complete Parsing Pipeline")
    print("=" * 70)

    expr = "10 / (2 + 3)"
    print(f"\nParsing: {expr}")

    # Step 1: Tokenize
    tokens = ExpressionTree._tokenize(expr)
    print(f"\nStep 1 - Tokenization:")
    print(f"  Input:  '{expr}'")
    print(f"  Output: {tokens}")

    # Step 2: Convert to postfix
    postfix = ExpressionTree._infix_to_postfix(tokens)
    print(f"\nStep 2 - Infix to Postfix (Shunting Yard):")
    print(f"  Input:  {' '.join(tokens)}")
    print(f"  Output: {' '.join(postfix)}")

    # Step 3: Build tree
    tree = ExpressionTree.from_infix(expr)
    print(f"\nStep 3 - Build Expression Tree:")
    print(tree)

    # Step 4: Analyze
    summary = tree.tree_structure_summary()
    print(f"\nStep 4 - Tree Analysis:")
    print(f"  Nodes: {summary['total_nodes']}")
    print(f"  Operators: {summary['operators']}")
    print(f"  Operands: {summary['operands']}")
    print(f"  Depth: {summary['depth']}")

    # Step 5: Evaluate
    result = tree.evaluate()
    print(f"\nStep 5 - Evaluation: {result}")


def workflow_8_json_representation():
    """Workflow 8: Export tree to JSON."""
    print("\n" + "=" * 70)
    print("Workflow 8: JSON Export and Representation")
    print("=" * 70)

    expr = "2 + 3 * 4"
    tree = ExpressionTree.from_infix(expr)

    print(f"\nExpression: {expr}")

    def to_json(node):
        return {
            "value": str(node.value),
            "type": "operator" if node.is_operator else "operand",
            "children": [to_json(child) for child in node.children]
        }

    tree_json = to_json(tree.root)
    print(f"\nTree as JSON:")
    print(json.dumps(tree_json, indent=2))


def workflow_9_error_handling():
    """Workflow 9: Demonstrate error handling."""
    print("\n" + "=" * 70)
    print("Workflow 9: Error Handling")
    print("=" * 70)

    invalid_expressions = [
        ("2 +", "Missing operand"),
        ("2 3 +", "Invalid sequence"),
        ("/ 2", "Invalid start"),
        ("2 + + 3", "Double operator"),
    ]

    print(f"\nTesting invalid expressions:\n")
    for expr, reason in invalid_expressions:
        try:
            tree = ExpressionTree.from_infix(expr)
            result = tree.evaluate()
            print(f"✗ {expr:15} - Should have failed ({reason})")
        except ValueError as e:
            print(f"✓ {expr:15} - Error: {str(e)[:40]}")


def workflow_10_performance_test():
    """Workflow 10: Performance analysis."""
    print("\n" + "=" * 70)
    print("Workflow 10: Performance Analysis")
    print("=" * 70)

    test_expressions = [
        "2 + 3",
        "2 + 3 * 4",
        "2 + 3 * 4 - 5 / 2",
        "(2 + 3) * (4 - 5) / 2",
        "1 + 2 * 3 + 4 * 5 + 6 * 7",
    ]

    print(f"\nPerformance Analysis:\n")
    print(f"{'Expression':<35} {'Tokens':<8} {'Nodes':<8} {'Depth':<8} {'Result':<10}")
    print(f"{'-' * 35} {'-' * 8} {'-' * 8} {'-' * 8} {'-' * 10}")

    for expr in test_expressions:
        tokens = ExpressionTree._tokenize(expr)
        tree = ExpressionTree.from_infix(expr)
        summary = tree.tree_structure_summary()
        result = tree.evaluate()

        print(f"{expr:<35} {len(tokens):<8} {summary['total_nodes']:<8} "
              f"{summary['depth']:<8} {result:<10.2f}")


if __name__ == "__main__":
    print("\n" + "#" * 70)
    print("# COMPLETE PARSING TREE WORKFLOW INTEGRATION")
    print("#" * 70)

    workflow_1_parse_and_evaluate()
    workflow_2_analyze_tree_structure()
    workflow_3_level_order_motion()
    workflow_4_build_and_construct()
    workflow_5_compare_precedence()
    workflow_6_traversal_comparison()
    workflow_7_parsing_pipeline()
    workflow_8_json_representation()
    workflow_9_error_handling()
    workflow_10_performance_test()

    print("\n" + "#" * 70)
    print("# ALL WORKFLOWS COMPLETED")
    print("#" * 70 + "\n")

