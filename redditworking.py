from psaw import PushshiftAPI
import datetime
import openpyxl
import os
import pandas as pd

#Set up excel file
def save_submissions(submissions_file, submissions):

    wb = openpyxl.reader.excel.load_workbook(submissions_file)
    sheet = wb.active    
    wb.save(submissions_file)

#API
api = PushshiftAPI()

start_time = int(datetime.datetime(2021,12,14).timestamp())

submissions = api.search_submissions(after=start_time,subreddit='wallstreetbets',filter=['title','created_utc'])

df = pd.DataFrame(submissions)
df.to_csv('redditsubmission.csv')
print('Done!')





