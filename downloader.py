from spider import Spider

runningDataStore = '\\\\monster.local\\RunningData\'
base_url = 'http://www.coolrunning.com/results/17/ct/Dec3_PearlH_set1.shtml'

def extract_year_and_state(url):
    url_parts = url.split('/')
    parts_count = len(url_parts)
    year = url_parts[parts_count - 2]
    state = url_parts[parts_count - 1].split('.')[0]
    return year, state

year, state = extract_year_and_state(base_url)

coolRunningDownloader = Spider()
coolRunningDownloader.download_file(base_url, runningDataStore )