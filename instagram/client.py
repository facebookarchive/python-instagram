import oauth2
from bind import bind_method
import simplejson
from models import Image, Media, User, Location, Tag

MEDIA_ACCEPT_PARAMETERS = ["count", "max_id"]
SEARCH_ACCEPT_PARAMETERS = ["q", "count"]

SUPPORTED_FORMATS = ['json']

class InstagramAPI(oauth2.OAuth2API):
        
    host = "api-privatebeta.instagr.am"
    base_path = "/v2"
    access_token_field = "access_token"
    authorize_url = "http://api-privatebeta.instagr.am/oauth/authorize"
    access_token_url = "http://api-privatebeta.instagr.am/oauth/access_token"
    protocol = "http"

    def __init__(self, *args, **kwargs):
        format = kwargs.get('format', 'json')
        if format in SUPPORTED_FORMATS:
            self.format = format
        else:
            self.format = SUPPORTED_FORMATS[0]
        super(InstagramAPI, self).__init__(*args, **kwargs)


    media_popular = bind_method(
                path = "/media/popular",
                accepts_parameters = MEDIA_ACCEPT_PARAMETERS,
                root_class = Media)

    media_search = bind_method(
                path = "/media/search",
                accepts_parameters = SEARCH_ACCEPT_PARAMETERS + ['ll'],
                root_class = Media)
    
    user_media_feed = bind_method(
                path = "/users/self/feed",
                accepts_parameters = MEDIA_ACCEPT_PARAMETERS,
                root_class = Media,
                paginates = True)

    user_recent_media = bind_method(
                path = "/users/{user_id}/media/recent",
                accepts_parameters = MEDIA_ACCEPT_PARAMETERS + ['user_id'],
                root_class = Media,
                paginates = True)

    user_search = bind_method(
                path = "/users/search",
                accepts_parameters = SEARCH_ACCEPT_PARAMETERS,
                root_class = User)

    user_follows = bind_method(
                path = "/users/{user_id}/follows/users",
                accepts_parameters = ["user_id"],
                root_class = User)

    user_followed_by = bind_method(
                path = "/users/{user_id}/followed-by/users",
                accepts_parameters = ["user_id"],
                root_class = User)

    user = bind_method(
                path = "/users/{user_id}",
                accepts_parameters = ["user_id"],
                root_class = User,
                root_type = "entry")
    
    location_recent_media = bind_method(
                path = "/locations/{location_id}/media/recent",
                accepts_parameters = MEDIA_ACCEPT_PARAMETERS + ['location_id'],
                root_class = Media,
                paginates = True)

    location_search = bind_method(
                path = "/locations/search",
                accepts_parameters = ['ll', 'count'],
                root_class = Location)

    location = bind_method(
                path = "/locations/{location_id}",
                accepts_parameters = ["location_id"],
                root_class = Location,
                root_type = "entry")


    tag_recent_media = bind_method(
                path = "/tags/{tag_name}/media/recent",
                accepts_parameters = MEDIA_ACCEPT_PARAMETERS + ['tag_name'],
                root_class = Media,
                paginates = True)

    tag_search = bind_method(
                path = "/tags/search",
                accepts_parameters = SEARCH_ACCEPT_PARAMETERS,
                root_class = Tag,
                paginates = True)

    tag = bind_method(
                path = "/tags/{tag_name}",
                accepts_parameters = ["tag_name"],
                root_class = Tag,
                root_type = "entry")
