# %%
import csv
import re
import tkinter as tk
import datetime
from tkinter.filedialog import askopenfilename

raw_csv = askopenfilename()
with open(raw_csv, 'r', encoding= 'UTF-8') as file:
    reader = csv.reader(file)
    col_names = next(reader)
    headers = next(reader)
    line_deets = []
    for line in reader:
        line_deets.append(line)

acct_code_dict = {
    9421903673244: {'acct': 227010725, 'desc': 'd3 RST - Rigid Strapping Tape'},
    9421903673220: {'acct': 225110726, 'desc': 'd3 K6.0 Kinesiology Tape'},
    9421905741828: {'acct': 225510725, 'desc': 'd3 X6.0 Waterproof Kinesiology Tape'},
    9421903673206: {'acct': 223010725, 'desc': 'd3 Cohesive Bandage'},
    9421034850477: {'acct': 224110725, 'desc': 'd3 Light EAB Spandex Bandage'},
    9421905131841: {'acct': 221010725, 'desc': 'd3 Athletic Tape'},
    9421034854208: {'acct': 284110725, 'desc': 'd3 Instant ice Pack x4'}
    }

# %%
item_list = []

for line in line_deets:
    contactname = 'Coles - Grocery Holdings Pty Limited'
    emailaddress = 'orders@coles.com.au'
    pocountry = 'Australia'
    ponumber = headers[0]
    inv_number = re.sub('R-', '', f'INV-{headers[0]}')[:-1]
    podate = headers[2]
    duedate = headers[5]
    productid = int(line[85])
    productdesc = acct_code_dict.get(productid, "")["desc"]
    orderqty = line[12]
    netprice = float(line[14])
    acct_code = acct_code_dict.get(productid, "")["acct"]
    tax_type = "GST on Income"
    currency = 'AUD'

    dueonterms = podate + datetime.timedelta(days=14)
    print(dueonterms)

    item_tuple = (contactname, emailaddress, '', '', '', '', '', '', '', pocountry,
      inv_number, ponumber, podate, duedate, productid, productdesc, orderqty,
       netprice, '', acct_code, tax_type, '', '', '', '', currency, '')

    item_list.append(item_tuple)

column_names = [
    "*ContactName", "EmailAddress", "POAddressLine1", "POAddressLine2", "POAddressLine3",
    "POAddressLine4", "POCity", "PORegion", "POPostalCode", "POCountry", "*InvoiceNumber", "Reference", "*InvoiceDate",
    "*DueDate", "InventoryItemCode", "*Description", "*Quantity", "*UnitAmount", "Discount", "*AccountCode",
    "*TaxType", "TrackingName1", "TrackingOption1", "TrackingName2", "TrackingOption2", "Currency", "BrandingTheme"
]

# %%
def main():
    csv_lines = []
    header = ""
    for name in column_names:
        header += f"{name},"

    header = header.strip(',')
    csv_lines.append(header)

    for j in range(len(item_list)):
        csv_line = ""
        csv_line += f"{item_list[j]},"
        csv_line = csv_line.strip('(,)').replace("'", '')
        csv_lines.append(csv_line)

    output_file = f"/Users/d3ops/Documents/{contactname}-{ponumber}.csv"
    with open(output_file, "w", encoding="utf-8") as f:
        for ealine in csv_lines:
            f.write(ealine + "\n")

    print(f"SUCCESS! CSV file has been successfully saved to: {output_file}")

    viewroot = tk.Tk()
    viewroot.withdraw()  # Hide the main window
    tk.messagebox.showinfo("Success", f"CSV file has been successfully created: {output_file}")
    viewroot.destroy()

    return 0

if __name__ == "__main__":
    main()