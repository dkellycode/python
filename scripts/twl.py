"""Tool for parsing TWL order CSV and creating packing summary for distribution"""
import csv
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
from dictionaries import twl_ctn_qtys, twl_store_names

root = tk.Tk()
# root.attributes('-topmost', True)
# root.lift()
# root.focus_force()
root.withdraw()


raw_csv = askopenfilename()
with open(raw_csv, 'r', encoding= 'UTF-8') as file:
    reader = csv.reader(file)
    header_values = next(reader)
    line_deets = []
    for line in reader:
        line_deets.append(line)

def packlist():
    packlist = []
    for line in line_deets:
        store_number = int(line[1])
        store_name = twl_store_names.get(store_number, 'Unknown')
        gtin = int(line[3])
        units = int(line[9])
        qty = units/twl_ctn_qtys.get(gtin, 9999)
        packlist.append([f'{store_number} - {store_name}', qty]) #GTIN removed to preserve functionality

    packtable = pd.DataFrame(packlist, columns=['Store Number', 'Qty']).groupby(['Store Number']).sum()

    print(packtable)

def asn():
    packlist = []
    for line in line_deets:
        store_number = int(line[1])
        store_name = twl_store_names.get(store_number, 'Unknown')
        gtin = int(line[2])
        units = int(line[8])
        qty = units/twl_ctn_qtys.get(gtin, 9999)
        packlist.append([f'{store_number} - {store_name}', qty]) #GTIN removed to preserve functionality

    packtable = pd.DataFrame(packlist, columns=['Store Number', 'Qty']).groupby(['Store Number']).sum()

    print(packtable)

def main():
    if "asn" in raw_csv.lower():
        asn()
    else:
        packlist()

if __name__ == "__main__":
    main()
