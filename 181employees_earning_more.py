import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee[employee['salary'] > employee['managerId'].map(employee.set_index('id')['salary'])]
    df = df[['name']].rename(columns = {'name' : 'Employee'})
    return df