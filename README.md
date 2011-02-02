python-instagram
======
A Python client for the Instagram REST and Search APIs

Installation
-----
pip install instagram

Requires
-----
  * httplib2
  * simplejson

Follow @instagramapi on Twitter
----------------------------
You can [follow @instagramapi on Twitter](http://twitter.com/#!/instagramapi) for announcements,
updates, and news about the Instagram gem.

Obtaining an access token
-----
You can use the provided get_access_token.py script to obtain an access token for yourself. 
It will prompt you for your app's Client ID, Client Secret, and Redirect URI, 
and walk you through instructions for getting your own access token for your app.

Usage
-----
    from instagram.client import InstagramAPI

    access_token = "..."
    api = InstagramAPI(access_token=access_token)
    popular_media = api.popular_media(count=20)
    for media in popular_media:
        print media.images['high_resolution'].url
