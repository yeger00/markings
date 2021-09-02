import pytest
from markings import marker

@pytest.fixture()
def clear_all_markers():
    for _, marker_list in marker:
        marker_list.clear_all()
    yield
    for _, marker_list in marker:
        marker_list.clear_all()
