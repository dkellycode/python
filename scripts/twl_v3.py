"""Tool for parsing mutlipe TWL order CSVs and creating packing summary for distribution"""
import csv
import glob
import pandas as pd
from dictionaries import twl_ctn_qtys, twl_store_names

asns = glob.glob('/Users/d3ops/Downloads/asntocsv*.csv')
pos = glob.glob('/Users/d3ops/Downloads/potocsv*.csv')
raw_csv = asns + pos
import_count = 1
for each in raw_csv:
    print()
    print(f'Order ({import_count}) imported: {each}')
    import_count += 1
# print(raw_csv)

def main():
    for csv_file in raw_csv:
        with open(csv_file, 'r', encoding='UTF-8') as file:
            reader = csv.reader(file)
            header_values = next(reader)
            po_number = header_values[0]
            line_deets = []
            for line in reader:
                line_deets.append(line)


        def packlist():
            packlist = []
            for line in line_deets:
                store_number = int(line[1])
                store_name = twl_store_names.get(store_number, "")['name']
                # store_group = twl_store_names.get(store_number, "")['group']
                store_group = twl_store_names.get(store_number, {}).get('group', '')
                gtin = int(line[3])
                units = int(line[9])
                qty = units/twl_ctn_qtys.get(gtin, 9999)
                packlist.append([f'{store_number} - {store_name}', qty]) #GTIN removed to preserve functionality

            packtable = pd.DataFrame(packlist, columns=['Store Number', 'Qty']).groupby(['Store Number']).sum()
            # packtable = pd.DataFrame(packlist, columns=['Store Number', 'Qty']).groupby(['Store Number'], sort = False).sum()
            packtable.loc['Total Inners:'] = packtable.sum()

            print('\n')
            print(f'PO Number: {po_number}')
            print(packtable)
            print()
            

        def asn():
            polist = []
            for line in line_deets:
                store_number = int(line[1])
                store_name = twl_store_names.get(store_number, "")['name']
                store_group = twl_store_names.get(store_number, "")['group']#why the fuck does this syntax owrk here but nt in the packlist function?
                gtin = int(line[2])
                units = int(line[8])
                qty = units/twl_ctn_qtys.get(gtin, 9999)
                polist.append([f'{store_number} - {store_name}', qty]) #GTIN removed to preserve functionality

            packtable = pd.DataFrame(polist, columns=['Store Number', 'Qty']).groupby(['Store Number']).sum()
            # packtable = pd.DataFrame(polist, columns=['Store Number', 'Qty']).groupby(['Store Number'], sort = False).sum()
            packtable.loc['Total Inners:'] = packtable.sum()

            print('\n')
            print(f'PO Number: {po_number}')
            print(packtable)
            print()

        if "asn" in csv_file:
            asn()
        else:
            packlist()
        

if __name__ == "__main__":
    main()
