import pytest
from click.testing import CliRunner


@pytest.fixture
def runner():
    """ Returns the click client testing runner """
    return CliRunner()
