import pandas as pd
from pandas_timeinterval import Intervals

# Create a sample DataFrame
sample_data = pd.Series(
    [1, 2, 3, 4, 5], index=pd.date_range(start="2021-01-01", periods=5, freq="D")
)

# Create an Intervals object
intervals = Intervals([(pd.Timestamp("2021-01-02"), pd.Timestamp("2021-01-03"))])

# Trim the data
trimmed_data = intervals.trim(sample_data)

print(trimmed_data)
