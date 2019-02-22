import csv

LIST_OF_FUNDS_FILE = ["ABSLTR96", "MOLTE", "FranklinPrima"]
INSTRUMENT_FILE = "Instruments.csv"
SIP_DETAILS_FILE = "SIPDetails.csv"
DATA_DIR = "data/"
MONTH_TO_CONSIDER = ["dec18", "jan19"]


def load_data_by_file(file_name):
    rows = []
    f = open(file_name, mode='r', encoding='utf-8-sig')
    csv_reader = csv.reader(f)
    for row in csv_reader:
        row = [cell for cell in row]
        rows.append(row)
    return rows


def load_instruments():
    return load_data_by_file(INSTRUMENT_FILE)


def load_sip_details():
    return load_data_by_file(SIP_DETAILS_FILE)


def load_funds_file():
    mf_data = {}
    for s in LIST_OF_FUNDS_FILE:
        mf_data[s] = load_data_by_file(s + ".csv")
    return mf_data


def load_data():
    data = {}
    for month_name in MONTH_TO_CONSIDER:
        month_data = {}
        month_dir_name = DATA_DIR + month_name
        for fund_name in LIST_OF_FUNDS_FILE:
            fund_file_name = month_dir_name + '/' + fund_name + ".csv"
            fund_data = load_data_by_file(fund_file_name)
            month_data[fund_name] = fund_data
        data[month_name] = month_data
    return data


instruments = load_instruments()
sip_data = load_sip_details()
#mutual_funds_data = load_funds_file()
data = load_data()
