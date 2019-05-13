import datetime
import os
import pandas as pd


def build_stock_data(folder_path):
    # read in all .csv files from directory folder_path
    file_list = [file_path for file_path in os.listdir(folder_path)]
    files = []
    data_frame = pd.DataFrame()
    # initialize pandas dataframe with CSV
    print("\t==================================================\n"
          "Creating primary Data Frame. This may take several minutes...\n"
          "\t==================================================")
    for f in file_list:
        # Gets a stock ticker name from the file name
        nice_name = (os.path.split(f)[1]).split('.')[0].upper()
        f = os.path.join(folder_path, f)
        # Due to dirty data, there are some files with no or little data. This discards them
        if os.path.getsize(f) > 50000:
            files.append(f)
            print("Found stock %s" % nice_name)
            next_frame = pd.read_csv(f)
            del next_frame['OpenInt']  # Useless column, is always zero
            next_frame['ticker'] = nice_name
            data_frame = pd.concat([data_frame, next_frame], ignore_index=True)
        else:
            print("Discarding %s (too small)" % nice_name)

    return data_frame


def store_data_frame(data_frame):
    data_frame.to_csv("compiled_data_%s.csv" % datetime.date.today(), compression='zip')


stock_data = build_stock_data("Stock_Data\\Stocks")
store_data_frame(stock_data)
