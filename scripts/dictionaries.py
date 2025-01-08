"""FMCG dictionaries to be called as required"""

#TWL

#  TWLcarton quantities per product GTIN
twl_ctn_qtys = {
        9421903673008:8,
        9421903673022:6,
        9421903673039:6,
        9421903673046:6,
        9421904070080:4,
        9421904070233:10,
        9421903673107:10,
        9421903673091:10
        }

#TWL store data for matching PO data and sorting pack lists
twl_store_names = {
    103: {'name': 'Westcity', 'group': 'B'},
    107: {'name': 'New Lynn', 'group': 'B'},
    109: {'name': 'Papakura', 'group': 'B'},
    110: {'name': 'Te Awamutu', 'group': 'B'},
    111: {'name': 'Pukekohe', 'group': 'B'},
    112: {'name': 'Balmoral', 'group': 'B'},
    113: {'name': 'Newmarket', 'group': 'B'},
    114: {'name': 'Pakuranga', 'group': 'A'},
    115: {'name': 'Whangaparoa', 'group': 'B'},
    116: {'name': 'Whangarei', 'group': 'A'},
    117: {'name': 'Kaitaia', 'group': 'B'},
    118: {'name': 'Birkenhead', 'group': 'B'},
    119: {'name': 'Albany', 'group': 'A'},
    120: {'name': 'Northlands', 'group': 'A'},
    122: {'name': 'Rolleston', 'group': 'B'},
    123: {'name': 'Eastgate', 'group': 'A'},
    125: {'name': 'Oamaru', 'group': 'B'},
    126: {'name': 'Nelson', 'group': 'A'},
    127: {'name': 'Timaru', 'group': 'A'},
    128: {'name': 'Hornby', 'group': 'B'},
    129: {'name': 'Dunedin', 'group': 'B'},
    130: {'name': 'Mosgiel', 'group': 'B'},
    131: {'name': 'Petone', 'group': 'B'},
    132: {'name': 'Porirua', 'group': 'B'},
    133: {'name': 'Johnsonville', 'group': 'B'},
    134: {'name': 'Wellington', 'group': 'B'},
    135: {'name': 'Paraparaumu', 'group': 'B'},
    136: {'name': 'Masterton', 'group': 'B'},
    137: {'name': 'Levin', 'group': 'B'},
    138: {'name': 'Upper Hutt', 'group': 'B'},
    139: {'name': 'Lower Hutt', 'group': 'B'},
    140: {'name': 'Hawera', 'group': 'B'},
    141: {'name': 'Hamilton', 'group': 'B'},
    142: {'name': 'Rotorua', 'group': 'A'},
    143: {'name': 'Tauranga', 'group': 'B'},
    144: {'name': 'New Plymouth', 'group': 'B'},
    145: {'name': 'Wanganui', 'group': 'B'},
    146: {'name': 'Palm Nth', 'group': 'A'},
    147: {'name': 'Tokoroa', 'group': 'B'},
    148: {'name': 'Taupo', 'group': 'B'},
    149: {'name': 'Thames', 'group': 'B'},
    151: {'name': 'Hastings', 'group': 'A'},
    152: {'name': 'Napier', 'group': 'A'},
    153: {'name': 'Gisborne', 'group': 'B'},
    154: {'name': 'Matamata', 'group': 'B'},
    155: {'name': 'Whakatane', 'group': 'B'},
    156: {'name': 'Papamoa', 'group': 'B'},
    157: {'name': 'Morrinsville', 'group': 'B'},
    158: {'name': 'Feilding', 'group': 'B'},
    159: {'name': 'Cambridge', 'group': 'B'},
    160: {'name': 'Hillcrest', 'group': 'B'},
    161: {'name': 'Dannevirke', 'group': 'B'},
    162: {'name': 'Wainuiomata', 'group': 'B'},
    163: {'name': 'Fraser Cove', 'group': 'A'},
    164: {'name': 'Bell Block', 'group': 'B'},
    165: {'name': 'Dargaville', 'group': 'B'},
    166: {'name': 'Snells Beach', 'group': 'B'},
    168: {'name': 'Te Kuiti', 'group': 'B'},
    169: {'name': 'Waipapa', 'group': 'B'},
    170: {'name': 'Lyall Bay', 'group': 'A'},
    171: {'name': 'Invercargill', 'group': 'A'},
    172: {'name': 'Gore', 'group': 'B'},
    173: {'name': 'Blenheim', 'group': 'B'},
    174: {'name': 'Greymouth', 'group': 'B'},
    175: {'name': 'Sth City (Chch)', 'group': 'B'},
    176: {'name': 'Ashburton', 'group': 'B'},
    177: {'name': 'Alexandra', 'group': 'B'},
    178: {'name': 'Barrington', 'group': 'B'},
    179: {'name': 'Queenstown', 'group': 'B'},
    180: {'name': 'Rangiora', 'group': 'B'},
    181: {'name': 'Belfast', 'group': 'B'},
    182: {'name': 'Motueka', 'group': 'B'},
    183: {'name': 'Dunedin South', 'group': 'A'},
    184: {'name': 'Balclutha', 'group': 'B'},
    185: {'name': 'Te Rapa', 'group': 'A'},
    186: {'name': 'Sylvia Park', 'group': 'A'},
    187: {'name': 'St Lukes', 'group': 'B'},
    188: {'name': 'Royal Oak', 'group': 'B'},
    189: {'name': 'Whitianga', 'group': 'B'},
    190: {'name': 'Lunn Ave', 'group': 'B'},
    191: {'name': 'Silverdale', 'group': 'A'},
    192: {'name': 'Mt Roskill', 'group': 'B'},
    193: {'name': 'Takanini', 'group': 'B'},
    195: {'name': 'Ormiston', 'group': 'B'},
    196: {'name': 'Warkworth', 'group': 'B'},
    201: {'name': 'Milford', 'group': 'B'},
    202: {'name': 'Botany Downs', 'group': 'B'},
    203: {'name': 'Downtown Ak', 'group': 'B'},
    204: {'name': 'Kaikohe', 'group': 'B'},
    205: {'name': 'Clendon', 'group': 'B'},
    207: {'name': 'Lincoln Road', 'group': 'B'},
    208: {'name': 'Westgate', 'group': 'A'},
    209: {'name': 'Airport', 'group': 'B'},
    210: {'name': 'Glenfield', 'group': 'B'},
    211: {'name': 'Richmond', 'group': 'B'},
    212: {'name': 'Wanaka (SWAS)', 'group': 'B'},
    220: {'name': 'Riccarton', 'group': 'A'},
    221: {'name': 'Atrium', 'group': 'B'},
    222: {'name': 'Turanga Crossing', 'group': 'B'},
    262: {'name': 'NIDC Central Fulfilment Centre', 'group': 'B'},
    405: {'name': 'Manukau', 'group': 'A'},
        }

#WOOLWORTHS

#Xero account codes for Woolworths products
ww_acct_code_dict = {
    9421903673244: {'acct': 227010725, 'desc': 'd3 RST - Rigid Strapping Tape'},
    9421903673220: {'acct': 225110726, 'desc': 'd3 K6.0 Kinesiology Tape'},
    9421905741828: {'acct': 225510725, 'desc': 'd3 X6.0 Waterproof Kinesiology Tape'},
    9421903673206: {'acct': 223010725, 'desc': 'd3 Cohesive Bandage'},
    9421034850477: {'acct': 224110725, 'desc': 'd3 Light EAB Spandex Bandage'},
    9421905131841: {'acct': 221010725, 'desc': 'd3 Athletic Tape'},
    9421034854208: {'acct': 284110725, 'desc': 'd3 Instant Ice Pack 4pk'}
    }

#COLES

#Xero account codes for Coles products
coles_acct_code_dict = {
    9421903673244: {'acct': 227010726, 'desc': 'd3 RST - Rigid Strapping Tape'},
    9421903673220: {'acct': 225110725, 'desc': 'd3 K6.0 Kinesiology Tape'},
    9421905741828: {'acct': 225510726, 'desc': 'd3 X6.0 Waterproof Kinesiology Tape'},
    9421903673206: {'acct': 223010726, 'desc': 'd3 Cohesive Bandage'},
    9421034850477: {'acct': 224110725, 'desc': 'd3 Light EAB Spandex Bandage'},
    9421905131841: {'acct': 221010725, 'desc': 'd3 Athletic Tape'},
    9421034854208: {'acct': 284110725, 'desc': 'd3 Instant ice Pack x4'}
    }

#XERO

#Generic column names list for building Xero import files
column_names = [
    "*ContactName", "EmailAddress", "POAddressLine1", "POAddressLine2", "POAddressLine3",
    "POAddressLine4", "POCity", "PORegion", "POPostalCode", "POCountry", "*InvoiceNumber", "Reference", "*InvoiceDate",
    "*DueDate", "InventoryItemCode", "*Description", "*Quantity", "*UnitAmount", "Discount", "*AccountCode",
    "*TaxType", "TrackingName1", "TrackingOption1", "TrackingName2", "TrackingOption2", "Currency", "BrandingTheme"
]