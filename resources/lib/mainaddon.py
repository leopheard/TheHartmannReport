import requests
import re
from bs4 import BeautifulSoup

def get_soup1(url1):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    
    print "type: ", type(soup1)
    return soup1

get_soup1("https://rss.art19.com/the-hartmann-report")

def get_soup2(url2):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    
    print "type: ", type(soup2)
    return soup2

get_soup2("http://stream1.thomhartmann.com/hartmannfp")


def get_playable_podcast1(soup1):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup1.find_all('item'):
        
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link

            title = content.find('title')
            title = title.get_text()

#            desc = content.find('description')
#            desc = desc.get_text()

            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': thumbnail
        }
        
        subjects.append(item) 
    
    return subjects


def compile_playable_podcast1(playable_podcast1):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })

    return items


def get_playable_podcast1(soup1):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup1.find_all('item', limit=3):
        
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link

            title = content.find('title')
            title = title.get_text()

#            desc = content.find('description')
#            desc = desc.get_text()

            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': thumbnail
        }
        
        subjects.append(item) 
    
    return subjects


def compile_playable_podcast1(playable_podcast1):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })

    return items
