from markings import marker

def test_sanity(clear_all_markers):
    assert len(marker.todo) == 0

    @marker.todo
    def func1():
        return 1

    @marker.known_issue
    def func2():
        return 1

    assert len(list(marker.todo.filter("tests"))) == 1

def test_filter(clear_all_markers):
    assert len(marker.todo) == 0

    @marker.todo
    def func():
        return 1

    @marker.known_issue
    def func2():
        return 1

    assert len(list(marker.todo.filter("tes", False))) == 1

def test_dynamic_attribute(clear_all_markers):
    assert len(marker.todo) == 0

    @marker.whatever
    def func1():
        return 1

    assert len(list(marker.whatever.filter("tests"))) == 1
