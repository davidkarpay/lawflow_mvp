import pytest
from services.retriever.main import run

def test_run():
    assert run() is None  # basic sanity test
