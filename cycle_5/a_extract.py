import requests
from bs4 import BeautifulSoup
print("Jerry James \n23MCA036")
def getdata(url):
    r = requests.get(url)
    return r.content

htmldata = getdata("https://sjcetpalai.ac.in/")
soup = BeautifulSoup(htmldata, 'html.parser')
links = soup.find_all('a')
print("Total no: of links:",len(links)) 
for i in links:
    if i.get("href") != "":
        print("Link : ", i.get("href"), "text: ", i.string)