import yfinance as yf


def get_data(intervals = ('1m', '5m', '15m', '60m'), 
    periods = ('15m', '1d', '1d', '1d'), 
    tickers=('^NDX',), 
    rolling_long = 30, 
    rolling_short = 10) -> []:
    """
    This function returns a list of Pandas DataFrames based on queried tickers for defined intervals/periods
    """

    data_tickers = dict()

    for ticker in tickers:
        data_interval = dict()
        for interval, period in zip(intervals, periods):
            # print(ticker, interval, period)

            data_interval[interval] = yf.download(  # or pdr.get_data_yahoo(...
                    # tickers list or string as well
                    tickers = ticker,

                    # use "period" instead of start/end
                    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                    # (optional, default is '1mo')
                    period = period,

                    # fetch data by interval (including intraday if period < 60 days)
                    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                    # (optional, default is '1d')
                    interval = interval,

                    # group by ticker (to access via data['SPY'])
                    # (optional, default is 'column')
                    group_by = 'ticker',

                    # adjust all OHLC automatically
                    # (optional, default is False)
                    auto_adjust = True,

                    # download pre/post regular market hours data
                    # (optional, default is False)
                    prepost = True,

                    # use threads for mass downloading? (True/False/Integer)
                    # (optional, default is True)
                    threads = True,

                    # proxy URL scheme use use when downloading?
                    # (optional, default is None)
                    proxy = None,

                    # don't show the progress bars
                    progress = False
                )
            
            # add MAs rolling averages
            data_interval[interval][f'MA({rolling_long})'] = data_interval[interval]['Close'].rolling(window=rolling_long).mean()
            data_interval[interval][f'MA({rolling_short})'] = data_interval[interval]['Close'].rolling(window=rolling_short).mean()
            
            # add EMAs
            data_interval[interval][f'EMA({rolling_long})'] = data_interval[interval]['Close'].ewm(span=rolling_long, adjust=False).mean()
            data_interval[interval][f'EMA({rolling_short})'] = data_interval[interval]['Close'].ewm(span=rolling_short, adjust=False).mean()

        else:
            data_tickers[ticker] = data_interval
    
    return data_tickers