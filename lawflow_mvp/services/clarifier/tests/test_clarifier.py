import pytest
from services.clarifier.main import run

def test_run():
    assert run() is None  # basic sanity test
