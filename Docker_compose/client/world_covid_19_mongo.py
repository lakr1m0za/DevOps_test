import requests
import pymongo
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus"
r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
data = s.find_all("div",class_ = "maincounter-number")

con = data[0].text.strip().replace(",", "")
de = data[1].text.strip().replace(",", "")
he = data[2].text.strip().replace(",", "")

client = pymongo.MongoClient('mongodb://server:27017/')
db = client['covid19_test']
col = db.col

mydict = {"confirmed": con, "death": de, "health": he}
x = col.insert_one(mydict)

for x in col.find():
    print (x)
