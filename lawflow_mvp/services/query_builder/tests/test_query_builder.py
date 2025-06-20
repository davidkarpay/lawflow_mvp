import pytest
from services.query_builder.main import run

def test_run():
    assert run() is None  # basic sanity test
