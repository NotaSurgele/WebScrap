#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

def html_content(link):
    data = requests.get(link)
    return data.content

def get_instance(html_doc):
    return BeautifulSoup(html_doc, "html5lib")

def get_links(soup):
    links = []

    for a in soup.find_all("a"):
        link = a.get("href")
        if link.__contains__("https://") and not link.__contains__("google") and not link.__contains__("pdf"):
            links.append(link)
    return links

def get_texts(soup):
    for p in soup.find_all("p"):
        print(p.getText())

if __name__ == "__main__":
    data = html_content("https://scholar.google.com/scholar?as_ylo=2022&q=metaverse&hl=fr&as_sdt=0,5")
    soup = get_instance(html_doc=data)
    links = get_links(soup)
    index = 1
    for link in links:
        print("====================== Article " + str(index) + " ======================")
        html = html_content(link)
        soup = get_instance(html_doc=html)
        get_texts(soup=soup)
        print("========================================================\n\n")

