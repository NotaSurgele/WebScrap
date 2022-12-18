#!/usr/bin/env python3

from bs4 import BeautifulSoup
import sys
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
            title = a.getText()
            links.append((link, title))
    return links

def get_texts(soup):
    for p in soup.find_all("p"):
        print(p.getText())

#"https://scholar.google.com/scholar?hl=fr&as_sdt=0%2C5&as_ylo=2022&q=metaverse+opinion&btnG="

if __name__ == "__main__":
    index = 1
    f = open(sys.argv[1], "r")
    links = f.read().split("\n")

    for link in links:
        data = html_content(link)
        soup = get_instance(html_doc=data)
        infos = get_links(soup)
        for link, title in infos:
            print("====================== Article " + str(index) + " " + link + " " + title + " =======\n\n")
            html = html_content(link)
            soup = get_instance(html_doc=html)
            get_texts(soup=soup)
            print("================================================================================================================\n\n")
            index += 1