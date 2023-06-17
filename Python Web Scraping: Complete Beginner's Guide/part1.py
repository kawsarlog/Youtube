import requests
import bs4

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)
print(response)
soup = bs4.BeautifulSoup(response.text, "html.parser")

title = soup.find('h1').text
print(title)

urls = []

eles = soup.find_all('a')
for ele in eles:
    url = ele.get('href')
    urls.append(url)

print(urls)
