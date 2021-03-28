import datetime
import logging
import redis as Redis
from newsapi import NewsApiClient

from Models import HeadlinesModel, SourcesModel
from Redis import init_redis

FUNC_NAME = "NEWS API"

NEWS_API_KEY = '6aab955601ae425d9c7ad00e4a2ae51b'

def cmp_nested_dicts(d1, d2, path=""):
    for k in d1:
        if (k not in d2):
            # logging.info (path, ":")
            # logging.info (k + " as key not in d2", "\n")
            return False
        else:
            if type(d1[k]) is dict:
                if path == "":
                    path = k
                else:
                    path = path + "->" + k
                cmp_nested_dicts(d1[k],d2[k], path)
            else:
                if d1[k] != d2[k]:
                    return False
                    # logging.info (path, ":")
                    # logging.info (" - ", k," : ", d1[k])
                    # logging.info (" + ", k," : ", d2[k])
    return True

class NewsScrapper(object):
    def __init__(self, redis = None):
        logging.info('ScrapNewsToRedis')

        self.redis = init_redis(redis)
        self.init_news_api()
        
    def init_news_api(self):
        logging.info('Init News-Api')
        self.newsApi = NewsApiClient(api_key=NEWS_API_KEY)

    def scrap_top_headlines(self, params = None):
        if not params:
            params = HeadlinesModel()
        
        key = params.as_key()

        logging.info(f'News-Api download top headlines by params <{params.as_dict()}> with size: ')
        payload = self.newsApi.get_top_headlines(**params.as_dict())
        payloadStr = str(payload)
        logging.info('... %s', len(payloadStr))

        logging.info('Save news top headlines to redis: ')
        result = self.redis.set(key, payloadStr)
        logging.info('... %s', result)

        # self.check_for('top_headlines', payload)
        return payload

    # def set_sources(self):
    #     if not key:
    #         key = SourcesModel().as_key()

    #     logging.info('News-Api download news sources')
    #     payload = str(self.newsApi.get_sources())
    #     logging.info('... %s', len(payload))

    #     logging.info('Save news sources to redis: ')
    #     result = self.redis.set('sources', payload)
    #     logging.info('... %s', result)

        # self.check_for('sources', payload)

    # def check_for(self, key: str, val: str):
    #     logging.info(f'Redis get ${key} with size: ', )
    #     result = self.redis.get(key)

    #     logging.info(f'Redis assert that set == get for ${key}: ')
    #     logging.info('... %s', cmp_nested_dicts(eval(val), eval(result)))