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
tax_type = "GST on Income"

#build the line detail structure
orderitems = root.findall('.//POItem')
item_list = []  # Initialize an empty list to store all tuples

for orderitem in orderitems:
    contactname = contact_name
    emailaddress = "orders@woolworths.com.au"
    poaddressline1 = None
    poaddressline2 = None
    poaddressline3 = None
    poaddressline4 = None
    pocity = None
    poregion = None
    popostalcode = None
    pocountry = 'Australia'
    invoicenumber = inv_number
    reference = po_number.text
    invoicedate = podate
    datedue = duedate
    productid = orderitem.find('ProductIdentifierList').find('ProductID').find('PartNumber').text
    productdesc = orderitem.find('ItemName').text
    orderqty = orderitem.find('OrderQuantity').find('Quantity').find('Number').find('Value').text[:-4]
    netprice = float(orderitem.find('NetPriceIncludingTax').find('MonetaryValue').find('Number').find('Value').text[:-2])/100
    discount = None
    acct_code = acct_code_dict.get(int(productid), "")
    tax_type = "GST on Income"
    trackingname1 = None
    trackingoption1 = None
    trackingname2 = None
    trackingoption2 = None
    currency = 'AUD'
    brandingtheme = None
    
    item_tuple = (contactname, emailaddress, poaddressline1, poaddressline2, poaddressline3, poaddressline4, pocity, poregion, popostalcode, pocountry, invoicenumber, reference, invoicedate, datedue, productid, productdesc, orderqty, netprice, discount, acct_code, tax_type, trackingname1, trackingoption1, trackingname2, trackingoption2, currency, brandingtheme)
    item_list.append(item_tuple)

column_names = [
    "*ContactName", "EmailAddress", "POAddressLine1", "POAddressLine2", "POAddressLine3",
    "POAddressLine4", "POCity", "PORegion", "POPostalCode", "POCountry", "*InvoiceNumber", "Reference", "*InvoiceDate",
    "*DueDate", "InventoryItemCode", "*Description", "*Quantity", "*UnitAmount", "Discount", "*AccountCode",
    "*TaxType", "TrackingName1", "TrackingOption1", "TrackingName2", "TrackingOption2", "Currency", "BrandingTheme"
]

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
        csv_line = csv_line.strip('(,)')
        csv_lines.append(csv_line)

    print(csv_lines)

    output_file = f"/Users/d3ops/Documents/{contactname}-{po_number.text}.csv"
    with open(output_file, "w", encoding="utf-8") as f:
        for line in csv_lines:
            f.write(line + "\n")

    print(f"CSV file has been successfully created: {output_file}")

    viewroot = tk.Tk()
    viewroot.withdraw()  # Hide the main window
    tk.messagebox.showinfo("Success", f"CSV file has been successfully created: {output_file}")
    viewroot.destroy()

    return 0

if __name__ == "__main__":
    main()