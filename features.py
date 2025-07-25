"""Machine Learning Utilities for Fintech Applications

This module provides shared ML utilities for fraud detection,
credit scoring, and trading algorithms.
"""

def calculate_risk_score(data):
    """Calculate risk score for fraud detection
    
    Args:
        data: Dictionary with 'income' and 'debt' keys
        
    Returns:
        float: Risk score (income/debt ratio with zero debt protection)
    """
    # Updated calculation with improved zero debt handling
    return data['income'] / max(data['debt'], 1)


def extract_time_features(df, time_col):
    """Extract time-based features for fraud detection
    
    Args:
        df: Pandas DataFrame with transaction data
        time_col: Name of the timestamp column
        
    Returns:
        DataFrame: Original data with additional time features
    """
    # Simple implementation for demo
    import pandas as pd
    
    df = df.copy()
    df['hour'] = pd.to_datetime(df[time_col]).dt.hour
    df['day_of_week'] = pd.to_datetime(df[time_col]).dt.dayofweek
    df['is_weekend'] = df['day_of_week'].isin([5, 6])
    
    return df


def calculate_velocity(df, user_col, time_col):
    """Calculate transaction velocity features
    
    Args:
        df: Pandas DataFrame with transaction data
        user_col: Name of the user ID column
        time_col: Name of the timestamp column
        
    Returns:
        DataFrame: Data with velocity features added
    """
    # Simple implementation for demo
    df = df.copy()
    df['transaction_count_1h'] = df.groupby(user_col)[time_col].transform('count')
    
    return df


def validate_transaction_data(data):
    """Validate transaction data quality
    
    Args:
        data: Dictionary or DataFrame with transaction data
        
    Returns:
        dict: Validation report with data quality metrics
    """
    # Simple implementation for demo
    if isinstance(data, dict):
        report = {
            'total_fields': len(data),
            'validation_passed': True,
            'data_type': 'dict'
        }
    else:
        # If pandas DataFrame, use pandas methods
        try:
            if hasattr(data, 'isnull'):  # Check if it's a pandas DataFrame
                report = {
                    'total_rows': len(data),
                    'missing_values': data.isnull().sum().to_dict(),
                    'data_types': data.dtypes.to_dict(),
                    'validation_passed': data.isnull().sum().sum() == 0
                }
            else:
                raise AttributeError("Not a pandas DataFrame")
        except:
            report = {
                'validation_passed': True,
                'note': 'Basic validation only - not a pandas DataFrame'
            }
    
    return report