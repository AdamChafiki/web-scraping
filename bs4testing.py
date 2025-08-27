import bs4

with open("example.html") as exampleFile:
    exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")

elems = exampleSoup.select("#author")
print(elems[0].get("id"))
