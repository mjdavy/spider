import pytest
from spider import Spider
import os

testFile="foobar.txt"

@pytest.fixture()
def before():
    if os.path.exists(testFile):
        os.remove(testFile)

def test_SaveResult(before):
    s = Spider()
    s.SaveResult(testFile,"some stuff".encode())
    assert(os.path.exists(testFile))