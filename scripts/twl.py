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

def main():

    def packlist_build():
        polist = []
        for line in line_deets:
            store_number = int(line[1])
            store_name = twl_store_names.get(store_number, "")['name']
            store_group = twl_store_names.get(store_number, "")['group']
            gtin = int(line[2]) if "asn" in each.lower() else int(line[3])
            units = int(line[8]) if "asn" in each.lower() else int(line[9])
            qty = units/twl_ctn_qtys.get(gtin, 9999)
            polist.append([store_group, f'{store_number} - {store_name}', qty])

        packtable = pd.DataFrame(polist, columns=['Group', 'Store Number', 'Qty']).groupby(['Group','Store Number']).sum()
        packtable.index = [f"{g} {s}".strip('()') for g, s in packtable.index]
        packtable.loc['Total Inners:'] = packtable.sum()

        # return packtable
        # packtable.to_excel(f'{po_number} Label List.xlsx', sheet_name='Label List')

        print('\n')
        print(f'PO Number: {po_number}')
        print(packtable)
        print()


    for each in raw_csv:
        # global po_number, line_deets
        line_deets = []
        with open(each, 'r', encoding='UTF-8') as file:
            reader = csv.reader(file)
            header_values = next(reader)
            po_number = header_values[0]
            for line in reader:
                line_deets.append(line)
                
        packlist_build()

if __name__ == "__main__":
    main()


    # packtable.index = [f"{g} {s}" for g, s in packtable.index]
