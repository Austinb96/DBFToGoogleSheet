import pandas as pd
from dbfread import DBF
import gspread
from gspread_dataframe import set_with_dataframe
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# File for Importing
filePath = config['DEFAULT']['importFile']
# Sheet Key
key = config['DEFAULT']['key']
# Worksheet you are working on
worksheetName = config['DEFAULT']['worksheetName']
# Columns to keep
columnsToKeep = config['DEFAULT']['columnsToKeep'].split(',')
columnsToKeep = [i.strip('""') for i in columnsToKeep]

sa = gspread.service_account(filename='service_account.json')

# Take dbf and make it into DataFrame
dbf = DBF(filePath)
df = pd.DataFrame(iter(dbf))

# Make new DataFrame with only specified Columns
df = df[columnsToKeep]

sheet = sa.open_by_key(key)
worksheet = sheet.worksheet(worksheetName)

worksheet.clear()
set_with_dataframe(worksheet, df)

