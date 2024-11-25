# %%

import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename

xml_file = askopenfilename()

tree = ET.parse(xml_file)
root = tree.getroot()

#gather all the key data
contact_name = "Woolworths Limited"
po_number = root.find('.//BuyerPONumber')
inv_number = f"INV-{po_number.text}"
podate = root.find('.//CreationDate/DateTime/Day').text + "/" + root.find('.//CreationDate/DateTime/Month').text + "/" + root.find('.//CreationDate/DateTime/Year').text
deldate = root.find('.//DueDate/DateTime/Day').text + "/" + root.find('.//DueDate/DateTime/Month').text + "/" + root.find('.//DueDate/DateTime/Year').text
duedate = deldate
currency = root.find('.//CurrencyISO')
shipaddress = root.find('.//HEADER/NAD/NADST')

item_details = root.find.all('.//DETAIL/LINGRP')
items_lines = [{
    item_no = root.find.all('.//DETAIL/LINGRP/PIA/IN')
    item_desc = root.find.all('.//DETAIL/LINGRP/IMD')
    item_qty = root.find.all('.//DETAIL/LINGRP/QTY/TOTALORDEREDQUANTITY')
    item_price = root.find.all('.//DETAIL/LINGRP/PRI/UNITCOSTEXCLUSIVEGST')
    tax_type = "GST on Income"
    if currency.text == "AUD":
        acct_code = "225110723"
    elif currency.text == "NZD":
        acct_code = "225110713"
    else:
        acct_code = "Acct code error"
} for line in items_lines]

column_names = [
    "*ContactName", "EmailAddress", "POAddressLine1", "POAddressLine2", "POAddressLine3",
    "POAddressLine4", "POCity", "PORegion", "POPostalCode", "POCountry", "*InvoiceNumber", "Reference", "*InvoiceDate",
    "*DueDate", "InventoryItemCode", "*Description", "*Quantity", "*UnitAmount", "Discount", "*AccountCode",
    "*TaxType", "TrackingName1", "TrackingOption1", "TrackingName2", "TrackingOption2", "Currency", "BrandingTheme"
]

# %%

#create dictionary of key columns
def main():
    csv_writing_dict = {
        0: contact_name,
        10: inv_number,
        11: po_number.text,
        12: deldate,
        13: duedate,
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

    output_file = f"/Users/d3ops/Documents/"+{contact_name}+"-{po_number.text}.csv"
    with open(output_file, "w", encoding="utf-8") as f:
        for line in csv_lines:
            f.write(line + "\n")

    return 0

if __name__ == "__main__":
    main()

    # %% redundant data checks

    # all_tags = []
# for elem in root.iter():
#     if elem.tag not in all_tags:
#         all_tags.append(elem.tag)

# print("All node tags found in order:")
# for tag in all_tags:
#     print(tag)