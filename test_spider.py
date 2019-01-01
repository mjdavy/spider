import pytest
from spider import Spider
from datetime import datetime
import states
import url_base
import os

testFile="foobar.txt"
runningDataStore = '\\\\monster.local\\RunningData\\'
base_url = 'http://www.coolrunning.com/results/17/ct/Dec3_PearlH_set1.shtml'

@pytest.fixture()
def before():
    if os.path.exists(testFile):
        os.remove(testFile)

def test_save_result(before):
    s = Spider()
    s.save_result(testFile,"some stuff".encode())
    assert(os.path.exists(testFile))

def test_build_output_path():
    s = Spider()
    path = s.build_output_path(runningDataStore,base_url)
    assert(path == '\\\\monster.local\\RunningData\\Dec3_PearlH_set1.shtml')

def test_states():
    assert(len(states.states) == 51)

def test_base_url_list():
    years = datetime.now().year - 2000 + 1
    base_urls = url_base.get_base_urls()
    assert(len(base_urls) == 51*years)

def test_extract_links():
    s = Spider()
    url = 'http://www.coolrunning.com/results/17/pa.shtml'
    html = s.get_web_content(url)
    links = s.extract_links(html)
    assert(len(links) > 0)


