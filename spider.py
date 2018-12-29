import urllib3
import os.path
from bs4 import BeautifulSoup as bs

class Spider:
    def DownloadFile(self, targetUrl):
        http = urllib3.PoolManager()
        response = http.request('GET', targetUrl)
        if response.status == 200:
            self.SaveResult('CoolRunningFile', response.data)

    def SaveResult(self, fileName, data):
        path = os.path.join('Data', fileName)
        with open(path, 'wb') as f:
            f.write(data)

coolRunningDownloader = Spider()
coolRunningDownloader.DownloadFile('http://www.coolrunning.com/results/17/ct/Dec3_PearlH_set1.shtml')


