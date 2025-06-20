import pytest
from services.executor.main import run

def test_run():
    assert run() is None  # basic sanity test
