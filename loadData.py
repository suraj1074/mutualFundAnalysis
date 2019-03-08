import csv
from hepler import *

LIST_OF_FUNDS_FILE = ["ABSLTR96", "MOLTE", "FranklinPrima", "HdfcMidcap", "IciciHybrid","MiraeAsset","SbiSmallCap","ParagParikh"]
# LIST_OF_FUNDS_FILE = ["ABSLTR96"]
MONTH_TO_CONSIDER = ["dec18", "jan19"]
# MONTH_TO_CONSIDER = ["dec18"]
INSTRUMENT_FILE = "master_instruments.csv"
SIP_DETAILS_FILE = "SIPDetails.csv"
DATA_DIR = "data/"


def load_data_by_file(file_name):
    rows = []
    #print(file_name)
    f = open(file_name, mode='r', encoding='utf-8-sig')
    csv_reader = csv.reader(f)
    for row in csv_reader:
        row = [cell for cell in row]
        rows.append(row)
    return rows


def load_instruments():
    instruments_data = load_data_by_file(INSTRUMENT_FILE)
    result = {}
    for instrument in instruments_data:
        if instrument[1] not in result:
            result[instrument[0]] = instrument
    return result


def load_sip_details():
    return load_data_by_file(SIP_DETAILS_FILE)


def load_funds_file():
    mf_data = {}
    for s in LIST_OF_FUNDS_FILE:
        mf_data[s] = load_data_by_file(s + ".csv")
    return mf_data


def populate_portfolio_instruments(month_data, month_name):
    month_portfolio = {}
    for fund_data in month_data:
        for instrument_data in month_data[fund_data]:
            if check_isin(instrument_data[0]):
                if instrument_data[0] in month_portfolio:
                    continue
                elif instrument_data[0] not in instruments:
                    print("Instrument " + instrument_data[0] + " is absent. Fund: " + fund_data + " in month " + month_name)
                    month_portfolio[instrument_data[0]] = [instrument_data[0], "Empty", "Empty"]
                else:
                    month_portfolio[instrument_data[0]] = instruments[instrument_data[0]]
            else:
                print("Not a valid instrument: " + instrument_data[0])
    portfolio_instruments[month_name] = month_portfolio

def load_data():
    data = {}
    for month_name in MONTH_TO_CONSIDER:
        month_data = {}
        month_dir_name = DATA_DIR + month_name
        for fund_name in LIST_OF_FUNDS_FILE:
            fund_file_name = month_dir_name + '/' + fund_name + ".csv"
            fund_data = load_data_by_file(fund_file_name)
            month_data[fund_name] = fund_data
        populate_portfolio_instruments(month_data, month_name)
        data[month_name] = month_data
    return data


portfolio_instruments = {}
instruments = load_instruments()
sip_data = load_sip_details()
# mutual_funds_data = load_funds_file()
data = load_data()
print("loadData Finished")