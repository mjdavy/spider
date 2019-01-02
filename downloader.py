

from spider import Spider

runningDataStore = '\\\\monster\\RunningData\\'

spider = Spider()
spider.output_folder = runningDataStore

for url in spider.get_base_urls():
    filter = url.rsplit('.')[-2][3:]
    race_urls = spider.process_url(url,filter)
    for race_url in race_urls:
        fullUrl = f"http://www.coolrunning.com{race_url}"
        spider.download_file(fullUrl)

 
