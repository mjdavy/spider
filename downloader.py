from datetime import datetime
from states import states
from spider import Spider

runningDataStore = '\\\\monster.local\\RunningData\\'

# format is http://www.coolrunning.com/results/<2 digit year>/<2 letter state>.shtml
# example: race result for vermont in 2016 would be http://www.coolrunning.com/results/16/vt.shtml

def get_base_urls():
    base = "www.coolrunning.com/results/"
    years = [str(y)[-2:] for y in range(2000,datetime.now().year+1)]
    return [base+year+"/"+state.lower()+".shtml" for state in states for year in years]

def extract_year_and_state(url):
    url_parts = url.split('/')
    parts_count = len(url_parts)
    year = url_parts[parts_count - 2]
    state = url_parts[parts_count - 1].split('.')[0]
    return year, state
