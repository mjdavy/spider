import urllib3
import os.path
from bs4 import BeautifulSoup as bs

class Spider:
    def get_web_content(self, targetUrl):
        http = urllib3.PoolManager()
        response = http.request('GET', targetUrl)
        htmlContent = ""
        if response.status == 200:
            htmlContent = response.data
        else:
            print("error accessing url")
        return htmlContent

    def download_file(self, targetUrl, outputFolder):
        content = self.get_web_content(targetUrl)
        path = self.build_output_path(outputFolder, targetUrl)
        self.save_result(path, content)
          
    def build_output_path(self, folder, url):
        name = url.split('/')[-1:]
        path = os.path.join(folder, name[0])
        return path
        
    def save_result(self, path, data):
        with open(path, 'wb') as f:
            f.write(data)

    def extract_links(self, data):
        soup = bs(data, 'html.parser')
        return [link.get('href') for link in soup.find_all('a')]
            



