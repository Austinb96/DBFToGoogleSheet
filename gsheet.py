import pandas as pd
from dbfread import DBF
import gspread
from gspread_dataframe import set_with_dataframe

# File for Importing
filePath = ''
# Sheet Key
key = ""
# Worksheet you are working on
worksheetName = ""
# Columns to keep
columnsToKeep = ['']

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

