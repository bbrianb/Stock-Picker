import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as m_dates

def main():
    ticker = 'AAL'
    frame: pd.DataFrame = yf.download(ticker, start='2026-01-01', end='2026-02-26')
    series: pd.Series = frame['Close'][ticker]

    _, ax = plt.subplots()
    ax.plot(series)
    ax.xaxis.set_major_formatter(m_dates.DateFormatter('%m/%d'))
    ax.set_title(ticker)
    plt.show()

    returns: pd.Series = pd.Series()
    start_date: pd.Timestamp
    start_close: float
    start_date , start_close = next(iter(series.items()))
    returns[start_date] = 0

    for start_date, close in series.items():
        returns[start_date] = (close - start_close)/start_close

    frame[('Return', ticker)] = returns
    print(frame)

if __name__ == '__main__':
    main()