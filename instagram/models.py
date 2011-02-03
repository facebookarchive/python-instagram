from helper import timestamp_to_datetime

class Image(object):
    
    def __init__(self, url, width, height):
        self.url = url
        self.height = height
        self.width = width

class Media(object):

    def __init__(self, id=None, **kwargs):
        self.id = id
        for key,value in kwargs.iteritems():
            setattr(self, key, value)
    
    def get_standard_resolution_url(self):
        return self.images['standard_resolution'].url
    
    @classmethod
    def object_from_dictionary(cls, entry):
        new_media = Media(id=entry['id'])
        
        new_media.user = User.object_from_dictionary(entry['user'])
        new_media.images = {}
        for version,version_info in entry['images'].iteritems():
            new_media.images[version] = Image(**version_info)

        if 'user_has_liked' in entry:
            new_media.user_has_liked = entry['user_has_liked']
        new_media.like_count = entry['likes']['count']
        
        new_media.comment_count = entry['comments']['count']
        new_media.comments = []
        for comment in entry['comments']['data']:
            new_media.comments.append(Comment.object_from_dictionary(comment))

        new_media.created_time = timestamp_to_datetime(entry['created_time'])

        if entry['location']:
            new_media.location = Location.object_from_dictionary(entry['location'])

        new_media.link = entry['link']

        return new_media

class Tag(object):
    def __init__(self, name, **kwargs):
        self.name = name
        for key,value in kwargs.iteritems():
            setattr(self, key, value)
        
    @classmethod
    def object_from_dictionary(cls, entry):
        return cls(**entry)

    def __str__(self):
        return "Tag %s" % self.name

class Comment(object):
    def __init__(self, *args, **kwargs):
        for key,value in kwargs.iteritems():
            setattr(self, key, value)

    @classmethod
    def object_from_dictionary(cls, entry):
        user = User.object_from_dictionary(entry['from'])
        text = entry['text']
        created_at = timestamp_to_datetime(entry['created_time'])
        id = entry['id']
        return Comment(id, user, text, created_at)

    def __unicode__(self):
        print "%s said \"%s\"" % (self.user.username, self.message)

class Point(object):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class Location(object):
    def __init__(self, id, *args, **kwargs):
        self.id = id
        for key,value in kwargs.iteritems():
            setattr(self, key, value)

    @classmethod
    def object_from_dictionary(cls, entry):
        point = None
        if entry['latitude']:
            point = Point(entry['latitude'],
                          entry['longitude'])
        location = cls(entry['id'],
                       point,
                       name=entry['name'])
        return location
         
class User(object):

    def __init__(self, id, *args, **kwargs):
        self.id = id
        for key,value in kwargs.iteritems():
            setattr(self, key, value)

    @classmethod
    def object_from_dictionary(cls, entry):
        new_user = cls(**entry)
        return new_user

    def __str__(self):
        return "User %s" % self.username

        

