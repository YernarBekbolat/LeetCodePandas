import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(left='employee', right=bonus, how='left', on='empId').query("(bonus < 1000) | bonus.isna()")[['name', 'bonus']]