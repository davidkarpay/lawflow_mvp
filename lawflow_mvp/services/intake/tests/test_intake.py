import pytest
from services.intake.main import run

def test_run():
    assert run() is None  # basic sanity test
