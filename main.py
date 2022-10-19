import datetime as dt
from datetime import datetime, timedelta
from fastquant import get_crypto_data
import pandas as pd

date = dt.date.today() - pd.offsets.DateOffset(years=1)

# df = get_crypto_data("BTC/USDT", "2019-05-01", "2020-08-20")
print(datetime.today().date)
print(date)