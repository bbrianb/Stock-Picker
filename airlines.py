import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as m_dates
from matplotlib.ticker import MaxNLocator, PercentFormatter

def main():
    tickers = 'AAL', 'DAL'
    frame: pd.DataFrame = yf.download(tickers, start='2026-01-01', end='2026-03-07')

    for ticker in tickers:
        series: pd.Series = frame['Close'][ticker]

        returns: pd.Series = pd.Series()
        start_date: pd.Timestamp
        start_close: float
        start_date , start_close = next(iter(series.items()))
        returns[start_date] = 0

        for start_date, close in series.items():
            returns[start_date] = (close - start_close)/start_close

        frame[('Return', ticker)] = returns

    _, ax = plt.subplots(figsize=(6, 3))
    ax.plot(frame['Return']['AAL'], label='AAL')
    ax.plot(frame['Return']['DAL'], label='DAL')
    ax.xaxis.set_major_formatter(m_dates.DateFormatter('%m/%d'))
    ax.yaxis.set_major_formatter(PercentFormatter(1, 0))
    ax.set_title('AAL vs DAL')
    ax.grid(axis='y', linestyle='-', alpha=0.6)
    ax.xaxis.set_major_locator(MaxNLocator(4))
    ax.legend()
    plt.show()

    print(frame)

if __name__ == '__main__':
    main()