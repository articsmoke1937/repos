import requests
import json
heads = {'Host': 'www.sec.gov', 'Connection': 'close',
         'Accept': 'application/json, text/javascript, */*; q=0.01', 'X-Requested-With': 'XMLHttpRequest',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
         }
def download(year):
    for qtr in range(1, 5):
        url = f"https://data.sec.gov/submissions/CIK0001449003.json"
        response = requests.get(url, headers=heads)
        jurl = response.json()
        jdata = json.loads(jurl)
        print('jurl')

download(2019)