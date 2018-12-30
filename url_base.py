from datetime import datetime
from states import states

# format is http://www.coolrunning.com/results/15/ma.shtml

years = [str(y)[-2:] for y in range(2000,datetime.now().year+1)]
print(years)

base = "www.coolrunning.com/results/"
base_urls = []

for year in years:
    allStates = [base+year+"/"+state.lower()+".shtml" for state in states]
    base_urls.append(allStates)

print(base_urls)
print(len(base_urls))