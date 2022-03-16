#!/usr/bin/env python3
""" Module to do implementing an
    expiring web cache and tracker - Advanced task """

import redis
import requests
from typing import Callable
from functools import wraps

re = redis.Redis()


def counter_request(method: Callable) -> Callable:
    """ Counter to the have the request done
    """

    @wraps(method)
    def wrapper(url):
        """ Useful to use functool.wraps to conserve the
            original function’s name, docstring, etc.
        """
        re.incr("count:{}".format(url))
        cached_HTML_content = re.get("cached:{}".format(url))
        if cached_HTML_content:
            return cached_HTML_content.decode('utf-8')

        html = method(url)
        re.setex("cached:{}".format(url), 10, html)
        return html

    return wrapper


@counter_request
def get_page(url: str) -> str:
    """ It uses the requests module to obtain the HTML
        content of a particular URL and returns it.
    """
    req = requests.get(url)
    return req.text
