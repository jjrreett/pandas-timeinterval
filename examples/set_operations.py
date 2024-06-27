import pandas as pd
from pandas_timeinterval import Intervals

# Create two Intervals objects with datetime ranges
intervals1 = Intervals([(pd.Timestamp("2024-01-01"), pd.Timestamp("2024-01-02"))])
intervals2 = Intervals([(pd.Timestamp("2024-01-03"), pd.Timestamp("2024-01-04"))])

# Perform union operation
union_intervals = intervals1.union(intervals2)
print(union_intervals)

# Perform intersection operation
intersection_intervals = intervals1.intersection(intervals2)
print(intersection_intervals)
