import glob
import csv
import re
from datetime import datetime, timedelta
from container_tools import msgbox
from dictionaries import coles_acct_code_dict

csv_orders = glob.glob('/Users/d3ops/Downloads/Purchase_OrderR*.csv')
if len(csv_orders) == 0:
    msgbox("No Orders Found", "No order files were found in the specified directory.")
    exit()

for order in csv_orders:
    print("order processed: " + order)


column_names = [
"*ContactName", "EmailAddress", "POAddressLine1", "POAddressLine2", "POAddressLine3",
"POAddressLine4", "POCity", "PORegion", "POPostalCode", "POCountry", "*InvoiceNumber", "Reference", "*InvoiceDate",
"*DueDate", "InventoryItemCode", "*Description", "*Quantity", "*UnitAmount", "Discount", "*AccountCode",
"*TaxType", "TrackingName1", "TrackingOption1", "TrackingName2", "TrackingOption2", "Currency", "BrandingTheme"
]

def main():
    """
    main function to iterate over all csv orders
    """
    all_csv_lines = []
    first_order = True
    
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
            duedate = headers[5]
            productid = int(line[85])
            productdesc = coles_acct_code_dict.get(productid, "")["desc"]
            orderqty = line[12]
            netprice = round((float(line[14])/1.1),2)
            acct_code = coles_acct_code_dict.get(productid, "")["acct"]
            tax_type = "GST on Income"
            currency = 'AUD'

            deldate = datetime.strptime(headers[5], '%m/%d/%Y').strftime('%d/%m/%Y')
            dueonterms = (datetime.strptime(duedate, '%m/%d/%Y')+ timedelta(days=14)).strftime('%d/%m/%Y')

            item_tuple = (contactname, emailaddress, '', '', '', '', '', '', '', pocountry,
            inv_number, ponumber, deldate, dueonterms, productid, productdesc, orderqty,
            netprice, '', acct_code, tax_type, '', '', '', '', currency, '')

            item_list.append(item_tuple)
       
        csv_lines = []
        header = ""
        for name in column_names:
            header += f"{name},"
        header = header.strip(',')
        csv_lines.append(header)

        for item in item_list:
            csv_line = ",".join(str(iterable) for iterable in item)
            csv_lines.append(csv_line)

        if first_order:
            all_csv_lines = csv_lines
            first_order = False
        else:
            all_csv_lines.extend(csv_lines[1:])

    output_file = "/Users/d3ops/Documents/combined_coles_import.csv"
    with open(output_file, "w", encoding="utf-8") as f:
        for ealine in all_csv_lines:
            f.write(ealine + "\n")

    msgbox("Success", f"CSV file has been successfully created: {output_file}")

    return 0

if __name__ == "__main__":
    main()