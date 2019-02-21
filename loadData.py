import csv

LIST_OF_FUNDS_FILE = ["ABSLTR96", "MOLTE"]
INSTRUMENT_FILE = "Instruments.csv"
SIP_DETAILS_FILE = "SIPDetails.csv"


def load_data_by_file(file_name):
    rows = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            row = [unicode(cell, 'utf-8-sig') for cell in row]
            rows.append(row)
    return rows


def load_instruments():
    return load_data_by_file(INSTRUMENT_FILE)


def load_sip_details():
    return load_data_by_file(SIP_DETAILS_FILE)


def load_funds_file():
    mf_data = {}
    for s in LIST_OF_FUNDS_FILE:
        mf_data[s] = load_data_by_file(s+".csv")
    return mf_data


instruments = load_instruments()
sip_data = load_sip_details()
mutual_funds_data = load_funds_file()
