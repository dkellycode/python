# %%

import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter.filedialog import askopenfilename

xml_file = askopenfilename()

tree = ET.parse(xml_file)
root = tree.getroot()

acct_code_dict = {
    9421903673244: 227010725,
    9421903673220: 225110726,
    9421905741828: 225510725,
    9421903673206: 223010725,
    9421034850477: 224110725,
    9421905131841: 221010725,
    9421034854208: 284110725
    }

#gather all the key data
contact_name = "Woolworths Limited"
po_number = root.find('.//BuyerPONumber')
inv_number = f"INV-{po_number.text}"
podate = root.find('.//CreationDate/DateTime/Day').text + "/" + root.find('.//CreationDate/DateTime/Month').text + "/" + root.find('.//CreationDate/DateTime/Year').text
deldate = root.find('.//DueDate/DateTime/Day').text + "/" + root.find('.//DueDate/DateTime/Month').text + "/" + root.find('.//DueDate/DateTime/Year').text
duedate = deldate
currency = root.find('.//CurrencyISO')
shipaddress = root.find('.//HEADER/NAD/NADST')
tax_type = "GST on Income"

orderitems = root.findall('.//POItem')
itemlines = []
for orderitem in orderitems:
    productid = orderitem.find('ProductIdentifierList').find('ProductID').find('PartNumber').text
    productdesc = orderitem.find('ItemName').text
    orderqty = orderitem.find('OrderQuantity').find('Quantity').find('Number').find('Value').text[:-4]
    netprice = float(orderitem.find('NetPriceIncludingTax').find('MonetaryValue').find('Number').find('Value').text[:-2])/100
    acct_code = ()
    if productid in acct_code_dict:
        acct_code = acct_code_dict.get(productid,"")

    item_tuple = (productid, productdesc, orderqty, netprice, acct_code)
    item_list.append(item_tuple)

column_names = [
    "*ContactName", "EmailAddress", "POAddressLine1", "POAddressLine2", "POAddressLine3",
    "POAddressLine4", "POCity", "PORegion", "POPostalCode", "POCountry", "*InvoiceNumber", "Reference", "*InvoiceDate",
    "*DueDate", "InventoryItemCode", "*Description", "*Quantity", "*UnitAmount", "Discount", "*AccountCode",
    "*TaxType", "TrackingName1", "TrackingOption1", "TrackingName2", "TrackingOption2", "Currency", "BrandingTheme"
]

def main():
    csv_writing_dict = {
        0: contact_name,
        10: inv_number,
        11: po_number.text,
        12: deldate[0],
        13: duedate[0],
        15: productdesc,
        16: orderqty,
        17: netprice,
        19: acct_code,
        20: tax_type
    }

    csv_lines = []
    header = ""
    for name in column_names: 
        header += f"{name},"

    header = header.strip(',')

    csv_lines.append(header)

    csv_line = ""

    for j in range(len(column_names)):
        value = csv_writing_dict.get(j, "")
        csv_line += f"{value},"

    csv_line = csv_line.strip(',')

    csv_lines.append(csv_line)

    output_file = f"/Users/d3ops/Documents/{contact_name}-{po_number.text}.csv"
    with open(output_file, "w", encoding="utf-8") as f:
        for line in csv_lines:
            f.write(line + "\n")

    viewroot = tk.Tk()
    viewroot.withdraw()  # Hide the main window
    tk.messagebox.showinfo("Success", f"CSV file has been successfully created: {output_file}")
    viewroot.destroy()


    return 0

if __name__ == "__main__":
    main()
