from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

#HartmannReport
URL1 = "https://rss.art19.com/the-hartmann-report"
#live
URL2 = "http://stream1.thomhartmann.com/hartmannfp"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(10000), 
            'path': "http://stream1.thomhartmann.com/hartmannfp",
            'thumbnail': "https://pbs.twimg.com/profile_images/1284920980/thom-2011-150_400x400.jpg", 
            'is_playable': True},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://cdn3.thomhartmann.com/sites/default/files/thom%20and%20logo_13.jpg"},
 {
            'label': plugin.get_string(3000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://cdn3.thomhartmann.com/sites/default/files/thom%20and%20logo_13.jpg"},
    ]

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup1 = mainaddon.get_soup1(URL1)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup1 = mainaddon.get_soup(URL1)
    
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    
    items = mainaddon.compile_playable_podcast(playable_podcast)

    return items


if __name__ == '__main__':
    plugin.run()
