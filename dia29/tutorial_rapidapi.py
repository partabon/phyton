import requests
response = requests.get('https://google.com/')
print(response)
if response:
  print('Request is successful.')
else:
  print('Request returned an error.')

import requests

words = 30
paragraphs = 1
formats = 'text'

response = requests.get(f"https://alexnormand-dino-ipsum.p.rapidapi.com/?format={formats}&words={words}&paragraphs={paragraphs}",
 headers={
   "X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
   "X-RapidAPI-Key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 }
)

print(response.text)

response = requests.post("https://NasaAPIdimasV1.p.rapidapi.com/getEPICEarthImagery",
  headers={
    "X-RapidAPI-Host": "NasaAPIdimasV1.p.rapidapi.com",
    "X-RapidAPI-Key": "krV5NqBAVIt4J2dDDOY4af3VWn5u1iUoxwRHdDnr",
    "Content-Type": "application/x-www-form-urlencoded"
  }
)

print(response)
if response:
  print('Request is successful.')
else:
  print('Request returned an error.')