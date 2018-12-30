import urllib3
import os.path
from bs4 import BeautifulSoup as bs

runningDataStore = '\\\\monster.local\\RunningData'

class Spider:
    def download_file(self, targetUrl):
        http = urllib3.PoolManager()
        response = http.request('GET', targetUrl)
        if response.status == 200:
            path = os.path.join(runningDataStore, 'CoolRunningFile.txt')
            self.save_result(path, response.data)

    def save_result(self, path, data):
        with open(path, 'wb') as f:
            f.write(data)

    def extract_links(self, data):
        pass

coolRunningDownloader = Spider()
coolRunningDownloader.download_file('http://www.coolrunning.com/results/17/ct/Dec3_PearlH_set1.shtml')


