# imports
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen, Request
from os import path

HERE = path.abspath(path.dirname(__file__))


class ValueNotFound(Exception):
    """Exception raised when no value or list of values is given to the function.
    """

    def __init__(self, tickers, message="No value or list of values given to the function."):
        self.tickers = tickers
        self.message = message
        super().__init__(self.message)


class TickerNotFound(Exception):
    """Exception raised when the ticker given is not in the NASDAQ, AMEX or NYSE.
    """

    def __init__(self, tickers, message="Ticker not found in the NASDAQ, AMEX or NYSE."):
        self.tickers = tickers
        self.message = message
        super().__init__(self.message)


class InvalidDataType(Exception):
    """Exception raised when the ticker given is not a string or list.
    """

    def __init__(self, tickers, message="Invalid input data-type. Input should be string or list."):
        self.tickers = tickers
        self.message = message
        super().__init__(self.message)


with open(path.join(HERE, 'stock_list.txt')) as text_file:
    stock_list = [line.strip() for line in text_file.readlines()]

# text_file = open("stock_list.txt", 'r')
# stock_list = [line.strip() for line in text_file.readlines()]
web_url = 'https://finviz.com/quote.ashx?t='


def get_sentiment_data(tickers):
    """
    Returns dataframe of given ticker(s) with date, time, headlines and source.

    :param tickers: The ticker or list of tickers.
    :type tickers: str/list
    """
    if len(tickers) == 0 or tickers is None or len(str(tickers).strip()) == 0:
        raise ValueNotFound(tickers)

    if type(tickers) != str and type(tickers) != list:
        raise InvalidDataType(tickers)

    if type(tickers) == str:
        tickers  = [tickers]
    tickers = [x.upper() for x in tickers]
    for x in tickers:
        if x not in stock_list:
            raise TickerNotFound(tickers)
    news_tables = {}
    for tick in tickers:
        url = web_url + tick
        req = Request(url=url, headers={"User-Agent": "FireFox"})
        response = urlopen(req)
        html = BeautifulSoup(response, "html.parser")
        news_table = html.find(id='news-table')
        news_tables[tick] = news_table
    news_list = []

    for file_name, news_table in news_tables.items():
        for i in news_table.findAll('tr'):

            text = i.a.get_text()

            date_scrape = i.td.text.split()
            source = i.div.span.get_text()

            if len(date_scrape) == 1:
                time = date_scrape[0]

            else:
                date = date_scrape[0]
                time = date_scrape[1]

            tick = file_name.split('_')[0]

            news_list.append([tick, date, time, source, text])
    columns = ['ticker', 'date', 'time', 'source', 'headline']
    news_df = pd.DataFrame(news_list, columns=columns)
    news_df['date'] = pd.to_datetime(news_df.date).dt.date
    return news_df
