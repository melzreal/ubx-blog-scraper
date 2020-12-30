from bs4 import BeautifulSoup

with open("ubx-blog-list.html", encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, "html5lib")


for a in soup.select("a.blog-tile"):
    titles = a.find("div", {"class": "blog-large-tile__title"})
    authors = a.find("div", {"class": "blog-large-tile__author"})
    dates = a.find("div", {"class": "blog-large-tile__date"})

    authors_text = authors.text
    print(authors_text)

