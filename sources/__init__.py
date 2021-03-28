
import logging
import azure.functions as func

from Models import HeadlinesModel
from NewsReader import NewsReader


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # if req.method == "GET":
        # params = HeadlinesModel(**req.params)
        # newsReader = NewsReader()
        # print(params)
        # topHeadlines = newsReader.get_top_headlines(params)
        # return func.HttpResponse(body=topHeadlines)
    # else:
    return func.HttpResponse(
            "Sorry not implemented. Bad request. Only GET allowed.",
            status_code=400
        )
