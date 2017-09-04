#!/usr/bin/python
import requests
from BeautifulSoup import BeautifulSoup

def decodeWebpage(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text)
  
  for story_heading in soup.find_all(class_="stroy-heading"):
    if story_heading.a:
      print (story_heading.a.text.replace("\n", " ").strip())
    else:
      print (story_heading.contents[0].strip())


def main():
  decodeWebpage('http://www.nytimes.com/')

if __name__ == '__main__':
  main()
