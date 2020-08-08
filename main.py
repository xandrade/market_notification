from datetime import datetime, timedelta, date, time
import time
import sched

from pytz import timezone
import numpy as np
import yfinance as yf
from notify_run import Notify 

import data

notify = Notify()
notify.endpoint = 'https://notify.run/9rIXhJ9MVTZjzOBN'


def nasdaq_market_open() -> bool: 
    """Check if Nasdaq Stock Markets market is open for trading
    https://www.nasdaq.com/stock-market-trading-hours-for-nasdaq
    https://www.nasdaq.com/nasdaq-2020-holiday-hours-trading-schedule
    """

    now = datetime.now(timezone('US/Eastern'))
    t = now.time().replace(microsecond=0)
    d = now.weekday()
    if now.month == 1 and now.day == 1: return False  # New Year's Day	Wednesday, January 1
    elif now.month == 1 and now.day == 20: return False  # Martin Luther King, Jr. Day	Monday, January 20
    elif now.month == 2 and now.day == 17: return False  # Presidents' Day	Presidents' Day, February 17
    elif now.month == 4 and now.day == 10: return False  # Good Friday	Friday, April 10
    elif now.month == 5 and now.day == 25: return False  # Memorial Day	Monday, May 25
    elif now.month == 7 and now.day == 3: return False  # Independence Day	Friday, July 3
    elif now.month == 9 and now.day == 7: return False  # Labor Day	Monday, September 7
    elif now.month == 11 and now.day == 26: return False  # Thanksgiving Day	Thursday, November 26
    elif now.month == 12 and now.day == 25: return False  # Christmas Day	Friday, December 25
    elif d == 5 or d == 6: return False  # Saturday and Sunday are closed 
    elif time(9, 30, 0, timezone('US/Eastern')) <= t <= time(4, 0, 0, timezone('US/Eastern')): return True  # Market is open
    else: return False



"""
Push notifications
curl https://notify.run/9rIXhJ9MVTZjzOBN -d "^NDX (1m) important volume change. %Change: 818.82, Diff: 162618, Volumes: (t-1) 19860, (t) 182478"
"""

if __name__ == "__main__":
    
    s = sched.scheduler(time.time, time.sleep)

    def run_task(sc): 
        
        print("Running Task", datetime.now(), end='\r')

        ticker = '^NDX'
        interval = '1m'

        if not nasdaq_market_open():

            intervals = ('1m', '5m', '15m', '60m')
            periods = ('3m', '15m', '45m', '3d')
            tickers=('^NDX',)

            data_tickers = data.get_data(intervals=intervals)

            x = data_tickers[ticker][interval].tail(2)
            volumes = x['Volume'].values
            volumes_diff = np.diff(volumes)
            volumes_pct_change = np.diff(volumes) / volumes[:1] * 100

            for interval in intervals:
                x = data_tickers[ticker][interval].tail(2)
                volumes = x['Volume'].values
                volumes_diff = np.diff(volumes)
                volumes_pct_change = np.diff(volumes) / volumes[:1] * 100

                # print(x)
                #if market_open():
                if volumes_pct_change > 500 and volumes[-1] > 100000:
                    msg = f'{ticker} ({interval}) %Change: {volumes_pct_change.item() :.2f}, Diff: {volumes_diff.item()}, Volumes: (t-1) {volumes[0]}, (t) {volumes[1]}'
                    print(msg)
                    #notify.send(msg)

        print("Last Run Time", datetime.now(), flush=True)

        s.enter(60, 1, run_task, (sc,))

    s.enter(0, 1, run_task, (s,))
    s.run()
