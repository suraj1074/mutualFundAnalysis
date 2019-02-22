from loadData import *
import csv


def get_instrument_wise_exposure_month_by_month(months_name):
    security_wise_exposure_monthly = {}
    for month in months_name:
        security_wise_exposure_monthly[month] = calculate_instrument_wise_exposure_by_month(month)
    write_exposure_data_to_csv(security_wise_exposure_monthly)


def calculate_instrument_wise_exposure_by_month(month_name):
    security_wise_exposure = {}
    for instrument in instruments[1:]:
        fund_wise_exposure = get_exposure_to_instrument_by_month(data[month_name], instrument[1])
        fund_wise_contribution = get_contribution_till_month(sip_data, month_name)
        security_wise_exposure[instrument[1]] = 0
        for fund in fund_wise_exposure:
            security_wise_exposure[instrument[1]] += (get_float_from_percentage_string(fund_wise_exposure[fund]) *
                                                      fund_wise_contribution[fund])
    return security_wise_exposure


def get_exposure_to_instrument_by_month(funds_data, ISIN):
    fund_wise_exposure = {}
    for fund in funds_data:
        fund_data = funds_data[fund]
        fund_wise_exposure[fund] = 0
        keys = fund_data[0]
        isin_column_number = keys.index("ISIN")
        exposure_column_number = keys.index("% to net asset")
        for row in fund_data[1:]:
            if row[isin_column_number] == ISIN:
                fund_wise_exposure[fund] = row[exposure_column_number]
    return fund_wise_exposure


def get_contribution_till_month(sip_data, month_name):
    keys = sip_data[0][1:]
    total_contribution = {}
    for k in range(len(keys)):
        key = keys[k]
        total_contribution[key] = 0
        for i in range(len(sip_data)-1, -1, -1):
            total_contribution[key] += float(sip_data[i][k+1])
            if sip_data[i][0] == month_name:
                break
    return total_contribution


def get_float_from_percentage_string(percentage_string):
    value = 0
    try:
        value = float(percentage_string.strip('%')) / 100
    except AttributeError:
        if percentage_string != 0:
            print(percentage_string)
    return value


def write_exposure_data_to_csv(security_wise_exposure):
    nice_table = transform_to_nice_table(security_wise_exposure)
    with open('security_wise_exposure.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        for row in nice_table:
            writer.writerow([s for s in row or []])
    csvFile.close()


def transform_to_nice_table(security_wise_exposure):
    month_names = security_wise_exposure.keys()
    header_row = list(["ISIN", "Instrument Name"]).append(month_names)
    security_wise_exposure_transformed = list()
    security_wise_exposure_transformed.append(header_row)
    instrument_isins = {}
    for instrument in instruments[1:]:
        instrument_isins[instrument[1]] = instrument[0]
    for instrument_isin in instrument_isins:
        row = [instrument_isin, instrument_isins[instrument_isin]]
        for month_name in month_names:
            row.append(security_wise_exposure[month_name][instrument_isin])
        security_wise_exposure_transformed.append(row)
    return security_wise_exposure_transformed


get_instrument_wise_exposure_month_by_month(MONTH_TO_CONSIDER)
# print calculate_instrument_wise_exposure_by_month('Jan 19')

