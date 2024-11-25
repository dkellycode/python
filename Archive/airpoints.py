# %%
import csv
import tkinter as tk
import datetime as dt
from tkinter.filedialog import askopenfilename
from datetime import datetime

raw_csv = askopenfilename()
with open(raw_csv, 'r', encoding= 'UTF-8') as file:
    reader = csv.reader(file)
    col_names = next(reader)
    line_deets = []
    for line in reader:
        line_deets.append(line)

print(line_deets)

#remove this dictionary if Aiproints update their account codes; also edit line 48
acct_code_dict = {
    'D3PTMDBK': 24570,
    'D3PTMDSV': 24570
    }

# %%
item_list = []

for line in line_deets:
    contactname = 'Air New Zealand'
    title = line[1]
    firstname = line[2]
    lastname = line[3]
    companyname = line[4]
    street = line[5]
    suburb = line[6]
    city = line[7]
    state = line[8]
    country = line[9]
    postcode = line[10]
    phone = line[12]
    email = line[13]
    ponumber = line[11]
    inv_number = f'INV-{line[11]}'
    podate = datetime.strptime(line[14], '%d/%m/%Y %H:%M').date()
    productid = str(line[19])
    productdesc = line[23]
    orderqty = line[25]
    netprice = float(line[27])
    acct_code = acct_code_dict.get(productid, "")
    tax_type = "GST on Income"
    currency = 'NZD'

    dueonterms = podate + dt.timedelta(days=14)

    item_tuple = [contactname, email, street, '', '', '', city, '', postcode, country,
      inv_number, ponumber, podate.strftime('%d/%m/%Y'), dueonterms.strftime('%d/%m/%Y'), productid, productdesc, orderqty,
       netprice, '', acct_code, tax_type, '', '', '', '', currency, '']

    item_list.append(item_tuple)

column_names = [
    "*ContactName", "EmailAddress", "POAddressLine1", "POAddressLine2", "POAddressLine3",
    "POAddressLine4", "POCity", "PORegion", "POPostalCode", "POCountry", "*InvoiceNumber", "Reference", "*InvoiceDate",
    "*DueDate", "InventoryItemCode", "*Description", "*Quantity", "*UnitAmount", "Discount", "*AccountCode",
    "*TaxType", "TrackingName1", "TrackingOption1", "TrackingName2", "TrackingOption2", "Currency", "BrandingTheme"
]

csv_lines = []
header = ""
for name in column_names:
    header += f"{name},"

header = header.strip(',')
csv_lines.append(header)

for item in item_list:
    csv_line = ",".join(str(iterable) for iterable in item)
    csv_lines.append(csv_line)

output_file = f"/Users/d3ops/Documents/{contactname}-{ponumber}.csv"
with open(output_file, "w", encoding="utf-8") as f:
    for ealine in csv_lines:
        f.write(ealine + "\n")

viewroot = tk.Tk()
viewroot.withdraw()  # Hide the main window
tk.messagebox.showinfo("Success", f"CSV file has been successfully created: {output_file}")
viewroot.destroy()