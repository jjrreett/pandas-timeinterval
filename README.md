# pandas-timeinterval

A package to trim datetime indexed DataFrames and Series in pandas.

## Installation

```bash
pip install pandas-timeinterval
```

## Usage
```python
import pandas as pd
import numpy as np

# Create a time range from 0 to 1 hour, with data points every second
time_range = pd.date_range(start="2023-01-01 00:00:00", end="2023-01-01 01:00:00", freq='S')
# Create a sine wave with a period of 1 minute (60 seconds)
data = np.sin(2 * np.pi * time_range.second / 60)

# Create a DataFrame
df = pd.DataFrame(data, index=time_range, columns=["sine_wave"])

print(df.head())


from pandas_timeinterval import Intervals
df_trimed = Intervals.from_bools(df['sine_wave'] > 0.707 | df['sine_wave'] < -0.707).contract('50s').trim(df)
```

## Development

### Setting up Pre-Commit Hooks

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files # optional
```
