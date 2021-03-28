
import logging

from pprint import pprint as ppr

from Redis import init_redis
from Models import HeadlinesModel, SourcesModel
from NewsScrapper import NewsScrapper


class NewsReader(object):
    def __init__(self):
        logging.info('ScrapNewsToRedis')
        self.redis = init_redis()

    def get_top_headlines(self, params: HeadlinesModel):
        logging.info(f'Redis get top_headlines with size: ', )

        key = params.as_key()
        logging.info("KEY>>> %s", key)
        if self.redis.exists(key):
            logging.info(f'Read cached top headlines: ', )
            # TODO reload outdated news
            return self.redis.get(key)
        else:
            logging.info(f'Scrap and cache top headlines: ', )
            return NewsScrapper(self.redis).scrap_top_headlines(params)
        
        # logging.info(f'Redis assert that set == get for ${key}: ')
        # logging.info('... %s', cmp_nested_dicts(eval(val), eval(result)))
    def get_sources(self, params: SourcesModel):
        pass