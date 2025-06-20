import pytest
from services.reporter.main import run

def test_run():
    assert run() is None  # basic sanity test
