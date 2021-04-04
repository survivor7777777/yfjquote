# Copyright (C) 2021 @survivor7777777
# See LICENSE for details.

import requests
import lxml.html as html

from .utils import constant as C
from .utils import random_user_agent, remove_commas

def get_stock_countries_list():
    return C.STOCK_COUNTRIES.keys()

def get_stock_quote(symbol, country='jp'):
    """
    """
    if not symbol:
        raise ValueError("ERR#0001: symbol parameter is mandatory and must be a valid stock symbol.")

    country_obj = C.STOCK_COUNTRIES[country]
    if not country_obj:
        raise ValueError("ERR#0002: unknown country")

    url = country_obj['url'].format(symbol)

    headers = {
        'User-Agent': random_user_agent(),
        'Accept': 'text/html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    req = requests.get(url, headers=headers)

    if req.status_code != 200:
        raise ConnectionError("ERR#0003: HTTP error ({})".format(req.status_code))

    root = html.fromstring(req.text)
    func = country_obj['parser']
    if not func:
        raise RuntieError('ERR#0004: internal error: no suitable html parser')
    
    return func(symbol, root)

def parse_html_jp(symbol, root):
    # new format since 2021/03/23
    path = root.xpath(".//main//div[@class='_1nb3c4wQ']")
    if path:
        name = path[0].xpath(".//h1")[0].text_content()
        quote = path[0].xpath(".//span[@class='_3rXWJKZF']")[0].text_content()
        ret = {
            'symbol': symbol,
            'name': name,
            'quote': remove_commas(quote)
        }
        return ret

    # ETF etc
    path = root.xpath(".//div[@id='stockinf']")
    if path:
        name = path[0].xpath(".//th[@class='symbol']")[0].text_content()
        quote = path[0].xpath(".//td[@class='stoksPrice']")[0].text_content()
        ret = {
            'symbol': symbol,
            'name': name,
            'quote': remove_commas(quote)
        }
        return ret

    raise ValueError("ERR#0003: unknown symbol")

def parse_html_us(symbol, root):
    path = root.xpath(".//table[@class='stocksTable']")
    if path:
        name = path[0].xpath(".//th[@class='symbol']")[0].text_content()
        quote = path[0].xpath(".//td[@class='stoksPrice']")[0].text_content()
        ret = {
            'symbol': symbol,
            'name': name,
            'quote': remove_commas(quote)
        }
        return ret

    raise ValueError("ERR#0003: unknown symbol")

C.STOCK_COUNTRIES['jp']['parser'] = parse_html_jp
C.STOCK_COUNTRIES['us']['parser'] = parse_html_us
