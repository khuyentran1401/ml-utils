# **DEMO**: ML Utilities for Fintech

Demo repository for Git submodules tutorial. Contains shared ML utilities for educational purposes.

## Features

- **Risk Scoring**: Calculate risk scores with division-by-zero protection
- **Time Features**: Extract time-based features for fraud detection
- **Velocity Calculation**: Compute transaction velocity metrics

## Usage

```python
from ml_utils.features import calculate_risk_score, extract_time_features

# Calculate risk score
risk = calculate_risk_score({'income': 50000, 'debt': 10000})

# Extract time features
df_with_time = extract_time_features(df, 'transaction_time')
```

## Functions

- `calculate_risk_score(data)` - Calculate income/debt risk ratio
- `extract_time_features(df, time_col)` - Add hour, day_of_week, is_weekend features  
- `calculate_velocity(df, user_col, time_col)` - Add transaction velocity features
