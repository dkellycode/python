import pandas as pd
import tkinter as tk
from tkinter import simpledialog

def __main__():

    root = tk.Tk()
    root.withdraw()  # Hide the main window

    region = simpledialog.askstring("Input", "Please enter Region:", parent=root)

    # region = input('Please enter Region')

    datasource = pd.read_clipboard()

    datasource['Created'] = pd.to_datetime(datasource['Created'], format='%d/%m/%Y', dayfirst=True)
    datasource.set_index('Created', inplace=True)
    datasource['Week'] = datasource.index.to_period('W').start_time.strftime('%d/%m/%Y')
    datasource = datasource.sort_values('Week')
    for column in ['Total', 'Balance']:
        datasource[column] = datasource[column].str.replace('$', '').str.replace(',', '').astype(float)
    datasource['Total for week'] = datasource.groupby('Week')['Total'].transform('sum')

    weekly_totals = datasource.groupby('Week')['Total'].sum().reset_index()
    weekly_totals = weekly_totals.rename(columns={'Total': 'Weekly_Total'})

    # datasource.to_excel(f'/Users/d3ops/Documents/{region}_Ecomm_weekly_sales.xlsx')
    weekly_totals.to_excel(f'/Users/d3ops/Documents/{region}_Ecomm_weekly_totals.xlsx')
    print(weekly_totals)

    return 0

if __name__ == "__main__":
    __main__()

