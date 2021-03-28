import logging


class HeadlinesModel(object):

    def __init__(self,
                 q=None,
                 qintitle=None,
                 sources=None, 
                 language="en", 
                 country=None, 
                 category=None, 
                 page_size=None, 
                 page=None
                 ):

        self.q = q
        self.qintitle = qintitle
        self.sources = sources
        self.language = language
        self.country = country
        self.category = category
        self.page_size = page_size
        self.page = page


    def __repr__(self):
        return "{%s}" % f"q: {self.q}, qintitle: {self.qintitle}, sources: {self.sources}, language: {self.language}, country: {self.country}, category: {self.category}, page_size: {self.page_size}, page: {self.page}"

    def as_key(self):
        return f"top_headlines_q_{self.q}_qintitle_{self.qintitle}_sources_{self.sources}_language_{self.language}_country_{self.country}_category_{self.category}_page_size_{self.page_size}_page_{self.page}"

    def as_dict(self):
        return self.__dict__


class SourcesModel(object):

    def __init__(self,
                 q: str = None,
                 sources: str = None,
                 category: str = None,
                 country: str = None,
                 language: str = 'en'):
        self.q = q
        self.sources = sources
        self.category = category
        self.country = country
        self.language = language

    def __repr__(self):
        return "{%s}" % f"q: {self.q}, sources: {self.sources}, category: {self.category}, country: {self.country}, language: {self.language}"

    def as_key(self):
        return f"top_headlines_q_{self.q}_sources_{self.sources}_category_{self.category}_country_{self.country}_language_{self.language}"

    def as_dict(self):
        return self.__dict__
