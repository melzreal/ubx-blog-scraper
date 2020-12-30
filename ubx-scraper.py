from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

browser = webdriver.Chrome()
browser.get("https://unboxed.co/blog")

blog_posts = []
published_dates = []
titles_text = []
tag_group = []
authors_text = []
blog_contents = []
post_images = []

blog_posts = browser.find_elements_by_css_selector("a.blog-tile.blog-large-tile")
# len(blog_posts)
for i in range(4):

    posts = browser.find_elements_by_css_selector("a.blog-tile.blog-large-tile")
    posts[i].click()

    # title = browser.find_element_by_css_selector("span.blog-header__article-title")
    # titles_text += [title.text]

    # published_date = browser.find_element_by_css_selector("div.blog-header__published-date")
    # published_dates += [published_date.text]

    # tags = browser.find_elements_by_css_selector("a.blog-tags__tag.blog-tags__tag--active")
    # tag_group += [[t.text for t in tags]]

    try:
        author = browser.find_element_by_css_selector("a.blog-header__author--linked")
        authors_text += [author.text]
    except:
        author = browser.find_element_by_css_selector("div.blog-header__author")
        authors_text += [author.text]

    images = browser.find_elements_by_css_selector(".blog-content img")
    print("images", images)

    for image in images:
        post_images += [image.get_attribute('src'), image.get_attribute('alt')]

    blog_content = browser.find_element_by_css_selector("article.blog-content")
    blog_contents += [blog_content.text]

    browser.back()

    # scraping blog index

    # authors = browser.find_elements_by_css_selector("div.blog-large-tile__author")
    # authors_text += [t.text for t in authors]

    # next_page = browser.find_element_by_css_selector("a.blog-pagination__link")
    # next_page.click()

print(post_images)

# csv_clean_blog = [i.replace('\n','|') for i in  blog_contents]

# dict = {'title': titles_text, 'date': published_dates, 'author': authors_text, 'tags': tag_group, 'content': csv_clean_blog }

# df = pd.DataFrame(dict)
# df.to_csv('blogs.csv')