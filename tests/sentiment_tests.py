import unittest
from stocksent import Sentiment
from stocksent.get_sentiment_data import get_sentiment_data

columns_get_sentiment_data = ['ticker', 'date', 'time', 'source', 'headline']

columns_get_dataframe = ['ticker', 'date', 'time', 'source', 'headline', 'Negative', 'Neutral', 'Positive', 'Overall']


class TestGetSentimentData(unittest.TestCase):
    def test_return_type(self):
        result = get_sentiment_data('AAPL')
        self.assertEqual(str(type(result)), "<class 'pandas.core.frame.DataFrame'>")

    def test_return_type_list(self):
        result = get_sentiment_data(['AAPL', 'TSLA', 'GOOG'])
        self.assertEqual(str(type(result)), "<class 'pandas.core.frame.DataFrame'>")

    def test_return_columns(self):
        result = get_sentiment_data('AAPL')
        self.assertEqual(list(result.columns), columns_get_sentiment_data)

    def test_return_columns_list(self):
        result = get_sentiment_data(['AAPL', 'TSLA', 'GOOG'])
        self.assertEqual(list(result.columns), columns_get_sentiment_data)

    def test_check_df_length(self):
        result = get_sentiment_data('AAPL')
        self.assertGreaterEqual(len(result.index), 99)

    def test_check_df_length_list(self):
        result = get_sentiment_data(['AAPL', 'GOOG', 'TSLA'])
        self.assertGreaterEqual(len(result.index), 299)


class TestSentiment(unittest.TestCase):

    def test_return_float(self):
        stock = Sentiment('AAPL')
        result = stock.get_sentiment()
        self.assertEqual(str(type(result)), "<class 'float'>")

    def test_return_float_list(self):
        stock = Sentiment(['AAPL', 'GOOG', 'TSLA'])
        result = stock.get_sentiment()
        self.assertEqual(str(type(result)), "<class 'float'>")

    def test_return_range(self):
        stock = Sentiment('AAPL')
        result = stock.get_sentiment()
        self.assertGreaterEqual(result, -1)
        self.assertLessEqual(result, 1)

    def test_return_range_list(self):
        stock = Sentiment(['AAPL', 'GOOG', 'TSLA'])
        result = stock.get_sentiment()
        self.assertGreaterEqual(result, -1)
        self.assertLessEqual(result, 1)

    def test_get_dataframe_columns(self):
        stock = Sentiment('AAPL')
        result = stock.get_dataframe()
        self.assertEqual(list(result.columns), columns_get_dataframe)

    def test_get_dataframe_columns_list(self):
        stock = Sentiment(['AAPL', 'GOOG', 'TSLA'])
        result = stock.get_dataframe()
        self.assertEqual(list(result.columns), columns_get_dataframe)

    def test_nan_values(self):
        stock = Sentiment('AAPL')
        result = stock.get_dataframe()
        self.assertEqual(str(result.isnull().values.any()), "False")

    def test_nan_values_list(self):
        stock = Sentiment(['AAPL', 'GOOG', 'TSLA'])
        result = stock.get_dataframe()
        self.assertEqual(str(result.isnull().values.any()), "False")

    def test_nan_values_days(self):
        stock = Sentiment('AAPL')
        result = stock.get_dataframe(days=3)
        self.assertEqual(str(result.isnull().values.any()), "False")

    def test_nan_values_list_days(self):
        stock = Sentiment(['AAPL', 'GOOG', 'TSLA'])
        result = stock.get_dataframe(days=3)
        self.assertEqual(str(result.isnull().values.any()), "False")


if __name__ == '__main__':
    unittest.main()
