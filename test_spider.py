import pytest
import os

from spider import Spider
from datetime import datetime
from states import states

runningDataStore = '\\\\monster.local\\RunningData\\'

def test_states():
    assert(len(states) == 51)

def test_save_result():
    s = Spider()
    testFile = "foobar.txt"
    if os.path.exists(testFile):
        os.remove(testFile)
    s.save_result(testFile,"some stuff".encode())
    assert(os.path.exists(testFile))

def test_build_output_path():
    s = Spider()
    s.output_folder = runningDataStore
    base_url = 'http://www.coolrunning.com/results/17/ct/Dec3_PearlH_set1.shtml'
    path = s.build_output_path(base_url)
    assert(path == '\\\\monster.local\\RunningData\\17\ct\\Dec3_PearlH_set1.shtml')

def test_base_url_list():
    s = Spider()
    years = datetime.now().year - 2000 + 1
    base_urls = s.get_base_urls()
    assert(len(base_urls) == 51*years)

def test_extract_links():
    s = Spider()
    url = 'http://www.coolrunning.com/results/17/pa.shtml'
    filter = url.rsplit('.')[-2][3:]
    status, html = s.get_web_content(url)
    links = s.extract_links(html,filter)
    assert(len(links) == 18)
    assert(status == 200)



