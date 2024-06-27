import pandas as pd
from pandas_timeinterval import Intervals, Interval

# Create Intervals object
intervals = Intervals(
    [
        Interval(pd.Timestamp("2021-01-01"), pd.Timestamp("2021-01-03")),
        Interval(pd.Timestamp("2021-01-02"), pd.Timestamp("2021-01-04")),
    ]
)

# Adjust intervals by adding one day
adjusted_intervals = intervals.adjust(pd.Timedelta(days=1))
print(adjusted_intervals)

# Normalize intervals to merge overlapping intervals
normalized_intervals = intervals.normalize()
print(normalized_intervals)
