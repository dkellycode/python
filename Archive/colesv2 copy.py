# %%
import glob
import csv
import re
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

csv_orders = glob.glob('/Users/d3ops/Downloads/Purchase_OrderR*.csv')
if len(csv_orders) == 0:
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showwarning("No Orders Found", "No order files were found in the specified directory.")
    root.destroy()
    exit()
for order in csv_orders:
    print("order processed: " + order)

acct_code_dict = {
    9421903673244: {'acct': 227010726, 'desc': 'd3 RST - Rigid Strapping Tape'},
    9421903673220: {'acct': 225110725, 'desc': 'd3 K6.0 Kinesiology Tape'},
    9421905741828: {'acct': 225510725, 'desc': 'd3 X6.0 Waterproof Kinesiology Tape'},
    9421903673206: {'acct': 223010725, 'desc': 'd3 Cohesive Bandage'},
    9421034850477: {'acct': 224110725, 'desc': 'd3 Light EAB Spandex Bandage'},
    9421905131841: {'acct': 221010725, 'desc': 'd3 Athletic Tape'},
    9421034854208: {'acct': 284110725, 'desc': 'd3 Instant ice Pack x4'}
    }

def main():
    """
    main function to iterate over all csv orders
    """
    for csvorder in csv_orders:

        with open(csvorder, 'r', encoding= 'UTF-8') as file:
            reader = csv.reader(file)
            next(reader)
            headers = next(reader)
            line_deets = []
            for line in reader:
                line_deets.append(line)

        item_list = []

        for line in line_deets:
            contactname = 'Coles - Grocery Holdings Pty Limited'
            emailaddress = 'orders@coles.com.au'
            pocountry = 'Australia'
            ponumber = re.sub('R-','PO ', headers[0])
            inv_number = re.sub('R-', '', f'INV-{headers[0]}')[:-1]
            # podate = datetime.strptime(headers[2], '%m/%d/%Y').strftime('%d/%m/%Y')
            duedate = headers[5]
            productid = int(line[85])
            productdesc = acct_code_dict.get(productid, "")["desc"]
            orderqty = line[12]
            netprice = round((float(line[14])/1.1),2)
            acct_code = acct_code_dict.get(productid, "")["acct"]
            tax_type = "GST on Income"
            currency = 'AUD'

            deldate = datetime.strptime(headers[5], '%m/%d/%Y').strftime('%d/%m/%Y')
            dueonterms = (datetime.strptime(duedate, '%m/%d/%Y')+ timedelta(days=14)).strftime('%d/%m/%Y')

            item_tuple = (contactname, emailaddress, '', '', '', '', '', '', '', pocountry,
            inv_number, ponumber, deldate, dueonterms, productid, productdesc, orderqty,
            netprice, '', acct_code, tax_type, '', '', '', '', currency, '')

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

        for j in range(len(item_list)):
            csv_line = ""
            csv_line += f"{item_list[j]},"
            csv_line = csv_line.strip('(,)').replace("'", '')
            csv_lines.append(csv_line)

        output_file = f"/Users/d3ops/Documents/{contactname}-{ponumber}.csv"
        with open(output_file, "w", encoding="utf-8") as f:
            for ealine in csv_lines:
                f.write(ealine + "\n")

        viewroot = tk.Tk()
        viewroot.withdraw()  # Hide the main window
        messagebox.showinfo("Success", f"CSV file has been successfully created: {output_file}")
        viewroot.destroy()

    return 0

if __name__ == "__main__":
    main()