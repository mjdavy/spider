import urllib3
import os.path
from bs4 import BeautifulSoup as bs

runningDataStore = 'E:\\RunningData'

class Spider:
    def DownloadFile(self, targetUrl):
        http = urllib3.PoolManager()
        response = http.request('GET', targetUrl)
        if response.status == 200:
            path = os.path.join(runningDataStore, 'CoolRunningFile.txt')
            self.SaveResult(path, response.data)

    def SaveResult(self, path, data):
        with open(path, 'wb') as f:
            f.write(data)

    def ExtractLinks(self, data):
        pass

coolRunningDownloader = Spider()
coolRunningDownloader.DownloadFile('http://www.coolrunning.com/results/17/ct/Dec3_PearlH_set1.shtml')


