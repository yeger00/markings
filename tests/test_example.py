
def test_example_1(clear_all_markers):
    from markings import marker
    import examples.example_1_module
    assert len(marker.todo) == 1
    assert len(marker.known_issue) == 1
