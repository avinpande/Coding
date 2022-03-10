import logging

from sas7bdat import SAS7BDAT
import sys
import pandas as pd


def write_sas7bdat(source_file_path, target_file_path):
    source_file_path = source_file_path.strip()
    target_file_path = target_file_path.strip()
    pass


def read_sas7bdat(source_file_path):
    try:
        source_file_path = source_file_path.strip()
        with SAS7BDAT(source_file_path) as read_obj:
            df = read_obj.to_data_frame()
            print(df.head(1,truncate=False))
    except:
        print(logging.error('Error'))
    pass


source_path = r'C:\Users\avinpandey\Desktop\sas7bdat\DCSKINPRODUCT.sas7bdat'
read_sas7bdat(source_path)
target_path = r'C:\Users\avinpandey\Desktop\sas7bdat'
write_sas7bdat(source_path,target_path)
