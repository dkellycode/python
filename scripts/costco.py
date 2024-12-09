
import xml.etree.ElementTree as ET
import tkinter as tk
from datetime import datetime
from tkinter.filedialog import askopenfilename
from dictionaries import column_names
from container_tools import msgbox

xml_file = askopenfilename()

tree = ET.parse(xml_file)
root = tree.getroot()

def format_date(date_string):
    return datetime.strptime(date_string, '%Y%m%d').strftime('%d/%m/%Y')

#gather all the key data
contact_name = root.find('.//FROMBUSS')
po_number = root.find('.//PONUMBER')
inv_number = f"INV-{po_number.text}"
podate = root.find('.//BGM/PODATE')
deldate = root.find('.//DTM/REQUIREDDELIVERYDATE')
duedate = deldate.text
currency = root.find('.//CUX/CURRENCYTYPE')
shipaddress = root.find('.//HEADER/NAD/NADST')
item_no = root.find('.//DETAIL/LINGRP/PIA/IN')
item_desc = root.find('.//DETAIL/LINGRP/IMD')
item_qty = root.find('.//DETAIL/LINGRP/QTY/TOTALORDEREDQUANTITY')
item_price = root.find('.//DETAIL/LINGRP/PRI/UNITCOSTEXCLUSIVEGST')
tax_type = "GST on Income"
if currency.text == "AUD":
    acct_code = "225110723"
elif currency.text == "NZD":
    acct_code = "225110713"
else:
    acct_code = "Acct code error"

# Initialize a list to collect text content
keyaddelements = 8

addresselements = []

# Iterate through the first n elements and collect their text
for i, elem in enumerate(shipaddress.iter()):
    if i < keyaddelements:
        text = elem.text.strip() if elem.text else ''  # Use an empty string if no text is present
        addresselements.append(text)
    else:
        break

full_address = ' '.join(addresselements).lstrip()

#create dictionary of key columns
def main():
    csv_writing_dict = {
        0: contact_name.text,
        10: inv_number,
        11: po_number.text,
        12: format_date(deldate.text),
        13: format_date(duedate),
        15: item_desc.text,
        16: item_qty.text,
        17: item_price.text,
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

    output_file = f"/Users/d3ops/Documents/{contact_name.text}-{po_number.text}.csv"
    with open(output_file, "w", encoding="utf-8") as f:
        for line in csv_lines:
            f.write(line + "\n")

    msgbox("Success", f"CSV file has been successfully created: {output_file}")

    return 0

if __name__ == "__main__":
    main()
