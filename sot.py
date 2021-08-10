import requests

r = requests.get('https://www.sothebys.com/en/results?from=&to=&f2=00000164-609b-d1db-a5e6-e9ff01230000&f2=00000164-609b-d1db-a5e6-e9ff08ab0000&f2=00000164-609b-d1db-a5e6-e9ff0b150000&f3=LIVE&f3=ONLINE&q=')
r.text