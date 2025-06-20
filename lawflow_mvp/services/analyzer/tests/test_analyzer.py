import pytest
from services.analyzer.main import run

def test_run():
    assert run() is None  # basic sanity test
