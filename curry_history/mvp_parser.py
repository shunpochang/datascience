import requests
from bs4 import BeautifulSoup
output = []
for year in xrange(1957, 2016):
    html = requests.get('http://www.basketball-reference.com/awards/awards_%s.html' %str(year))
    if not html:
        continue
    s = BeautifulSoup(html.text, 'html.parser')
    mvp_rows = s.find('table', attrs={'id':'mvp'}).find_all('tr', attrs={'class':''})
    # First two rows are headers, and third row is the top MVP.
    vals = mvp_rows[2].find_all('td')
    # starting from column 1 - in order the values are:
    # name, age, team, top votes, won votes, max votes, vote share.
    year_val = [str(year)]
    year_val.extend([vals[i].get_text() for i in xrange(1,8)])
    output.append(year_val)

with open('mvp_output.txt', 'w') as f:
    for l in output:
        f.writelines(','.join(l))

