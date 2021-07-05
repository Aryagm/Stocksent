
# Stocksent

<a href="https://github.com/Aryagm/Stocksent" target="blank"><img align="center" src="https://img.shields.io/badge/Stocksent-100000?style=for-the-badge&logo=github&logoColor=white" /></a>

<p align="center">
<img src="https://raw.githubusercontent.com/Aryagm/Stocksent/master/logo.png" alt="logo" width="100"/>
</p>

Stocksent is a Python library for sentiment analysis of various tickers from the latest news from trusted sources. It also has options for plotting results.

## Installation

Use the package manager [pip](https://pypi.org/project/stocksent/) to install stocksent.

```bash
pip install stocksent
```
<br />
<br />

## Usage

<br />

### Get Sentiment of single stock

```python 
from stocksent import Sentiment
stock = Sentiment('AAPL')
sentiment_score = stock.get_sentiment()
print(sentiment_score)  # Returns a float with the sentiment score.
```

```python
0.189
```
<br />

### Get Sentiment of multiple stocks

```python
from stocksent import Sentiment
stocks = Sentiment(['AAPL','TSLA','GOOG'])
sentiment_score = stocks.get_sentiment(days=4) # Get the sentiment for the past 4 days.
print(sentiment_score)  # Returns a float with the sentiment score.
```

```python
0.237
```
<br/>

### Get DataFrame of headlines, source and sentiment scores

```python
from stocksent import Sentiment
stocks = Sentiment(['AAPL','TSLA','AMZN'])
sentiment_score = stocks.get_dataframe(days=6) # Get the headlines for the past 6 days.
print(sentiment_score)  # Returns a DataFrame with headlines, source and sentiment scores.
```

```
      ticker          date	   time	                    source	                                      headline       Negative   Neutral  Positive   Overall    
  0	AAPL	2021-07-05	09:55AM	 Investor's Business Daily   Dow Jones Futures: Apple, Google, Tech Titans ...	        0.000	  1.000	    0.000    0.0000
  1	AAPL	2021-07-05	09:04AM	           The Independent   7 best VPN services for streaming and security...	        0.000	  0.645	    0.355    0.7650
  2	AAPL	2021-07-05	09:00AM	               Motley Fool   Warren Buffett Owns These Dividend-Paying Grow...	        0.000	  0.776	    0.224    0.3818
  3	AAPL	2021-07-05	06:51AM	               Motley Fool   Here's Why Bill Ackman's SPAC Deal Could Be a ...	        0.000	  0.581	    0.419    0.7579
  4	AAPL	2021-07-05	06:09AM                Barrons.com   Jeff Bezos Steps Down as CEO on Monday. Heres ...	        0.073	  0.927	    0.000   -0.0258
...	 ...	       ...	    ...	                       ...	                                           ...	          ...	    ...	      ...	...
295	AMZN	2021-06-30	12:16PM	                   Reuters   UPDATE 1-Amazon asks FTC to recuse Chairwoman ...	        0.000	  1.000	    0.000    0.0000
296	AMZN	2021-06-30	12:01PM	                   Reuters   Amazon says FTC should take new chair off its ...	        0.000	  0.841	    0.159    0.1779
297	AMZN	2021-06-30	10:13AM	               Motley Fool   3 Stocks I Would Avoid at All Costs	                0.306	  0.694	    0.000   -0.2960
298	AMZN	2021-06-30	08:43AM	             TheStreet.com   Amazon Asks FTC to Bar Chair Khan From Matters...	        0.000	  0.781     0.219    0.2023
299	AMZN	2021-06-30	08:13AM	                     Zacks   Digital Transformation Giving Cloud Business a...	        0.000	  0.495     0.505    0.6249
```

<br />

### Get plot of sentiment scores

```python
from stocksent import Sentiment
stocks = Sentiment(['AAPL','TSLA','GOOG'])
stocks.plot(save_figure=True)
```
<img src="https://raw.githubusercontent.com/Aryagm/Stocksent/master/plot.png" alt="plot" width=450/>

<br />
<br />

### Get word cloud of headlines

```python
from stocksent import Sentiment
stocks = Sentiment(['AAPL','AMZN','GOOG','TSLA'])
stocks.word_cloud(days=5) #Create a word cloud from news from the past 5 days.
```
<img src="https://raw.githubusercontent.com/Aryagm/Stocksent/master/word_cloud.png" alt="word cloud" width=450/>

<br />
<br />

## Docs
Read the docs here: [https://stocksent.readthedocs.io](https://stocksent.readthedocs.io) !
<br />
<br />

## Contributing
Pull requests are welcome on [GitHub](https://github.com/Aryagm/Stocksent) !

<br />

## License
[Mozilla Public License
Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)

<br />

## Author
**Arya Manjaramkar**

<a href="https://www.linkedin.com/in/arya-manjaramkar" target="blank"><img align="center" src="https://img.shields.io/badge/Arya Manjaramkar-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>  &nbsp;&nbsp;&nbsp;       <a href="https://www.github.com/Aryagm" target="blank"><img align="center" src="https://img.shields.io/badge/Aryagm-100000?style=for-the-badge&logo=github&logoColor=white" /></a>

<br/>

### Disclaimer
<i>
The material in this repository is purely for educational purposes and should not be taken as professional investment advice. Invest at your own discretion.
</i>