from markings import marker

def test_sanity(clear_all_markers):
    assert len(marker.todo) == 0

    @marker.todo
    def func():
        return 1

    assert len(marker.todo) == 1
