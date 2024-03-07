import pandas as pd
from datetime import datetime, timedelta

input_file_path = 'C:\\Users\\Ajit Kumar Biswas\\Desktop\\assignment1\\input.csv'
df = pd.read_csv(input_file_path)

df.columns = [col.replace(' ', '') for col in df.columns]

print(df.columns)

df['DateofJoining'] = pd.to_datetime(df['DateofJoining'])
df.sort_values(['EmployeeCode', 'DateofJoining'], inplace=True)

def calculate_dates(data):
    data['DateofExit'] = pd.to_datetime(data['DateofExit'])
    data['EndDate'] = data['DateofExit'].shift(-1) - timedelta(days=1)
    data['EndDate'].fillna(pd.to_datetime('2100-01-01'), inplace=True)
    return data

df = df.groupby('EmployeeCode', group_keys=False).apply(calculate_dates)


df.fillna(method='ffill', inplace=True)

output_columns = ['EmployeeCode', 'ManagerEmployeeCode', 'LastCompensation', 'Compensation',
                  'LastPayRaiseDate', 'VariablePay', 'TenureinOrg', 'PerformanceRating',
                  'EngagementScore', 'EffectiveDate', 'EndDate']


output_df = pd.DataFrame(columns=output_columns)

for employee_code in df['EmployeeCode'].unique():
    employee_data = df[df['EmployeeCode'] == employee_code]

    
    for i in range(len(employee_data)):
        row = employee_data.iloc[i]

        
        
        output_df = output_df.append({
            'EmployeeCode': row['EmployeeCode'],
            'ManagerEmployeeCode': row['ManagerEmployeeCode'],
            'LastCompensation': row['Compensation1'],  
            'Compensation': row['Compensation2'],       
            'LastPayRaiseDate': row['Compensation1date'],  
            'VariablePay': '',  
            'TenureinOrg': '',  
            'PerformanceRating': row['Review2'],  
            'EngagementScore': row['Engagement2'],  
            'EffectiveDate': row['DateofJoining'],
            'EndDate': row['EndDate'],
        }, ignore_index=True)

output_file_path = 'C:\\Users\\Ajit Kumar Biswas\\Desktop\\assignment1\\newoutput.csv'
output_df.to_csv(output_file_path, index=False)









