import sys
import time
import getpass
import unittest
from instagram import *

try:
    from test_settings import *
except Exception:
    print "Must have a test_settings.py file with settings defined"
    sys.exit(1)


class TestInstagramAPI(InstagramAPI):
    host = test_host
    base_path = test_base_path
    access_token_field = "access_token"
    authorize_url = test_authorize_url
    access_token_url = test_access_token_url
    protocol = test_protocol


class InstagramAuthTests(unittest.TestCase):
    def setUp(self):
        self.unauthenticated_api = TestInstagramAPI(client_id=client_id, redirect_uri=redirect_uri, client_secret=client_secret)

    def test_authorize_login_url(self):
        redirect_uri = self.unauthenticated_api.get_authorize_login_url()
        assert redirect_uri
        print "Please visit and authorize at:\n%s" % redirect_uri
        code = raw_input("Paste received code (blank to skip): ").strip()
        if not code:
            return

        access_token = self.unauthenticated_api.exchange_code_for_access_token(code)
        assert access_token

    def test_xauth_exchange(self):
        """ Your client ID must be authorized for xAuth access; email
            xauth@instagram.com for access"""
        username = raw_input("Enter username for XAuth (blank to skip): ").strip()
        if not username:
            return
        password =  getpass.getpass("Enter password for XAuth (blank to skip): ").strip()
        access_token = self.unauthenticated_api.exchange_xauth_login_for_access_token(username, password)
        assert access_token


class InstagramAPITests(unittest.TestCase):

    def setUp(self):
        self.client_only_api = TestInstagramAPI(client_id=client_id)
        self.api = TestInstagramAPI(access_token=access_token)

    def test_popular_media(self):
        self.api.popular_media(count=10)

    def test_media_search(self):
        self.client_only_api.media_search(ll='37.7,-122.22')
        self.api.media_search(ll='37.7,-122.22')

    def test_media_search_without_ll(self):
        self.assertRaises(InstagramAPIError, self.api.media_search)

    def test_user_feed(self):
        self.api.user_media_feed(count=50)

    def test_generator_user_feed(self):
        generator = self.api.user_media_feed(as_generator=True, max_pages=3, count=2)
        for page in generator:
            str(generator)

    def test_user_recent_media(self):
        self.api.user_recent_media(count=10)

    def test_user_search(self):
        self.api.user_search('mikeyk', 10)

    def test_user_follows(self):
        for page in self.api.user_followed_by(as_generator=True):
            str(page)

    def test_user_followed_by(self):
        for page in self.api.user_followed_by(as_generator=True):
            str(page)

    def test_other_user_followed_by(self):
        self.api.user_followed_by(user_id=3)

    def test_self_info(self):
        self.api.user()
        self.assertRaises(InstagramAPIError, self.client_only_api.user)

    def test_location_recent_media(self):
        self.api.location_recent_media(location_id=1)

    def test_location_search(self):
        self.api.location_search(ll='37.7,-122.22', distance=2500)

    def test_location(self):
        self.api.location(1)

    def test_tag_recent_media(self):
        self.api.tag_recent_media(tag_name='1', count=5)

    def test_tag_recent_media_paginated(self):
        for page in self.api.tag_recent_media(tag_name='1', count=5, as_generator=True, max_pages=2):
            str(page)

    def test_tag_search(self):
        self.api.tag_search("coff")

    def tag(self):
        self.api.tag("coffee")

if __name__ == '__main__':
    unittest.main()

