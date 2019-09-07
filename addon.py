from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL1 = "https://rss.art19.com/the-hartmann-report"  #HartmannReport
URL2 = "http://stream1.thomhartmann.com/hartmannfp"  #live
URL3 = "https://www.thomhartmann.com/podcasts.xml?token=8n5cpef8kchye42urmk7hpmpfa3oeeng" #TH HOUR

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30010), 
            'path': "http://stream1.thomhartmann.com/hartmannfp",
            'thumbnail': "https://cdn-radiotime-logos.tunein.com/s184220q.png", 
            'is_playable': True},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://content.production.cdn.art19.com/images/9d/86/34/c6/9d8634c6-dbca-4368-9f95-c55922195f83/460c595b8fa9ce2d24d5328a274e187c8f7ba039adc9f7b404d921e9b32092c373be11d84bde5be717e7412f277594a791eb73f996a1702e045c5fbf3b9477bd.jpeg"},
 {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://content.production.cdn.art19.com/images/9d/86/34/c6/9d8634c6-dbca-4368-9f95-c55922195f83/460c595b8fa9ce2d24d5328a274e187c8f7ba039adc9f7b404d921e9b32092c373be11d84bde5be717e7412f277594a791eb73f996a1702e045c5fbf3b9477bd.jpeg"},
 {
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('all_episodes3'),
            'thumbnail': "https://content.production.cdn.art19.com/images/9d/86/34/c6/9d8634c6-dbca-4368-9f95-c55922195f83/460c595b8fa9ce2d24d5328a274e187c8f7ba039adc9f7b404d921e9b32092c373be11d84bde5be717e7412f277594a791eb73f996a1702e045c5fbf3b9477bd.jpeg"},

    ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup1 = mainaddon.get_soup1(URL1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup1 = mainaddon.get_soup1(URL1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/all_episodes3/')
def all_episodes3():
    soup3 = mainaddon.get_soup3(URL3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

if __name__ == '__main__':
    plugin.run()
