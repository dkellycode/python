import glob
import csv
from datetime import datetime, timedelta
from container_tools import msgbox

raw_csv = glob.glob('/Users/d3ops/Downloads/AirPointsStore_APSN_D3NZ*.csv')
if len(raw_csv) == 0:
    msgbox("No Orders Found", "No order files were found in the specified directory.")
    exit()

for order in raw_csv:
    print("order processed: " + order)

# #remove this dictionary if Airpoints update their account codes; also edit line 48
acct_code_dict = {
    'D3PTMDBK': 24570,
    'D3PTMDSV': 24570
    }

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
    for csvorder in raw_csv:
        with open(csvorder, 'r', encoding='UTF-8') as file:
            reader = csv.reader(file)
            next(reader)
            line_deets = []
            for line in reader:
                line_deets.append(line)

        item_list = []

        for line in line_deets:
            title = line[1]
            firstname = line[2]
            lastname = line[3]
            companyname = line[4]
            street = line[5]
            # suburb = line[6]
            city = line[7]
            # state = line[8]
            country = line[9]
            postcode = line[10]
            # phone = line[12]
            email = line[13]
            ponumber = line[11]
            inv_number = f'INV-{line[11]}'
            podate = datetime.strptime(line[14], '%Y-%m-%d %H:%M:%S')
            productid = str(line[19])
            productdesc = line[23]
            orderqty = line[25]
            netprice = float(line[27])
            acct_code = acct_code_dict.get(productid, "")
            tax_type = "GST on Income"
            currency = 'NZD'
            contactname = f'{title} {firstname} {lastname}'
            if companyname != "":
                contactname = (f'{contactname} care of {companyname}')

            dueonterms = (podate + timedelta(days=14)).strftime('%d/%m/%Y')

            item_tuple = [contactname, email, street, '', '', '', city, '', postcode, country,
            inv_number, ponumber, podate.strftime('%d/%m/%Y'), dueonterms, productid, productdesc, orderqty,
            netprice, '', acct_code, tax_type, '', '', '', '', currency, '']

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

        output_file = f"/Users/d3ops/Documents/AirPoints_{contactname}-{ponumber}.csv"
        with open(output_file, "w", encoding="utf-8") as f:
            for ealine in csv_lines:
                f.write(ealine + "\n")

        msgbox("Success", f"CSV file has been successfully created: {output_file}")

    return 0

if __name__ == "__main__":
    main()