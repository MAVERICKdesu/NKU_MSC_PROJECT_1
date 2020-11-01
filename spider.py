import requests
import bs4

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                            '65.0.3325.1''81 Safari/537.36'}

url = "https://www.baidu.com/s?wd=%E7%88%AC%E8%99%AB"
response = requests.get(url=url, allow_redirects=False, headers=headers)
response.encoding = 'utf-8'
soup = bs4.BeautifulSoup(response.text, "html5lib")
with open("baidu.txt", "w",  encoding='utf-8') as f:
    f.write(response.text)
list = soup.find_all("div", {"class":"result c-container new-pmd"})
for item in list:
   print(item.find_all("a")[0].get("href"))

