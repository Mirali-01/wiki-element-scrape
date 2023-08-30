import requests
from bs4 import BeautifulSoup


def getElementNames():
    url = "https://en.wikipedia.org/wiki/List_of_chemical_elements"
    page = requests.get(url=url)
    soup = BeautifulSoup(page.content, "html.parser")
    t_body = soup.find("tbody")

    t_row = t_body.find_all("tr", {"class": "anchor"})
    Elements = []
    for row in t_row:
        t_data_cell = row.find_all("a")
        data_cell_element = t_data_cell[0]
        for data_cell in data_cell_element:
            title_name = data_cell.text
            # print(title_name)
            Elements.append(title_name)

    print(Elements)


getElementNames()
