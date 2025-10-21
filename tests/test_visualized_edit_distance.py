from algorithms.dynamic_programming.visualized_edit_distance import \
    visualize_edit_operations


def test_visualize_edit_operations():
    ops = visualize_edit_operations("kitten", "sitting")
    assert isinstance(ops, list)
    assert any(op[0] in {"insert", "delete", "replace", "match"} for op in ops)
