import requests

parameter = {"sl" : "plethora"}
f = "https://api.datamuse.com/words?"

data1 = requests.get(f, params=parameter)

print(data1)

print(data1.text)