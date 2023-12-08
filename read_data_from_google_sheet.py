#!/home/virtual_envs/google-sheet/bin/python3

from google.oauth2 import service_account
import pandas as pd
import gspread
import json
import os

service_account_info = json.loads(open("/home/amir/Downloads/medusa-log-hours-sheet-ff646cb32860.json", 'r').read())
credentials = service_account.Credentials.from_service_account_info(service_account_info)
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds_with_scope = credentials.with_scopes(scope)
client = gspread.authorize(creds_with_scope)
spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1n9ssE2QmfN9KPIId3tz9s-gi2wGJ5kZcQg1TNsLoB7w/edit#gid=443238577')
worksheet = spreadsheet.get_worksheet(-1)
records_data = worksheet.get_all_values()
df = pd.DataFrame.from_dict(records_data)
df.columns = df.iloc[0, :].to_list()
df = df.iloc[1:, :]
df = df.loc[:, :"Invoice #"]
int_cols = ['Hours', 'Minutes', 'Invoice #']
df[int_cols] = df[int_cols].astype(int)
df.Date = pd.to_datetime(df.Date)
