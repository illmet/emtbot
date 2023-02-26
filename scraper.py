import requests
from bs4 import BeautifulSoup

URL = "https://www.lottery.ie/results/euromillions/history"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
#dates
dateinter = soup.find_all("h4", class_="text-xl font-black text-2xl")
dates = []
for i in dateinter:
    dates.append(i.get_text())
#jackpots
amountinter = soup.find_all("p", class_="font-black text-xl")
amount = []
for i in amountinter:
    amount.append(i.get_text())
amount = amount[::2]
#location (winning ticket was bought in)
locinter = soup.find_all("p", class_="text-sm")
loc = []
for i in locinter:
    loc.append(i.get_text())
last = loc[0].split(".")
#current jackpot
currentjackpot = "https://www.lottery.ie/draw-games/euromillions"
pagecurr = requests.get(currentjackpot)
soup2 = BeautifulSoup(pagecurr.content, "html.parser")
jack = soup2.find("h1", class_="text-white shadow-text text-3xl md:text-4xl lg:text-5xl font-black")
jackpot = jack.get_text()
jackpot = jackpot.split(" ")[0]