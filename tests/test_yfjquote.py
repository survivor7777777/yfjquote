#!/usr/bin/env python

import pytest

import yfjquote

def test_yfjquote():
    print(yfjquote.__author__)
    print(yfjquote.__version__)

def test_yfjquote_get_stock_countries_list():
    countries = yfjquote.get_stock_countries_list()
    for c in countries:
        print(c)

def test_yfjquote_get_stock_quote_jp():
    symbols = [ '7203', '3068', '4502', '1545', '1328' ]
    for s in symbols:
        q = yfjquote.get_stock_quote(s)
        print(q)

def test_yfjquote_get_stock_quote_us():
    symbols = [ 'GOOG', 'AAPL' ]
    for s in symbols:
        q = yfjquote.get_stock_quote(s, 'us')
        print(q)

if __name__ == '__main__':
    test_yfjquote()
    test_yfjquote_get_stock_countries_list()
    test_yfjquote_get_stock_quote_jp()
    test_yfjquote_get_stock_quote_us()
