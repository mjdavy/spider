import urllib3
import os
import os.path
from bs4 import BeautifulSoup as bs
from datetime import datetime
from states import states

class Spider:
    output_folder = '.\\'
    base = "www.coolrunning.com/results/"

    # format is http://www.coolrunning.com/results/<2 digit year>/<2 letter state>.shtml
    # example: race result for vermont in 2016 would be http://www.coolrunning.com/results/16/vt.shtml  
    def get_base_urls(self):
        years = [str(y)[-2:] for y in range(2000,datetime.now().year+1)]
        return [self.base+year+"/"+state.lower()+".shtml" for state in states for year in years]

    def get_web_content(self, targetUrl):
        http = urllib3.PoolManager()
        response = http.request('GET', targetUrl)
        return response.status, response.data

    def download_file(self, targetUrl):
        status, content = self.get_web_content(targetUrl)
        if status == 200:
            path = self.build_output_path(targetUrl)
            self.save_result(path, content)
          
    def build_output_path(self, url):
        name = url.split('/')[-1:]
        year,state = url.split('/')[-3:-1]
        folder = f"{self.output_folder}{year}\\{state}\\"
        if not os.path.exists(folder):
            os.makedirs(folder)
        path = os.path.join(folder, name[0])
        return path
        
    def save_result(self, path, data):
        with open(path, 'wb') as f:
            f.write(data)

    def extract_links(self, data, match):
        soup = bs(data, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a')]
        return [link for link in links if link is not None and match in link]

    def process_url(self, url, filter):
        status, html = self.get_web_content(url)
        links = self.extract_links(html,filter)
        return links


            



