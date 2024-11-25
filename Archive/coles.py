import tkinter as tk
import pandas as pd
import numpy as np
from tkinter.filedialog import askopenfilename

def cost_table_build():
	global cost_table 
	cost_table = pd.DataFrame({
	'prodname':['rigid','kines','wtrprf','cohesive','eab','ast','bfees'],
	'prodcost':[280.80,233.28,332.10,149.76,999.99,999.99,0.00],
	'proddesc':['d3 RST - Rigid Strapping Tape','d3 K6.0 Kinesiology Tape','d3 X6.0 Waterproof Kinesiology Tape','d3 Cohesive Bandage','d3 Light EAB Spandex Bandage','d3 Athletic Tape','Adjustment to Total'],
	'prodaccts':[227010726,225110725,225510726,223010726,000000000,000000000,41100],
	'shippercodes':[9421903673244,9421903673220,9421905741828,9421903673206,9421034850477,9421905131841,99999],
	'taxtype':['GST on Income','GST on Income','GST on Income','GST on Income','GST on Income','GST on Income','BAS Excluded']
	})


def get_po_file():
	global rawdf
	rawdf = pd.read_csv(askopenfilename())
	pd.set_option('display.max_columns',(rawdf.shape[1]))

def data_extract():
	duedate = rawdf.iat[1,6]
	#colnames = (rawdf.columns.tolist)
	print(duedate)

cost_table_build()
get_po_file()
data_extract()









#def cost_table_show():
#	print(cost_table)

#cost_table_show()

#print(duedate)

#xero_import = rawdf[[]]
