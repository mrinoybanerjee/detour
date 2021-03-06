import requests

proxies = None

def get(url, params = None, headers = None):
    r = requests.get(url, params=params, headers=headers, proxies=proxies)
    return r

def post(url, data = None, headers = None):
    r = requests.post(url, data=data, headers=headers, proxies=proxies)
    return r

class Result(object):
    __slots__ = ('url', 'title', 'desc', 'thumbnail', 'source', 'album', 'tags', 'license', 'price',)
    def __init__(self, url, title, desc, thumbnail=None, source=None):
        self.url = url
        self.title = title
        self.desc = desc
        self.thumbnail = thumbnail
        self.source = source

        self.album = None
        self.tags = None
        self.license = None
        self.price = None


    def __repr__(self):
        return 'Result(%s)' % (
            ', '.join((x + '=' + repr(getattr(self, x)) for x in self.__slots__))
        )

    def __str__(self):
        s = ''
        for attr in self.__slots__:
            if attr != 'thumbnail':
                val = getattr(self, attr)
                if val:
                    s += str(val) + ', '
        return s

    def __eq__(self, other):
        return self.url == other.url

    def __hash__(self):
        return hash(self.url)

    def __lt__(self, other):
        return 0

    def __gt__(self, other):
        return 0

    def items(self):
        return {x: getattr(self, x) for x in self.__slots__}
