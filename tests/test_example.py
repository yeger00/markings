
def test_example_1(clear_all_markers):
    from markings import marker
    import examples.example_1_module
    assert len(list(marker.todo.filter("examples"))) == 1
    assert len(list(marker.known_issue.filter("examples"))) == 1
