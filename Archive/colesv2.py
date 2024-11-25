# %%

import pandas as pd
import re
from tkinter.filedialog import askopenfilename
from datetime import datetime

file_path = askopenfilename()
df = pd.read_csv(file_path, encoding='utf-8')

acct_code_dict = {
    9421903673244: 227010725,
    9421903673220: 225110726,
    9421905741828: 225510725,
    9421903673206: 223010725,
    9421034850477: 224110725,
    9421905131841: 221010725,
    9421034854208: 284110725
    }

po_number = df.iloc[1, 0]
po_date = df.iloc[1, 2]
deldate = df.iloc[1, 5]
shipdc = df.iloc[1, 10]
netprice = df.iloc[1, 92]

def format_date(date_string):
    return datetime.strptime(date_string, '%Y%m%d').strftime('%d/%m/%Y')

item_list = []
total_rows = len(df)
for row in range(1, (total_rows)):
    contactname = 'Coles - Grocery Holdings Pty Limited'
    emailaddress = 'orders@coles.com.au'
    pocountry = 'Australia'
    ponumber = po_number
    inv_number = re.sub(r'R-', '',  f"INV-{po_number}")
    podate = format_date(po_date)
    duedate = format_date(deldate)
    productid = int(df.iloc[row, 86])
    unitqty = float(df.iloc[row, 12])
    unitprice = float(df.iloc[row, 14])
    acct_code = acct_code_dict.get(productid), ""
    tax_type = "GST on Income"
    currency = 'AUD'

    itemtuple = (contactname, '', '', '', '', '', '', '', '', '', inv_number, ponumber, podate, duedate, productid,
     '', unitqty, unitprice, '', acct_code, tax_type, '', '', '', '', '', '')    

    item_list.append(itemtuple)

    print(itemtuple)
    print(item_list)

# column_names = [
# "*ContactName", "EmailAddress", "POAddressLine1", "POAddressLine2", "POAddressLine3",
# "POAddressLine4", "POCity", "PORegion", "POPostalCode", "POCountry", "*InvoiceNumber", "Reference", "*InvoiceDate",
# "*DueDate", "InventoryItemCode", "*Description", "*Quantity", "*UnitAmount", "Discount", "*AccountCode",
# "*TaxType", "TrackingName1", "TrackingOption1", "TrackingName2", "TrackingOption2", "Currency", "BrandingTheme"
# ]

# def main():
#     csv_lines = []
#     header = ""
#     for name in column_names:
#         header += f"{name},"

#     header = header.strip(',')
#     csv_lines.append(header)

#     for j in range(len(item_list)):
#         csv_line = ""
#         csv_line += f"{item_list[j]},"
#         csv_line = csv_line.strip('(,)').replace("'", '')
#         csv_lines.append(csv_line)

#     output_file = f"/Users/d3ops/Documents/{contactname}-{po_number}.csv"
#     with open(output_file, "w", encoding="utf-8") as f:
#         for line in csv_lines:
#             f.write(line + "\n")

#     print(f"SUCCESS! CSV file has been successfully saved to: {output_file}")

#     viewroot = tk.Tk()
#     viewroot.withdraw()  # Hide the main window
#     tk.messagebox.showinfo("Success", f"CSV file has been successfully created: {output_file}")
#     viewroot.destroy()
# # %%
# # import csv
# # from tkinter.filedialog import askopenfilename

# # with open(askopenfilename(), newline='', encoding='utf-8') as csvfile:
# #     reader = csv.reader(csvfile)
# #     column_names = next(reader)
# #     column_names = [name.strip() for name in column_names]
# #     for row in reader:
# #         print(row)
