import pytest

from zilla_package.zilla import Zilla


@pytest.fixture
def zilla_instance():
    """Fixture to create a Zilla instance with a default name."""
    return Zilla("test-zilla")



