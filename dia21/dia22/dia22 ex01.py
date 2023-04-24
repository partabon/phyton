import requests # importing the request module

url = 'http://www.bu.edu/president/boston-university-facts-stats/' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
html_doc = response.text # gives all the text from the page
#print(text)


from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)

print(soup.a)
print(soup.find_all('a'))
print(soup.find(id="link"))
#print(soup.get_text())
