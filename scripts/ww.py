# %%

import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter.filedialog import askopenfilename
from datetime import datetime, timedelta
from dictionaries import ww_acct_code_dict, column_names

xml_file = askopenfilename()

tree = ET.parse(xml_file)
root = tree.getroot()

#build the line detail structure
po_number = root.find('.//BuyerPONumber').text
orderitems = root.findall('.//POItem')
item_list = [] # Initialize an empty lists to store all tuples
credit_list = []  

for orderitem in orderitems:
    contactname = "Woolworths Limited"
    emailaddress = "orders@woolworths.com.au"
    pocountry = 'Australia'
    ponumber = po_number
    inv_number = f"INV-{po_number}"
    #podate = root.find('.//CreationDate/DateTime/Day').text + "/" + root.find('.//CreationDate/DateTime/Month').text + "/" + root.find('.//CreationDate/DateTime/Year').text
    duedate = root.find('.//DueDate/DateTime/Day').text + "/" + root.find('.//DueDate/DateTime/Month').text + "/" + root.find('.//DueDate/DateTime/Year').text
    productid = orderitem.find('ProductIdentifierList').find('ProductID').find('PartNumber').text
    productdesc = ww_acct_code_dict.get(int(productid), "")["desc"]
    orderqty = orderitem.find('OrderQuantity').find('Quantity').find('Number').find('Value').text[:-4] #if they ever order >99 this will fuck out
    netprice = (float(orderitem.find('NetPriceIncludingTax').find('MonetaryValue').find('Number').find('Value').text[:-2])/100)/1.1
    acct_code = ww_acct_code_dict.get(int(productid), "")['acct']
    tax_type = "GST on Income"
    currency = root.find('.//CurrencyISO').text
    dueonterms = datetime.strptime(duedate, '%d/%m/%Y') + timedelta(days=14)

    item_tuple = [contactname, emailaddress,'', '', '', '', '', '', '', pocountry,
      inv_number, ponumber, duedate, dueonterms.strftime('%d/%m/%Y'), productid, productdesc, orderqty,
       round(netprice,2), '', acct_code, tax_type, '', '', '', '', currency, '']
       
    item_list.append(item_tuple)

    credit_tuple = [contactname, emailaddress, '', '', '', '', '', '', '', pocountry,
        inv_number.replace("INV","CN"), ponumber, duedate, dueonterms.strftime('%d/%m/%Y'), productid, productdesc, orderqty,
        round((netprice*-.2075),2), '', acct_code, tax_type, '', '', '', '', currency, '']

    credit_list.append(credit_tuple)

adjustment_line = [contactname, emailaddress, '', '', '', '', '', '', '', pocountry,
         inv_number.replace("INV","CN"), f'PO {ponumber}', duedate, dueonterms.strftime('%d/%m/%Y'), '', 'Adjustment to Total', 1, 0.00, '', 41100, 'BAS Excluded', '',
          '', '', '', currency, '']
    

def main():
    csv_lines = []
    header = ",".join(str(iterable) for iterable in column_names)
    csv_lines.append(header)

    for item in item_list:
        csv_line = ",".join(str(iterable) for iterable in item)
        csv_lines.append(csv_line)
    
    inv_adjust = ",".join(str(iterable) for iterable in adjustment_line)
    csv_lines.append(inv_adjust)

    for credit in credit_list:
        csv_line = ",".join(str(iterable) for iterable in credit)
        csv_lines.append(csv_line)

    footer = ",".join(str(iterable) for iterable in adjustment_line)
    csv_lines.append(footer)

    output_file = f"/Users/d3ops/Documents/{contactname}-{po_number}.csv"
    with open(output_file, "w", encoding="utf-8") as f:
        for line in csv_lines:
            f.write(line + "\n")

    # print(f"SUCCESS! CSV file has been successfully saved to: {output_file}")

    viewroot = tk.Tk()
    viewroot.withdraw()  # Hide the main window
    tk.messagebox.showinfo("Success", f"CSV file has been successfully created: {output_file}")
    viewroot.destroy()

    return 0

if __name__ == "__main__":
    main()
