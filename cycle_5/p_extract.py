import requests
from bs4 import BeautifulSoup
print("Jerry James \n23MCA036")
def getdata(url):
    r = requests.get(url)
    return r.content

htmldata = getdata("https://sjcetpalai.ac.in/")
soap = BeautifulSoup(htmldata, 'html.parser')
data = ''
pr = len(soap.find_all('p'))
print("<p> tag", pr)
for data in soap.find_all('p'):
    print(data.get_text())