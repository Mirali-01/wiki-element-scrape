import requests
from bs4 import BeautifulSoup


def getElementPageContent():
    url = "https://en.wikipedia.org/wiki/Hydrogen"
    page = requests.get(url=url)
    soup = BeautifulSoup(page.content, "html.parser")
    elementName = soup.find(id="firstHeading")
    table = soup.find("table", {"class": "infobox"})
    t_body = table.find("tbody")
    t_row = t_body.find_all("tr")

    print(t_row[8])

    # for row in t_row:
    #     print(row.text.strip())

    print(elementName.text)


getElementPageContent()
