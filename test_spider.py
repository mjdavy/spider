import pytest
from spider import Spider
import os

testFile="foobar.txt"

@pytest.fixture()
def before():
    if os.path.exists(testFile):
        os.remove(testFile)

def test_save_result(before):
    s = Spider()
    s.save_result(testFile,"some stuff".encode())
    assert(os.path.exists(testFile))